# -*- coding: utf-8 -*-
"""
DESCRIPTION
"""

import os
import shutil
import random

datas = r"C:\Users\evgeny\Desktop\keras-tutorial\keras-tutorial\animals"
datas = os.path.abspath(datas)

test_datas = r"C:\Users\evgeny\Desktop\keras-tutorial\keras-tutorial\test_animals"
test_datas = os.path.abspath(test_datas)

if (os.path.exists(test_datas)):
    shutil.rmtree(test_datas, ignore_errors=True)
os.mkdir(test_datas)

test_size = 25

for folder, sub_folders, files in os.walk(datas):
    
    if (files):
        
        _, CLASS = os.path.split(folder)
        dir_for_copy = os.path.join(test_datas, CLASS)
        
        if not os.path.exists(dir_for_copy):
                os.mkdir(dir_for_copy)
        
        random.shuffle(files)
        
        counter = round(len(files) / 100 * test_size)
        
        for file in files:
            
            copy_from = os.path.join(folder, file)            
            copy_to = os.path.join(dir_for_copy, file)
            
            shutil.copy2(copy_from, copy_to)
            
            os.remove(copy_from)
            
            counter -= 1
            
            if counter <= 0:
                break