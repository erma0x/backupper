import glob
import os
import time
from datetime import datetime

'''
sudo python3 backupper.py

Backup from one directory to another automatically
also works with USB and external drives
'''

def get_files(directory:str, extensions:list ,dir_to_exclude:list = ['venv']):
    file_paths = []
    for ext in extensions:
        files = glob.glob(directory+'/**/*' + ext, recursive = True)
        
        for file_path in files:
            ok = True
            
            for i in dir_to_exclude:
                if i in file_path:
                   ok = False 
                
            if ok:
               file_paths.append(file_path)
            
    return file_paths


def backupper(my_directory:list =['/media/directory_to_backup1'], backup_directories:list  =['/media/external_drive/'],extensions:list  = ['.csv','.txt'], dir_to_exclude:list  = ['venv','__pycache__','__init__']):
    backup_directory = [f"{i}{str(datetime.now())[:10].replace(' ','_').replace('.','_').replace(':','_')}/" for i in backup_directories]

    for bk in backup_directory:
        for j in my_directory:
            moving_files = get_files(directory = j, extensions=extensions, dir_to_exclude = dir_to_exclude)   

            for i in range(len(moving_files)):

                backupping_directory = '/'.join(moving_files[i].split('/')[:-1]).replace(j,bk).replace('//','/').replace(' ','')
                if not os.path.isdir(backupping_directory,): 
                    os.makedirs(backupping_directory)

                backupping_path = backupping_directory + '/' + moving_files[i].split('/')[-1]                  
                cmd = f"sudo cp '{moving_files[i]}' '{backupping_path}'"
                print(cmd)
                os.system(cmd)


def main():

    to_backup_directories = ['/home/user/Documents/']
    backup_directories = ['/home/user/Backup/']
    extensions = ['.ods','.csv','.txt','.pdf','.png','.jpeg','.mp3','.md','.gpg','.ipynb','.jpg','.odt','.mp4','.mov','.xlm','.py','.c','.sh','.PNG','.JPEG','.JPG']
    dir_to_exclude = ['venv','__pycache__','__init__']

    time.sleep(2)
    backupper(to_backup_directories, backup_directories, extensions, dir_to_exclude)

    
if __name__ == '__main__':
    main()
