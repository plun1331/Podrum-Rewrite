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
from datetime import datetime
import inspect

class logger:
    @staticmethod
    def log(log_type, content):
        date_time = datetime.now()
        if log_type.lower() == "info":
            color = text_format.blue
        elif log_type.lower() == "warn":
            color = text_format.yellow
        elif log_type.lower() == "error":
            color = text_format.red
        elif log_type.lower() == "success":
            color = text_format.green
        elif log_type.lower() == "emergency":
            color = text_format.gold
        elif log_type.lower() == "alert":
            color = text_format.purple
        elif log_type.lower() == "notice":
            color = text_format.aqua
        elif log_type.lower() == "critical":
            color = text_format.darkRed
        elif log_type.lower() == "debug":
            color = text_format.gray
        else:
            return
        print(f"{color}[{log_type.upper()}: {date_time.strftime('%H:%M')}]{text_format.white} {content}")

    @staticmethod
    def info(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def warn(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def error(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def success(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def emergency(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def alert(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def notice(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def critical(content):
        logger.log(inspect.stack()[0][3], content)

    @staticmethod
    def debug(content):
        logger.log(inspect.stack()[0][3], content)
