# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:23:44 2023

@author: suxiaozhou

Using AI technology to help to Created.
"""

import os
import time
import chardet

#Optional variables#########################################
path="mycode/";
mode=1;#1 mean GB2312 to UTF-8;0 mean UTF-8 to GB2312.
file_extensions='.cpp';#后缀
############################################################

Processed_num=0

def convert_encoding(file_path, new_encoding):
    global Processed_num
    Processed_num+=1
    print(file_path)
    with open(file_path, 'rb') as f:
        data = f.read()
    with open(file_path, 'wb') as f:
        #print(data.decode(chardet.detect(data)['encoding']).encode(new_encoding))
        f.write(data.decode(chardet.detect(data)['encoding']).encode(new_encoding))

def main(directory, codeflag):
    start_time = time.time()
    cpp_files = [f for f in os.listdir(directory) if f.endswith(file_extensions)]#here are Filter_criteria.
    cpp_files.sort()
    print(cpp_files)
    for i, file_name in enumerate(cpp_files):
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'rb') as f:
            data = f.read()
        detected_encoding = chardet.detect(data)['encoding']
        #print(detected_encoding,end=" ")
        if codeflag == 1 and detected_encoding == 'GB2312':  # 将GB2312转为UTF-8  GB2312 to UTF-8
            convert_encoding(file_path, 'utf-8')
        elif codeflag == 0 and detected_encoding == 'utf-8':  # 将UTF-8转为GB2312 UTF-8 to GB2312
            convert_encoding(file_path, 'GB2312')

    end_time = time.time()
    print("Check "+str(len(cpp_files))+" files in total. Processed "+str(Processed_num)+" files in total. Total time "+str(end_time - start_time)+" seconds.")

if __name__ == '__main__':
    main(path, mode)
"""
遍历指定目录下的所有.cpp文件，根据编码方式转换文件编码。
指定要遍历的目录
编码转换标志(mode)：1表示将GB2312转为UTF-8，0表示将UTF-8转为GB2312
"""