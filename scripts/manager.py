import os
import shutil
import tempfile

temp_folder = tempfile.gettempdir()
temp = f'{temp_folder}\\WatcherCache.txt' 

dir = ""
with open(temp, "r") as f:
    for line in f:
        dir = line.strip()

if not os.path.exists(f"{dir}/text"):
    os.mkdir(f"{dir}/text")

if not os.path.exists(f"{dir}/images"):
    os.mkdir(f"{dir}/images")

if not os.path.exists(f"{dir}/Hdris"):
    os.mkdir(f"{dir}/Hdris")


for i in os.listdir(str(dir)):
    
    if i.endswith("txt"):
        shutil.move(f"{dir}\\{i}", f"{dir}\\text\\{i}") 
    if i.endswith("png"):
        shutil.move(f"{dir}\\{i}", f"{dir}\\images\\{i}") 
    if i.endswith("exr"): 
        shutil.move(f"{dir}\\{i}", f"{dir}\\Hdris\\{i}")
        
    
        