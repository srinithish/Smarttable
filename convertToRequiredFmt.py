# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:12:00 2019

@author: GELab
"""

import pascal_voc_writer as xmlWriter
import pickle
import os 
import cv2 
import matplotlib.pyplot as plt
import collections as col



CLS_MAPPING_DICT = {'apple':0,'cucumber':2,'carrot':1}


class Item(object):
   def __init__(self, label , xmax, xmin, ymin, ymax):
      self.label = label
      self.xmax = xmax
      self.xmin = xmin
      self.ymin = ymin
      self.ymax = ymax


   def __repr__(self):
      return '{}: xmin: {}, xmax: {}, ymin: {}, ymax: {}'.format(self.label, self.xmin,self.xmax, self.ymin, self.ymax)



class Img(object):
   def __init__(self, name, objects):
      self.name  = name
      self.objects = objects

   def __repr__(self):
      return '{}: {}'.format(self.name,self.objects)


# Writer(path, width, height)






    
def getObjectsArrayAndLables(imgObject,dirpath = './imageCaptures/images/' ):
    listOfObjArr = []
    listOfLabels = []
    listOfIntLabel = []
    
    
    inpfile = dirpath+image.name
    imgArray = cv2.imread(inpfile)
    
    for obj in imgObject.objects:
    
        
        croppedImageOfObj = imgArray[obj.ymin:obj.ymax,obj.xmin:obj.xmax]
        resizedImg = cv2.resize(croppedImageOfObj,(28,28))
        
        listOfObjArr.append(resizedImg)
        listOfLabels.append(obj.label)
        listOfIntLabel.append(CLS_MAPPING_DICT[obj.label])
        
        
    return listOfObjArr,listOfLabels,listOfIntLabel
    






###generate x and y
    
dictOfImgAndObjs = col.defaultdict(list)

AllImgs = pickle.load(open('./Data/AllCucumber.pickle','rb'))

#for image in AllImgs:
#    for obj in image.objects:
#    
#        temp = obj.xmin 
#        obj.xmin = obj.xmax
#        obj.xmax = temp
#        
#        
#pickle.dump(AllImgs, open('./Data/AllCucumber.pickle','wb'))

for image in AllImgs:
    
    
#    imageNameNoExt = os.path.splitext(os.path.basename(image.name))[0]
    try:
        dictOfImgAndObjs['FileNames'].append(image.name)
        dictOfImgAndObjs['X'].extend(getObjectsArrayAndLables(image)[0]) ## all x
        dictOfImgAndObjs['Label'].extend(getObjectsArrayAndLables(image)[1]) ##all labels
        dictOfImgAndObjs['Y'].extend(getObjectsArrayAndLables(image)[2])
    except Exception as ex:
        
        print('exception', ex, 'in ', image.name)

pickle.dump(dictOfImgAndObjs,open('./Data/AllObjectLevelData.pkl','wb'))
