import cv2
import numpy as np
import os
from functools import reduce
import random
import shutil
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", dest="path", help="Link to data folder")
# parser.add_argument("-f", "--folder2", dest="pathB", help="Link to test folder")

args = parser.parse_args()
# myFile = args.myFile
path = args.path
pathA = os.path.join(path,'train_A/')
pathB = os.path.join(path,'train_B/')
path1 = os.path.join(path,'test_A/')
path2 = os.path.join(path,'test_B/')

fA = []
fB = []

# pathA = '/home/niranjan/Projects/datasets/Elie_room_data/trainA/'
# pathB = '/home/niranjan/Projects/datasets/Elie_room_data/trainB/'

# path1 = '/home/niranjan/Projects/datasets/Elie_room_data/testA/'
# path2 = '/home/niranjan/Projects/datasets/Elie_room_data/testB/'
os.mkdir(path1)
os.mkdir(path2)
for (dirpath, dirnames, filenames) in os.walk(pathA):
    fA.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk(pathB):
    fB.extend(filenames)


def get_label_img(f):
    val = unique_values(f)
    for image_name in f:
        print(image_name + ' ...done')
        img = cv2.imread(path1 + image_name)
        img = np.sum(img, 2)
        count = 0
        for i in val:
            ind = img == i
            img[ind] = count
            count += 1
        cv2.imwrite(path2 + image_name, img)


def unique_values(f):
    val = []
    for image_name in f:
        img = cv2.imread(path1 + image_name)
        img = np.sum(img, 2)
        val.append(np.unique(img).tolist())
    return np.unique(np.array(reduce(lambda x, y: x + y, val)))

def move_image(f,path,path_):
    for image_name in f:
        shutil.move(path + image_name, path_ + image_name)
        # img = cv2.imread(path + image_name)
        # cv2.imwrite(path_ + image_name, img)

def get_n_random_files(fA,fB,n, files=None):
    if files is None:
        files = np.random.choice(len(fA), n, replace=False)
    print(files.shape)
    selectedA = [fA[i] for i in files]
    selectedB = [fB[i] for i in files]

    return selectedA, selectedB, files
fA.sort()
fB.sort()
print(fA)
print(fB)
filesA, filesB, index = get_n_random_files(fA, fB, int(len(fA)/5))

print(filesA)
print(filesB)

move_image(filesA,pathA,path1)
move_image(filesB,pathB,path2)


# get_label_img(f)