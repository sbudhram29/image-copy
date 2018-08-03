'''
copy carryover images from images folder to carryover
'''
import re
import os
import shutil
# directory you wish to copy all the files to.
dst = '/Users/sbudhram/code/python/carryover/carryover'
src = '/Users/sbudhram/code/python/carryover/images'


with open("file.txt", 'r') as fread:
    for line in fread:
        line = line.rstrip()
        line += ".jpg"
        # concatenates destination and source path with subdirectory path and copies file over.
        dst_file_path = "%s/%s" % (dst, line)
        (root, file_name) = os.path.splitext(dst_file_path)

        src_file_path = os.path.normcase("%s/%s" % (src, line))
        try:
            shutil.copyfile(src_file_path, dst_file_path)
            print(f"{dst}/{line}")
        except FileNotFoundError:
            print(f"{line} not found")
