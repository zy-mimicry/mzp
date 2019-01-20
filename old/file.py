#! /usr/bin/env python3
# coding: UTF-8

# Author : mz
# Date   : 2018-07-12
# TODO   :

# Version: 0.0.1
# ^ History ^
###
###

import os
import os.path
import shutil

class FileExecption(Exception):
    pass

class Component:
    def __init__(self, name):
        self.name = name
        pass

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder
        pass

    def delete(self):
        del self.parent.children[self.name]
        pass

class Folder(Component):
    def __init__(self, name):
        super.__init__(name)
        self.children = {}
        pass

    def add_child(self, child):
        pass

    def copy(self, new_path):
        pass

class File(Component):
    def __init__(self, name, contents):
        super.__init__(name)
        self.contents = contents
        pass

    def copy(self, new_path):
        pass


mzroot = Folder('')

def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node
