from glob import glob
from shutil import copy
import os

CURRENT_PATH = __file__[:__file__.rfind("/")]


def mp_threes_in_dir(dir):
    search_query = dir + "/*.mp3"
    return glob(search_query)


def mp_threes_in_dir_tree(root_dir):
    mp_threes = []

    for dirName, subdirList, fileList in os.walk(root_dir):
        mp_threes_in_curr_dir = mp_threes_in_dir(dirName)

        for mp_three in mp_threes_in_curr_dir:
            mp_threes.append(mp_three)

    return mp_threes


def copy_to_collection(path_to_file):
    path_to_collection = CURRENT_PATH + "/collected_mp3s"
    copy(src=path_to_file,
         dst=path_to_collection)


if __name__ == "__main__":
    all_mp_three_paths = mp_threes_in_dir_tree(CURRENT_PATH + "/test_dir")

    # Collect paths to file, nothing is moved
    '''file = open("all_mp3_paths", mode="a+")
    for path in all_mp_three_paths:
        file.write(path + "\n")'''

    # Copy all found files to the collection
    '''for mp_three_path in all_mp_three_paths:
        copy_to_collection(mp_three_path)'''
