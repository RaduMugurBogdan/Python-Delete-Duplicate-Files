from PathTest import *
def run():
    while True:
        input_path=input("Introduceti path-ul folderului:")
        if test_folder_path(input_path)==True:
            perform_search(input_path)



if __name__=='__main__':
    run()


