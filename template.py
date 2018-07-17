#! /usr/bin/env python3
# coding: UTF-8

# Author : mz
# Date   : 2018-07-12
# TODO   :

# Version: 0.0.1
# ^ History ^
###

try:
    import demjson
    mz_json = "demjson"
except ImportError as e:
    print("Can find [demjson] module, now import built-in [json] module to replace it.")
    import json
    mz_json = "json"
    pass

import re
#from . import beautify_print.mzp_beautify_print as mzpp
from beautify_print import mzp_beautify_print as mzpp


class ConfException(Exception):
    pass
class ConfFileTypeError(ConfException):
    pass

class ConfTemplateParser:
    pass

class JsonConfParser(ConfTemplateParser):
    def __init__(self, conf_name):
        if not re.search(".*\.json$", str(conf_name)):
            raise ConfFileTypeError("File '{conf_name}' is NOT json type, please check again."\
                                    .format(conf_name = str(conf_name)))
        self.conf_name = str(conf_name)

    def parse_content(self):
        self.data = {}
        if mz_json == "demjson":
            self.data = demjson.decode_file(self.conf_name)
            mzpp(self.data)
        else:#json
            with open(self.conf_name,  'r', encoding = 'utf-8') as _f:
                self.data = json.loads(_f.read())
                mzpp(self.data)
        return self.data

