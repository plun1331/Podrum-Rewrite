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

from constant.version import version
from constant.translations import translations
import os

class vanilla_commands:
    @staticmethod
    def say(args: list, sender, server) -> None:
        if len(args) > 0:
            sender.send_message(" ".join(args))
        else:
            sender.send_message("say <message>")

    @staticmethod
    def stop(args: list, sender, server) -> None:
        sender.send_message(translations.get_translation('commands/content/stop/0'))
        server.stop()
        sender.send_message(translations.get_translation('commands/content/stop/1'))
        os.kill(os.getpid(), 15)
        
    @staticmethod
    def help(args: list, sender, server) -> None:
        sender.send_message(f"--- {translations.get_translation('commands/content/help')} ---")
        for name, info in dict(server.command_manager.commands).items():
            sender.send_message(f"/{name}: {info['description']}")
          
    @staticmethod
    def version(args: list, sender, server) -> None:
        sender.send_message(translations.get_translation('commands/content/version').format(version))

    @staticmethod
    def reload(args: list, sender, server) -> None:
        sender.send_message(translations.get_translation('commands/content/reload/0'))
        server.plugin_manager.reload_all()
        sender.send_message(translations.get_translation('commands/content/reload/1'))
                                
    @staticmethod
    def plugins(args: list, sender, server) -> None:
        sender.send_message(f"{translations.get_translation('commands/content/plugins')}({len(server.plugin_manager.plugins)}): {', '.join(server.plugin_manager.plugins)}")
