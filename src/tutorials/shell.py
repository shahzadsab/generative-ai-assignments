
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    
    if path.exists("textfile.txt"):# make a duplicate of an existing file
        
        src = path.realpath("textfile.txt");# get the path to the file in the current directory
        dst = src + ".bak"# let's make a backup copy by appending "bak" to the name
        shutil.copy(src,dst)# now use the shell to make a copy of the file
        os.rename("textfile.txt", "newfile.txt")# rename the original file
        root_dir,tail = path.split(src)# now put things into a ZIP archive
        shutil.make_archive("archive", "zip", root_dir)
        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip","w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
    main()