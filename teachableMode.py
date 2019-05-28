# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:02:23 2019

@author: GELab
"""

import pickle
import os 
import cv2 as cv 
import matplotlib.pyplot as plt
import collections as col
from ImgObjClass import Item,Img
import DatabaseOps
import captureImages
import time 
from datetime import datetime
import re
import label
import glob

camOps = captureImages.camOpertations()

def capture_save_by_frame(saveFolder,Label,capFrames = 200,camNum=0):
    
    
    print('Make sure to remove all other objects except the one you want to train')
    
    vidCap = cv.VideoCapture(camNum) ## from camera
    
    time.sleep(5)
    
    createdFileNameList = []
    
    for frameNum in range(capFrames):
        
        
        
        print('3 seconds for a picture, randomly place the object',frameNum)
        time.sleep(3)
        ret_val, img = vidCap.read()
        print("picture taken")
        
        img = cv.flip(img, 1)
#            img = cv.resize(img, (300, 300)) 
#        uniqueID = int(time.mktime(datetime.now().timetuple()))
        uniqueID = re.sub('(?:\W+)','_',str(datetime.now()))
        fileName = Label + "_" + uniqueID+'.jpg'
        
        createdFileNameList.append(os.path.join(saveFolder,fileName))
        
        
        
        
        cv.imwrite(os.path.join(saveFolder,fileName),img)
        

    cv.destroyAllWindows()  
    
    print('all done')
    
    return createdFileNameList
    

if __name__ == '__main__':

    Label = 'Potato' ### to be passed from cmd line args
    saveFolder = './imageCaptures/images'
    fileListCreated = capture_save_by_frame(saveFolder = saveFolder,
                                            Label = Label,capFrames = 30,camNum=1)
    
    
    
    
#    fileListCreated = [saveFolder+'/'+fileName for fileName in fileListCreated]
    
#    fileListCreated = glob.glob('./imageCaptures/images/Potato*')
    
    imgObjList = label.label_imgs(fileListCreated, Label)
    
    ##db update
    DatabaseOps.dbInsertWrapper(imgObjList)
    
    







