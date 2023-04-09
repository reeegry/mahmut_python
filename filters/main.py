import os
import picture
 
directory = 'anya_python\others\\filters\imgs'

imgs_paths = []
for entry in os.scandir(directory):
    if entry.is_file():
        imgs_paths.append(entry.path)


help(picture)