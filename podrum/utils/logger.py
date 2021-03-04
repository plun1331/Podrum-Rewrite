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

from constant.text_format import text_format
from constant.translations import translations
from datetime import datetime
import inspect
import sys

class logger:
    def __init__(self):
        if sys.platform == "win32" or sys.platform == "win64":
            from ctypes import windll
            kernel = windll.kernel32
            kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
        
    def log(self, log_type: str, content: str) -> None:
        date_time = datetime.now()
        if log_type.lower() == "info":
            color: str = text_format.blue
        elif log_type.lower() == "warn":
            color: str = text_format.yellow
        elif log_type.lower() == "error":
            color: str = text_format.red
        elif log_type.lower() == "success":
            color: str = text_format.green
        elif log_type.lower() == "emergency":
            color: str = text_format.gold
        elif log_type.lower() == "alert":
            color: str = text_format.purple
        elif log_type.lower() == "notice":
            color: str = text_format.aqua
        elif log_type.lower() == "critical":
            color: str = text_format.darkRed
        elif log_type.lower() == "debug":
            color: str = text_format.gray
        else:
            return
        print(f"{color}[{translations.get_translation(f'logger/{log_type.lower()}')}: {date_time.strftime('%H:%M')}]{text_format.white} {content}")

    def info(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def warn(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def error(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def success(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def emergency(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def alert(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def notice(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)
              
    def critical(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)

    def debug(self, content: str) -> None:
        self.log(inspect.stack()[0][3], content)
