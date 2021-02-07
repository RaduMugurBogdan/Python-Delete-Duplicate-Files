import os
import hashlib

def search_file(base_path):
    files_set=set()


def file_hash_value(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def tree_search(path,dup_set):
    dir_content=os.listdir(path)
    for path_value in dir_content:
        new_path=os.path.join(path,path_value)
        if os.path.isfile(new_path)==True:
            hash_value=file_hash_value(new_path)
            if (path_value,hash_value) in dup_set:
                list(dup_set[(path_value,hash_value)]).append(new_path)
            else:
                dup_set[(path_value, hash_value)]=[new_path]
        elif os.path.isdir(new_path)==True:
            tree_search(new_path,dup_set)

dup_set=dict()
tree_search("E:\\Documente",dup_set)
#print(dup_set)
for key in dup_set.keys():
    print(key)
    #
    # if len(dup_set[key])>1:
    #     print(key)
