import cv2
import numpy as np
import os
from functools import reduce
import random
import shutil
import re

def get_files(path):
    fA = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        fA.extend([os.path.join(path, files) for files in filenames])
    return fA

def blend_imgs(file_list,i,j):
    obj1 = cv2.imread(file_list[0][j])
    obj2 = cv2.imread(file_list[2][i])
    depth1 = cv2.imread(file_list[1][j])
    depth2 = cv2.imread(file_list[3][i])
    m = re.search('RigidBodyHand.(.+?).png',files_list[2][i])
    index = m.group(1)
    depth_diff = (depth1>depth2).astype('uint8')
    cv2.imshow('diff',255*depth_diff)
    # cv2.waitKey()
    final_image = depth_diff*obj1 + (1-depth_diff)*obj2
    cv2.imshow('final image', final_image)
    cv2.imwrite('test_results_combined/'+str(j)+'/final_img_'+index+'.png',final_image)
    # cv2.waitKey()
    # cv2.imwrite('add_img.png',(obj2.astype('float')+depth2.astype('float'))/2)
    print(file_list[2][i],file_list[3][i])
    # cv2.waitKey()

if __name__ == '__main__':

    path = '/home/niranjan/Projects/datasets/HandyPictures_synchronized_2/'
    path_hand = '/home/niranjan/Projects/datasets/test_hand/sim_real_2/test_latest/images'
    path_depth = '/home/niranjan/Projects/datasets/test_hand/sim_real_depth_2/test_latest/images'
    folder_names = ['CylinderColor', 'CylinderDepthMap']#, 'TexturedHand', 'zDepthFullHand']
    hand_folder_names = [path_hand, path_depth]


    files_list = [get_files(path+folder) for folder in folder_names]
    files_list.extend([get_files(folder) for folder in hand_folder_names])
    [folder.sort() for folder in files_list]
    os.mkdir('test_results_combined/'+str(22))
    for i in range(len(files_list[2])):

        blend_imgs(files_list, i,22)


