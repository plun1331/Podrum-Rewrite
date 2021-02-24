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

from constant.misc import misc
from constant.vanilla_commands import vanilla_commands
from handler.command_handler import command_handler
from manager.command_manager import command_manager
import os
import time
from utils.logger import logger

class server:
    def __init__(self) -> None:
        self.command_manager = command_manager(self)
        self.command_handler = command_handler(self)
        self.start()

    def register_vanilla_commands(self) -> None:
        self.command_manager.register(vanilla_commands.say, "Say Command")
        self.command_manager.register(vanilla_commands.stop, "Stop Command")
        self.command_manager.register(vanilla_commands.help, "Help Command")
        self.command_manager.register(vanilla_commands.version, "Version Command")

    def start(self) -> None:
        logger.enable_windows_formatting()
        start_time = time.time()
        print(misc.logo)
        self.register_vanilla_commands()
        self.command_handler.start_handler()
        finnish_time = time.time()
        startup_time = "%.3f" % (finnish_time - start_time)
        logger.success(f"Done in {startup_time}. Type help to view all available commands.")
        
    def stop(self) -> None:
        self.command_handler.stop_handler()
        os.kill(os.getpid(), 15)

    def send_message(self, message: str) -> None:
        logger.info(message)
