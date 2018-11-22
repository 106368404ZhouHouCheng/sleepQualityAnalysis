'''
editor: Jones
date: 2018/10/03
content: image rename
'''

from PIL import Image
import cv2
import os


path_name = '/home/jones/demo/video_split_img/sleep_to_left' #old image file name address

i = 0
# dirs = os.listdir(path_name)

for item in os.listdir(path_name):
    new_item = 'sleep_to_left.' + str(i) + '.jpg'  # old image all .bmp format
    os.rename(os.path.join(path_name, item), os.path.join(path_name, new_item))
    file_path = os.path.join(path_name, new_item)
    # print file_path
    out_path = os.path.splitext((file_path))[0] + '.jpg'
    print out_path
    Image.open(file_path).save(out_path)
    # os.remove(os.path.join(path_name, new_item))
    i+=1

print("finish rename")

# import numpy as np

# image = cv2.imread('face_up/0.jpg')
# height = np.size(image, 0)
# width = np.size(image, 1)
# print height, width



