import cv2
import os
import numpy as np
from blend_images import get_files
import re
path = '/home/niranjan/Projects/VR/test_results_combined/22'

f = get_files(path)
f.sort()
os.mkdir(path + '/combined/')
for i in range(0,len(f),2):
    img1 = cv2.imread(f[i])
    img2 = cv2.imread(f[i+1])
    m = re.search('final_img_.(.+?)_input',f[i])
    index = m.group(1)
    cv2.imwrite(path+'/combined/'+index+'.png',np.hstack((img1,img2)))
    # cv2.imshow('combined',np.hstack((img1,img2)))
    # cv2.waitKey()
print(f)