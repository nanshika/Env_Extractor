#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file_rename_to_SJIS.py
# C:\Script\Util\file_rename_to_SJIS.py "C:/B3/image/" ".+" "png"
import sys, os, re

# 対象リストの作成
def list_target_files(directory, file_list, regular, extension):
    extension = extension
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 対象選定
            if( re.search(r'%s\.%s'%(regular,extension), file) ):
                file_list.append(os.path.join(root, file))
                #print(os.path.join(root, file))

def fix_unSJIS(tarStr):
    return tarStr.encode("SJIS","ignore").decode('SJIS')

def file_rename_to_SJIS(file_list):
    for file in file_list:
        if file.find("戦女神MEMORIA") != -1 :
            # 「～」の処理でコケるため
            pass
        else:
            os.rename(file, file.encode("SJIS","ignore").decode('SJIS'))
            #print(file)

if len(sys.argv) == 4:
    tar_dir   = sys.argv[1]
    regular   = sys.argv[2]
    extension = sys.argv[3]
    file_list = []
    
    list_target_files(tar_dir, file_list, regular, extension)
    file_rename_to_SJIS(file_list)
else:
    print("Please pass the paths to check as parameters to the script")

