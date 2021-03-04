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
from constant.misc import misc

class translation_manager:
    languages: dict = {}
    language: str = "en"
    translations: dict = {}

    @classmethod
    def get_translation(cls, key: str) -> str:
        key = key.split("/")
        if cls.translations == {}:
            with open(f"{misc.translation_dir}/{cls.language}.json", "r") as f:
                cls.translations = json.load(f)
        cd = cls.translations
        for subkey in key:
            cd = cd[str(subkey)]
        return cd

    @classmethod
    def set_language(cls, language: str) -> None:
        language = language.lower()
        cls.language = language
        languages = cls.get_languages()
        if language not in languages.keys():
            raise ValueError("Invalid language.")
        with open(f"{misc.translation_dir}/{language}.json", "r") as f:
            cls.translations = json.load(f)

    @classmethod
    def get_languages(cls) -> dict:
        if cls.languages == {}:
            with open(f"{misc.translation_dir}/languages.json") as f:
                cls.languages = json.load(f)
        return cls.languages
