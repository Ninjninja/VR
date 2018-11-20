import cv2
import numpy as np
import os
from functools import reduce
import random
import shutil


fA = []
fB = []
fC = []
fD = []
pathA = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/RigidBodyHand/'
pathB = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/TexturedHand/'
pathC = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/zDepthFullHand/'
pathD = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/zDepthRigidBody/'

path1 = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/sim_real_2/testA/'
path2 = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/sim_real_2/testB/'
path3 = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/sim_real_depth_2/testA/'
path4 = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/sim_real_depth_2/testB/'
os.mkdir(path1)
os.mkdir(path2)
os.mkdir(path3)
os.mkdir(path4)
for (dirpath, dirnames, filenames) in os.walk(pathA):
    fA.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk(pathB):
    fB.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk(pathC):
    fC.extend(filenames)
for (dirpath, dirnames, filenames) in os.walk(pathD):
    fD.extend(filenames)

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
fC.sort()
fD.sort()
print(fA)
print(fB)
filesA, filesB, index = get_n_random_files(fA, fB, int(len(fA)/5))
filesC, filesD, index = get_n_random_files(fC, fD, int(len(fA)/5), index)

print(filesA)
print(filesB)
print(filesC)
print(filesD)
move_image(filesA,pathA,path1)
move_image(filesB,pathB,path2)
move_image(filesC,pathC,path3)
move_image(filesD,pathD,path4)

# get_label_img(f)