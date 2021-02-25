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
from utils.core_utils import core_utils
from zipfile import ZipFile

class plugin_manager:
    def __init__(self, server) -> None:
        self.server = server
        self.plugins: dict = {}
        self.plugin_count = 0
        
    def load(self, path: str) -> None:
        plugin_file = ZipFile(path, "r")
        plugin_info = json.loads(plugin_file.read("info.json"))
        if plugin_info["name"] in self.plugins:
            return
        if plugin_info["api_version"] != version.podrum_api_version:
            return
        sys.path.append(path)
        main = plugin_info["main"].rsplit(".", 1)
        module = importlib.import_module("plugins." + main[0])
        main_class = getattr(module, main[1])
        self.plugins[plugin_info["name"]] = main_class()
        self.plugins[plugin_info["name"]].server = self.server
        self.plugins[plugin_info["name"]].version = plugin_info["version"] if "version" in plugin_info else ""
        self.plugins[plugin_info["name"]].description = plugin_info["description"] if "description" in plugin_info else ""
        self.plugins[plugin_info["name"]].author = plugin_info["author"] if "author" in plugin_info else ""
        if core_utils.has_attribute(main_class, "on_load"):
            self.plugins[plugin_info["name"]].on_load()
        self.plugin_count += 1
        
    def load_all(self, path: str) -> None:
        for top, dirs, files in os.walk(path):
            for file_name in files:
                full_path = os.path.abspath(os.path.join(top, file_name))
                if full_path.endswith(".pyz") or full_path.endswith(".zip"):
                    self.load(full_path)
        
    def unload(self, name: str) -> None:
        if name in self.plugins:
            if core_utils.has_attribute(self.plugins[name], "on_unload"):
                self.plugins[name].on_unload()
            del self.plugins[name]
            self.plugin_count -= 1
            
    def unload_all(self) -> None:
        for name in self.plugins:
            self.unload(name)
