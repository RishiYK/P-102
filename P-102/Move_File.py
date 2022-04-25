
import os
import shutil
from unicodedata import name

from_dir="C:/Users/lenovo/Downloads/Random"
to_dir='E:/P-102'
list_of_files=os.listdir(from_dir)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)

    if extension=='':
        continue


    if extension in ['.pdf']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Document_Files'
        path3=to_dir+'/'+'Document_Files'+file_name
        

        if os.path.exists(path2):
            print("moving"+file_name+"......")
            shutil.move(path1,path2)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"....")
            shutil.move(path1,path2)
