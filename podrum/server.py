################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################
import json
import os

from constant.misc import misc
from constant.translations import translations
from constant.vanilla_commands import vanilla_commands
from handler.command_handler import command_handler
from manager.command_manager import command_manager
from manager.event_manager import event_manager
from manager.plugin_manager import plugin_manager
import time
from utils.logger import logger


class server:
    def __init__(self) -> None:
        self.command_manager = command_manager(self)
        self.command_handler = command_handler(self)
        self.logger = logger()
        self.plugin_manager = plugin_manager(self)
        self.event_manager = event_manager()
        with open(os.getcwd() + "/podrum/server.json", 'r') as f:
            self.config = json.load(f)
        translations.set_language(self.config['language'])
        self.start()

    def register_vanilla_commands(self) -> None:
        self.command_manager.register(vanilla_commands.say, translations.get_translation('commands/descriptions/say'))
        self.command_manager.register(vanilla_commands.stop, translations.get_translation('commands/descriptions/stop'))
        self.command_manager.register(vanilla_commands.help, translations.get_translation('commands/descriptions/help'))
        self.command_manager.register(vanilla_commands.version, translations.get_translation('commands/descriptions/version'))
        self.command_manager.register(vanilla_commands.reload, translations.get_translation('commands/descriptions/reload'))
        self.command_manager.register(vanilla_commands.plugins, translations.get_translation('commands/descriptions/plugins'))

    def get_plugin_main(self, name):
        if name in self.plugin_manager.plugins:
            return self.plugin_manager.plugins[name]

    def start(self) -> None:
        start_time = time.time()
        print(misc.logo)
        self.plugin_manager.load_all(misc.plugin_dir)
        self.register_vanilla_commands()
        self.command_handler.start_handler()
        finnish_time = time.time()
        startup_time = "%.3f" % (finnish_time - start_time)
        self.logger.success(translations.get_translation('serverStarted').format(startup_time))

    def stop(self) -> None:
        self.command_handler.stop_handler()
        self.plugin_manager.unload_all()

    def send_message(self, message: str) -> None:
        self.logger.info(message)
