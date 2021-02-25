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
import importlib
import json
import os
import sys
from zipfile import ZipFile

class plugin_manager:
    def __init__(self, server, path: str) -> None:
        self.server = server
        self.plugins: dict = {}
        self.plugin_count = 0
        self.path = path
        
    def load(self, path: str) -> None:
        plugin_file = ZipFile(path, "r")
        plugin_info = json.loads(plugin_file.read("info.json"))
        if plugin_info["name"] in self.plugins:
            return
        if plugin_info["api"] != version.podrum_api:
            return
        sys.path.append(path)
        main = pluginInfo["main"].rsplit(".", 1)
        module = importlib.import_module(main[0])
        main_class = getattr(module, main[1])
        self.plugins[plugin_info["name"]] = main_class()
        self.plugins[plugin_info["name"]].server = self.server
        self.plugins[plugin_info["name"]].version = info["version"] if "version" in plugin_info else ""
        self.plugins[plugin_info["name"]].description = info["description"] if "description" in plugin_info else ""
        self.plugins[plugin_info["name"]].on_load()
        self.plugin_count += 1
        
    def load_all() -> None:
        for file_name in os.listdir(self.path):
            if os.path.isfile(path):
                if path.endswith(".pyz"):
                    self.load(path)
        
    def unload(self, name: str) -> None:
        if name in self.plugins:
            self.plugins[name].on_unload()
            del self.plugins[name]
            self.plugin_count -= 1
            
    def unload_all(self) -> None:
        for name in self.plugins:
            self.unload(name)
