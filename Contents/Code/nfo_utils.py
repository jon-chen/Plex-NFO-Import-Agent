import glob
import os


def find_nfo_file_in_folder(folder, file_name):
    answer = None
    extension = "nfo"
    file_name_no_ext = os.path.splitext(file_name)[0]
    pattern = "{f}/{n}.{e}".format(f=folder, n=file_name_no_ext, e=extension)
    nfo_files = glob.glob(pattern)
    if len(nfo_files) == 1:
        answer = nfo_files[0]
    
    return answer
    