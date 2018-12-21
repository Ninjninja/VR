import pickle as pkl
import argparse
import csv
import re
from get_coordinates import FetchFrame2

def str2coordinates(self, input):
   matchObj = re.match(r'\((.*?), (.*?), (.*?)\)', input, re.M | re.I)
   if matchObj:
      # print(matchObj.group(1))
      # print(matchObj.group(2))
      # print(matchObj.group(3))
      return (float(matchObj.group(1)), float(matchObj.group(2)), float(matchObj.group(3)))

   else:
      print('no match')


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", dest="path", help="Link to data folder",default='/home/niranjan/Projects/datasets/dataCollection1/joints.pkl')
# parser.add_argument("-f", "--folder2", dest="pathB", help="Link to test folder")

args = parser.parse_args()
# myFile = args.myFile
path = args.path

# file = open(path,'rb')
# frames = pkl.load(file)
# file.close()
#
# frame = frames[0]
myFile = open('csvexample3.csv', 'w')

frame = FetchFrame2(path)
tframe = iter(frame)
count = 1
data = [['_Distal_next', '_Intermediate_next', '_Proximal_next', '_Metacarpal_next', '_Metacarpal_prev']]
# data = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky','elbow','wrist']
# data1 = next(frame)
data.extend(next(frame))
# for points in data[:-2]:
#    points = [list(data) for data in points]
#    for i in range(len(points) - 1):
#       print(points[i])
myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]
with myFile:
   writer = csv.writer(myFile)
   writer.writerows(data)
