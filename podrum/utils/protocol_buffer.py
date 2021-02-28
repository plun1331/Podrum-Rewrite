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

import struct

class protocol_buffer:
    def __init__(self, data: bytes = b"", pos: int = 0) -> None:
        self.data: bytes = data
        self.pos: int = pos
        
    def read(self, byte_count: int) -> bytes:
        self.pos += byte_count
        return self.data[self.pos - byte_count: self.pos]

    def write(self, data: bytes) -> None:
        self.data += data
        
    def read_char(self) -> int:
        return struct.unpack("b", self.read(1))[0]

    def write_char(self, value: int) -> None:
        self.write(struct.pack("b", value))
        
    def read_uchar(self) -> int:
        return struct.unpack("B", self.read(1))[0]

    def write_uchar(self, value: int) -> None:
        self.write(struct.pack("B", value))
        
    def read_bool(self) -> bool:
        return struct.unpack("?", self.read(1))[0]

    def write_bool(self, value: bool) -> None:
        self.write(struct.pack("?", value))

    def read_short(self, endianess: str) -> int:
        if endianess.lower() == "big":
            byte_order = ">"
        elif endianess.lower() == "little":
            byte_order = "<"
        else:
            return
        return struct.unpack(byte_order + "h", self.read(1))[0]

    def write_short(self, value: int, endianess: str) -> None:
        if endianess.lower() == "big":
            byte_order = ">"
        elif endianess.lower() == "little":
            byte_order = "<"
        else:
            return
        self.write(struct.pack(byte_order + "h", value))