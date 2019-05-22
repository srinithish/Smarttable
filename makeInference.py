# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:34:35 2019

@author: AI Lab
"""

import cv2 as cv

import os 
import numpy as np
import collections as col
CLS_MAPPING_DICT = {'apple':0,'carrot':1,'cucumber':2}

def initVidCap(camNum=0):
    vidCapHandle = cv.VideoCapture(camNum)
    return vidCapHandle
    
    
def getFrame(vidCapHandle,mirror=False):
    ret_val, img = vidCapHandle.read()
    if mirror: 
        img = cv.flip(img, 1)
    img = cv.resize(img, (300, 300)) 
    
    return img

def showFrame(img,Label):
    
    
    font                   = cv.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (50,50)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2
    
    
    reverseMappingDict = {value:key for key,value in CLS_MAPPING_DICT.items()}
    enumeratedObjs = col.Counter(Label)
    enumeratedObjs ={reverseMappingDict[key]:value for  key,value in enumeratedObjs.items() }
    
    cv.putText(img,str(enumeratedObjs), 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        lineType)
    
    cv.imshow('LiveFeed', img)
    
    pass


def getObjectsArray(imgObject,dirpath = './imageCaptures/images/' ):
    listOfObjArr = []
    listOfLabels = []
    listOfIntLabel = []
    
    ##get objects isolated
    
    for obj in imgObject.objects:
    
        
        croppedImageOfObj = imgArray[obj.ymin:obj.ymax,obj.xmin:obj.xmax]
        resizedImg = cv.resize(croppedImageOfObj,(28,28))
        
        listOfObjArr.append(resizedImg)
        listOfLabels.append(obj.label)
        listOfIntLabel.append(CLS_MAPPING_DICT[obj.label])
        
        
    return listOfObjArr,listOfLabels,listOfIntLabel
    
