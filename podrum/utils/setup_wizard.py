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

def yesNo(user_input):
    if user_input.lower() in ('y', 'yes'):
        return True
    if user_input.lower() in ('n', 'no'):
        return False


class setup_wizard:
    step = 0
    config = {'port': 19132,
              'motd': 'A Podrum server.',
              'gamemode': 0,
              'maxPlayers': 5}

    def __init__(self):
        while True:
            if self.step == 0:
                t = translation_manager.get_languages()
                send = ''
                for lang in t:
                    send += f"{t[lang]} -> {lang}\n"
                send = send.strip('\n')
                print(send)
                select_lang = input("> Please select a language: ")
                if select_lang.lower() not in t:
                    print("Invalid language.")
                    continue
                self.config['language'] = select_lang.lower()
                translation_manager.set_language(select_lang.lower())
                print(translation_manager.get_translation('wizard/langSelected').format(t[select_lang.lower()]))
                self.step += 1
            if self.step == 1:
                yn = input(f"> {translation_manager.get_translation('wizard/licensePrompt').format(version.podrum_license)}")
                if yesNo(yn) is None:
                    continue
                if not yesNo(yn):
                    print(translation_manager.get_translation('wizard/acceptLicense'))
                    continue
                self.step += 1
            if self.step == 2:
                print(misc.logo)
                yn = input(f"> {translation_manager.get_translation('wizard/continuePrompt')}")
                if not yesNo(yn):
                    print(translation_manager.get_translation('wizard/skipped'))
                    with open(os.getcwd() + '/podrum/server.json', 'w') as f:
                        json.dump(self.config, f)
                    break
                self.step += 1
            if self.step == 3:
                port = input(f"> {translation_manager.get_translation('wizard/selectPort')}")
                if port == '':
                    port = '19132'
                if port.isdigit():
                    self.config['port'] = int(port)
                else:
                    continue
                print(translation_manager.get_translation('wizard/portSet').format(self.config['port']))
                self.step += 1
            if self.step == 4:
                motd = input(f"> {translation_manager.get_translation('wizard/selectMOTD')}")
                if motd == '':
                    motd = 'A Podrum server.'
                self.config['motd'] = motd
                print(translation_manager.get_translation('wizard/MOTDSet').format(self.config['motd']))
                self.step += 1
            if self.step == 5:
                gamemode = input(f"> {translation_manager.get_translation('wizard/selectGamemode')}")
                if gamemode == '':
                    gamemode = '0'
                if gamemode.isdigit():
                    self.config['gamemode'] = int(gamemode)
                else:
                    continue
                print(translation_manager.get_translation('wizard/gamemodeSet').format(self.config['gamemode']))
                self.step += 1
            if self.step == 6:
                max_players = input(f"> {translation_manager.get_translation('wizard/selectMaxPlayers')}")
                if max_players == '':
                    max_players = '5'
                if max_players.isdigit():
                    self.config['maxPlayers'] = int(max_players)
                else:
                    continue
                print(translation_manager.get_translation('wizard/maxPlayersSet').format(self.config['maxPlayers']))
                self.step += 1
            if self.step == 7:
                print(translation_manager.get_translation('wizard/complete'))
                with open(os.getcwd() + '/podrum/server.json', 'w') as f:
                    json.dump(self.config, f)
                break

