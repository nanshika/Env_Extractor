# python C:\Script\Util\anime_file_rename.py
# -*- coding: utf-8 -*-
import sys, os, re

# 対象リストの作成
def anime_file_rename(directory, regular_expression, extension):
    cnt_success = 0
    cnt_failure = 0
    log_file = 'C:/Script/Util/anime_file_rename.log'
    f = open(log_file,'a')
    #print("\n--- " + directory + " ---\n")
    extension = extension
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 対象選定
            if( re.search(r'%s\.%s'%(regular_expression,extension), file) ):
                mod_file_name = file
                try:
                    chapter_sub = re.search(r' \d  ',mod_file_name)
                    #chapter = file[chapter_sub.start()+1:chapter_sub.end()-2]
                    #mod_file_name = file[0:re.search(r" Episode",file).start()] + "_#0" + chapter + "_Eng.mp4"
                    mod_file_name = re.sub(r'\[.+?\] ','', mod_file_name)
                    mod_file_name = re.sub(r' - ','_#', mod_file_name)
                    mod_file_name = re.sub(r'\[.+?\.','.', mod_file_name)
                    mod_file_name = re.sub(r' English SubbedDubbed Full HD for Free.*\.mp4','_Eng.mp4', mod_file_name)
                    mod_file_name = re.sub(r'[ _-]*Watch anime online, English anime online.*\.mp4','_Eng.mp4', mod_file_name)
                    mod_file_name = re.sub(r'[ _-]*Watch anime online, English anime online.*\.flv','_Eng.mp4', mod_file_name)
                    mod_file_name = re.sub(r'- anime-Eng, English anime-Eng| *HD Stream *Hentai Haven| anime-Eng, English anime-Eng| English Subbedat Gogoanime','_Eng', mod_file_name)
                    mod_file_name = re.sub(r'play44_| - Hentai Stigma - Stream - Hentai-Eng','', mod_file_name)
                    mod_file_name = re.sub(r' Episode ','_#', mod_file_name) 
                    mod_file_name = re.sub(r'_+','_', mod_file_name) 
                    mod_file_name = re.sub(r'Watch ','', mod_file_name) 
                    #mod_file_name = re.sub(r' Online','-Eng', mod_file_name)
                    mod_file_name = re.sub(r' - VLCメディアプレイヤー| - GOM Player| - ニコニコ動画_GINZA| - ニコニコ動画','', mod_file_name)
                    mod_file_name = re.sub(r'  ',' ', mod_file_name)
                    if re.search("_#\d_",mod_file_name):
                        mod_file_name = mod_file_name.replace('_#','_#0')
                    
                except:
                    pass
                
                finally:
                    #print(mod_file_name)
                    if file != mod_file_name:
                        
                        try:
                            os.rename(os.path.join(root, file), os.path.join(root, mod_file_name))
                            print("before:" + file) 
                            print(" after:" + mod_file_name)
                            f.write(root + "\t" + file + "\t" + mod_file_name + "\n")
                            cnt_success += 1
                        except:
                            cnt_failure += 1
                            pass
    if cnt_success + cnt_failure != 0:
        print("\n=== Renaming finished for " + str(cnt_success) + " files,"
                        + " and failed for " + str(cnt_failure) + " files ===")

def list_up_animes(anime_dir_list, regular_expression, extension):
    anime_title_dict = {}
    #print("\n--- " + directory + " ---\n")
    for directory in anime_dir_list:
        for root, dirs, files in os.walk(directory):
            for file in files:
                # 対象選定
                if( re.search('(%s)\.(%s)'%(regular_expression,extension), file)):
                    anime_title = re.search(".+[#第]",file).group()[0:-2]
                    anime_num   = re.search("[#第]\d+",file).group()[1:99]
                    try:
                        anime_title_dict[anime_title] = anime_title_dict[anime_title] if anime_title_dict[anime_title] > anime_num else num
                    except:
                        anime_title_dict[anime_title] = anime_num
    
    for key, value in sorted(anime_title_dict.items(), key=lambda x:x[1], reverse=1):
        dummy_file = "C:/__yetMoved/_movie__R/__fin/"+"{}_#{}".format(key,value)+".txt"
        if int(value) < 12:
            print("{}\t{}".format(value, key))
            with open(dummy_file,"w") as f:
                pass

def onsen_rename(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            for file in files:
                mod_file = file.replace('fmc2','■')
                if( re.search('(.+?)(\d{6})(.+?\.mp3)', file )):
                     try:
                         mod_file = re.sub('(.+?)(\d{6})(.+?\.mp3)',r'\2_\1_\3',mod_file)
                         mod_file = mod_file.replace('■','fmc2')
                         print(root+"\t"+file+"\t→\t"+mod_file)
                         os.rename(file, mod_file)
                         os.rename(mod_file, mod_file.replace(' (1)',''))
                     except:
                        pass

def main():
    DEFAULT_PATH = "C:/Users/works/yet"
    
    # 引数がないときは標準設定で検索
    if len(sys.argv) > 1:
        tar_path = sys.argv[1]
    else:
        tar_path = DEFAULT_PATH
    
    onsen_rename(tar_path)
    #anime_file_rename(tar_path, ".+", "mp4|flv")
    #anime_dir_list = [tar_path,r"C:\__yetMoved\_movie__R"]
    #list_up_animes(anime_dir_list, ".+#\d+.+", "mp4|flv|txt")

if __name__ == '__main__':
    main()

#anime_dir_list = [r"C:\Users\works\yet",r"C:\__yetMoved\_movie__R", "R:\アニメ"]
#list_up_animes(anime_dir_list, ".+[#第]\d+.+", "mp4|flv|txt")
