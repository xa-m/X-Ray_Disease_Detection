# get the current path
import os
import shutil
current_path = os.getcwd()


# copy all of the images from multiple directories into one directory

def copy_images():
    """
    copy images from /data/images_001/images to /data/all_images

    examples: 
    /data/images_001/images/ -> /data/all_images
    /data/images_002/images/ -> /data/all_images
    /data/images_003/images/ -> /data/all_images
    """

    # get the current path
    current_path = os.getcwd()

    # get the list of directories
    dir_list = os.listdir(current_path)

    # loop through the directories
    for dir in dir_list:
        # get the full path
        full_path = os.path.join(current_path, dir)
        # check if the directory exists
        if os.path.isdir(full_path):
            # get the list of files
            file_list = os.listdir(full_path)
            # loop through the files
            for file in file_list:
                # get the full path
                full_file_path = os.path.join(full_path, file)
                # check if the file is a jpeg
                if os.path.isfile(full_file_path) and file.endswith('.png'):
                    # copy the file to the new directory
                    shutil.copy(full_file_path, '/data/all_images')


copy_images()