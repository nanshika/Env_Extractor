#!/usr/bin/env python
# -*- coding: SJIS -*-
# python module_checker.py C:/Script/tmp/a/scraping-img-11_dummy.py
from modulefinder import ModuleFinder
from optparse import OptionParser
import numpy as np

def make_module_list(input_file, output_file):
    module_list = []
    finder = ModuleFinder()
    finder.run_script(input_file)
    
    keys = sorted(finder.modules.keys())
    for key in keys:
        if finder.modules[key].__path__ and key.find(".") == -1:
            module_list.append(key)
    
    with open(output_file, "w") as f_o:
        f_o.write('pip install ' + ' '.join(module_list))
        print('pip install ' + ' '.join(module_list))

import sys
def module_check():
    # Check what's imported by this script
    print('Script name:', end=' ')
    print(__file__)
    print('-'*(20 + len(__file__)) +'\npip install', end=' ')
    for module in sorted(sys.modules.keys()):
        if module.find('_') == -1 and module.find('.') == -1:
            print(module, end=' ')

module_check()
