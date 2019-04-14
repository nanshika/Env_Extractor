# python delete_few_files_dirs.py "C:\_deletable\ex\nhentai.net"
# -*- coding: utf-8 -*-
import sys, os, re, shutil
THRESHOLD = 10

# 指定ファイル数未満しか格納していないフォルダを、ファイルごと削除
def delete_few_files_dirs(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            for root2, dirs2, files2 in os.walk(os.path.join(root,dir)):
                if len(files2) < THRESHOLD:
                    for file2 in files2:
                        print(os.path.join(root2,file2))
                        os.remove(os.path.join(root2,file2))
                    
                    print('removed: '+root2)
                    os.removedirs(root2)


if __name__ == '__main__':
    delete_few_files_dirs(r'C:\_deletable\ex\nhentai.net')
    delete_few_files_dirs(r'C:\_deletable\ex\nh_2')
    
    if len(sys.argv) == 2:
        directory = sys.argv[1]
        delete_few_files_dirs(directory)
    else:
        print("Please pass the paths to check as parameters to the script")

