import sys
import cv2
import numpy as np
import os

def format_path(path):
    if(path[-1:] == '/'):
        path = path[:-1]
    return path

def preprocess(path, path_to_save, thresh_amt):
    path = format_path(path)
    path_to_save = format_path(path_to_save)
    pic_names = os.listdir(path)
    pics = ['{}/{}'.format(path,pic_name) for pic_name in pic_names]
    pics = ['test_pic2.jpg']
    for pic,pic_name in zip(pics,pic_names):
        img = cv2.imread(pic, 0)
        ret, threshed = cv2.threshold(img,thresh_amt,255,cv2.THRESH_BINARY)
        ind = pic_name.index('.')
        resized = cv2.resize(threshed, (720,720))
        cv2.imwrite('{}/{}.png'.format(path_to_save,pic_name[:ind]), resized)

if(__name__ == '__main__'):
    path = sys.argv[1]
    path_to_save = sys.argv[2]
    thresh_amt = 50
    preprocess(path, path_to_save, thresh_amt)
