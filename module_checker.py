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

if __name__ == '__main__':
    input_is_excel = 0
    usage = "%prog [options] <input_Excel_file> [<output_txt_file>] \n"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    
    if len(args) == 1:
        # 出力ファイルの指定がない場合
        args.append(args[0].replace('.py','_modules.txt'))
    elif len(args) != 2:
        # 引数に過不足がある場合の対処
        parser.error("Check the usage and arguments!")
    
    make_module_list(args[0], args[1])

