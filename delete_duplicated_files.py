# python delete_duplicated_files.py 
# -*- coding: utf-8 -*-
import sys, os, re, shutil

# src*配下のファイルがtar*配下にあれば削除
# 対象リストの作成
def list_target_files(directory, file_list, regular, extension):
    extension = extension
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 対象選定
            if( re.search(r'%s\.%s'%(regular,extension), file) ):
                file_list.append(os.path.join(root, file))
                # print(os.path.join(root, file))

def delete_duplicated_files(directory, tar_file_list, exception_dir):
    """ 対象フォルダと別のフォルダで同じファイル名のファイルがあれば削除
        NB. ファイル名しか見ていない """
    for root, dirs, files in os.walk(directory):
        # 削除対象フォルダは除外。それ以外を対象に操作
        if not root == exception_dir:
            # print("searching... " + root)
            for file in files:
                # 対象選定
                src_file_name = os.path.join(root, file)
                for tar_file in tar_file_list:
                    tar_file_name = tar_file.split("\\")[-1]
                    if( file.find(tar_file_name) != -1 ):
                        """ 初めに該当したファイルは移動、それ以降は削除 """
                        try:
                            shutil.move(src_file_name, del_dir)
                            print("moved:    " + src_file_name)
                        except:
                            os.remove(src_file_name)
                            print(" deleted: " + src_file_name)

# 汎例
"""
tar_dir = r"C:\B3\docs\婚活\010000_seen"
src_dir = r"C:\B3\docs\婚活"
del_dir = "C:\_deletable\_Nul"
list_target_files(tar_dir, tar_file_list,".+","png")
delete_duplicated_files(src_dir, tar_file_list, tar_dir)
"""
if len(sys.argv) > 2:
    tar_dir = sys.argv[1]
    src_dir = sys.argv[2]
    try:
        dummy = len(sys.argv[3])
        del_dir = sys.argv[3] 
    except:
        del_dir = "C:\_deletable\_Nul"
        
    tar_file_list = []

    list_target_files(tar_dir, tar_file_list,".+","png|jpg|mp3")
    delete_duplicated_files(src_dir, tar_file_list, tar_dir)
else:
    print("Please pass the paths to check as parameters to the script")

