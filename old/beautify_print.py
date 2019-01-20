#! /usr/bin/env python3
# coding: UTF-8

# Author : mz
# Date   : 2018-07-12
# TODO   :

# Version: 0.0.1
# ^ History ^
###
###

class PrintException(Exception):
    pass
class BackendTypeError(PrintException):
    pass

def __mzp_print_tuple(t_tuple, indent = 2):
    print(" " * indent + "(")
    for _t in t_tuple:
        if type(_t) == type(tuple):
            __mzp_print_tuple(_t, indent = indent + 4)
        elif type(_t) == type({}):
            __mzp_print_dict(_t, indent = indent + 4)
        elif type(_t) == type([]):
            __mzp_print_list(_t, indent = indent + 4)
        else:
            print(" " * (indent + 2) , end = "")
            print("{}".format(_t), end = ",\n")
    print(" " * indent + ")")

def __mzp_print_list(l_list, indent = 2):
    print(" " * indent + "[")
    for _i in l_list:
        if type(_i) == type([]):
            __mzp_print_list(_i, indent = indent + 4)
        elif type(_i) == type({}):
            __mzp_print_dict(_i, indent = indent + 4)
        elif type(_i) == type(()):
            __mzp_print_tuple(_i, indent = indent + 4)
        else:
            print(" " * (indent + 2) , end = "")
            print("{}".format(_i), end = ",\n")
    print(" " * indent + "]")

def __mzp_print_dict(d_dict, indent = 2):
    print(" " * indent + "{")
    for k,v in d_dict.items():
        print(" " * (indent + 2) , end = "")
        if type(v) == type({}):
            print("{key} : ".format(key = k))
            __mzp_print_dict(v, indent = indent + 4)
        elif type(v) == type([]):
            print("{key} : ".format(key = k))
            __mzp_print_list(v, indent = indent + 4)
        elif type(v) == type(()):
            print("{key} : ".format(key = k))
            __mzp_print_tuple(v, indent = indent + 4)
        else:
            print("{key} : {value}".format(key = k, value = v))
    print(" " * indent + "}")

def beautiful_print(func):
    def b_print(*vargs,  **kwargs):
        _b = "*"*50
        print(_b + "Mzp Print BEG" + _b)
        func(*vargs, **kwargs)
        print(_b + "Mzp Print END" + _b)
    return b_print

def _mzp_beautify_print_backend(any_thing, *kargs, indent = 2, **kwargs):
    '''
    mzp print beautiful format.

    Now, support those types
    1. list type
    2. dict type
    3. tuple type
    '''
    if type(any_thing) == type([]):
        __mzp_print_list(any_thing, indent = indent)
    elif type(any_thing) == type(()):
        __mzp_print_tuple(any_thing, indent = indent)
    elif type(any_thing) == type({}):
        __mzp_print_dict(any_thing, indent = indent)
    else:
        print(any_thing)

def _mzp_pprint_backend(any_thing, *kargs, indent = 2, depth = None, **kwargs):
    'Call the pprint.pprint to format.'
    from pprint import pprint as pp
    pp(any_thing, *kargs, indent = indent, depth = depth,**kwargs)


@beautiful_print
def mzp_beautify_print(any_thing, *kargs, backend = 'mzp', **kwargs):
    '''
    Print Beautifully, and backend which can be chosed.

    Now, support backend:
    1. mzp
    2. pp
    '''
    mzp_backend = ['pp', 'mzp']
    if backend not in mzp_backend:
        raise BackendTypeError("Please input the correct backend type, \nchosen: {}".format(mzp_backend))
    if backend == 'pp':
        _mzp_pprint_backend(any_thing, *kargs, **kwargs)
    else:#backend == 'mzp':
        _mzp_beautify_print_backend(any_thing, *kargs, **kwargs)


if __name__ == "__main__":
    zz = {'root-path': './',
    'root-name': 'root',
    'description': 'Just for test for root path.',
    'sub-nodes': {'local-files': [{'file-name': 'file1',
        'file-actions': {'move': True, 'from': '', 'to': ''}}],
    'local-folders': {'folder-name': 'folder1',
    'local-files': [100, 2, 4 ,{"hello" : 888, 100 : "dd" , (100,99): "jjj" , "mm" : [100 , 22]}],
    'local-folders': {'folder-name': 'folder11',
        'local-files': [100, "jk", ["fuck",(1,2,3,4,5), {100 : 11}]],
        'local-folders': {}}}}}
    mzp_beautify_print(zz)
    mzp_beautify_print(zz, backend = 'pp')
