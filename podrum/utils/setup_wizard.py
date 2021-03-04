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

from manager.translation_manager import translation_manager
from constant.version import version
from constant.misc import misc

def yes_no(user_input):
    if user_input.lower() in ('y', 'yes'):
        return True
    if user_input.lower() in ('n', 'no'):
        return False

class setup_wizard:
    def __init__(self):
        self.config = {
            "port": 19132,
            "motd": 'A Podrum server.',
            "gamemode": 0,
            "max_players": 5
        }
        self.step = 0
        self.start_setup()
                   
    def start_setup(self):
        while 0 <= self.step <= 6:
            if self.step == 0:
                self.step_one()
            elif self.step == 1:
                self.step_two()
            elif self.step == 2:
                self.step_three()
            elif self.step == 3:
                self.step_four()
            elif self.step == 4:
                self.step_five()
            elif self.step == 5:
                self.step_six()
            elif self.step == 6:
                self.step_seven()

    def step_one(self):
        t = translation_manager.get_languages()
        send = ''
        for lang in t:
            send += f"{t[lang]} -> {lang}\n"
        send = send.strip('\n')
        print(send)
        select_lang = input("> Please select a language: ")
        if select_lang.lower() not in t:
            print("Invalid language.")
            return
        self.config['language'] = select_lang.lower()
        translation_manager.set_language(select_lang.lower())
        print(translation_manager.get_translation('wizard/lang_selected').format(t[select_lang.lower()]))
        self.step += 1

    def step_two(self):
        yn = input(f"> {translation_manager.get_translation('wizard/license_prompt').format(version.podrum_license)}")
        if yes_no(yn) is None:
            return
        if not yes_no(yn):
            print(translation_manager.get_translation('wizard/accept_license'))
            return
        self.step += 1

    def step_three(self):
        print(misc.logo)
        yn = input(f"> {translation_manager.get_translation('wizard/continue_prompt')}")
        if not yes_no(yn):
            print(translation_manager.get_translation('wizard/skipped'))
            with open(os.getcwd() + '/podrum/server.json', 'w') as f:
                json.dump(self.config, f)
            self.step = 8
            return
        self.step += 1

    def step_four(self):
        port = input(f"> {translation_manager.get_translation('wizard/select_port')}")
        if port == '':
            port = '19132'
        if port.isdigit():
            self.config['port'] = int(port)
        else:
            return
        print(translation_manager.get_translation('wizard/port_set').format(self.config['port']))
        self.step += 1

    def step_five(self):
        gamemode = input(f"> {translation_manager.get_translation('wizard/select_gamemode')}")
        if gamemode == '':
            gamemode = '0'
        if gamemode.isdigit():
            self.config['gamemode'] = int(gamemode)
        else:
            return
        print(translation_manager.get_translation('wizard/gamemode_set').format(self.config['gamemode']))
        self.step += 1

    def step_six(self):
        max_players = input(f"> {translation_manager.get_translation('wizard/select_max_players')}")
        if max_players == '':
            max_players = '5'
        if max_players.isdigit():
            self.config['max_players'] = int(max_players)
        else:
            return
        print(translation_manager.get_translation('wizard/max_players_set').format(self.config['max_players']))
        self.step += 1

    def step_seven(self):
        print(translation_manager.get_translation('wizard/complete'))
        with open(os.getcwd() + '/podrum/server.json', 'w') as f:
            json.dump(self.config, f)
        self.step += 1
