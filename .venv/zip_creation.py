import zipfile
import pathlib

def make_archieve(filepaths,dest):
    dest_path=pathlib.Path(dest,"compressed.zip")
    with zipfile.ZipFile(dest_path,"w") as archive:
        
         for filepath in filepaths:
             filepath = pathlib.Path(filepath)
             archive.write(filepath,arcname=filepath.name)
if __name__=="__main__":
    make_archieve(filepaths=["bonus.py","bonus1,py"],dest="dict")

             