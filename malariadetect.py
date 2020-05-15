import cv2,os
import numpy as np 
import csv
import glob

label = 'Parasitized'
dir_list = glob.glob('E://cell_images/train/'+label+'/*.png')
fl= open('csv/mdata.csv','a')

for image_path in dir_list:

    im = cv2.imread(image_path)
    #Applying a blur mask on each image
    im = cv2.GaussianBlur(im, (5,5), 2)
    #converting into gray image
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #if pixel value is greater than threshold value get it
    ret, thresh = cv2.threshold(im_gray,127,255,0)
    #now obtaining the contours from those thresholds ,contours means borders
    contours,_ = cv2.findContours(thresh,1,2)
    fl.write(label)
    fl.write(',')
    for i in range(5):
        try:
            area = cv2.contourArea(contours[i])
            fl.write(str(area))
        except:
            fl.write('0')
        fl.write(',')
    fl.write('\n')
