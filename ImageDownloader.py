#!/usr/bin/python

'''
Created on 08/08/2015

@author: karippain

'''

import urllib
import os

# relative file path
dir = os.path.dirname(__file__)						
ImageBook = os.path.join(dir, 'ImageCollection.txt')		


# read text file
with open(ImageBook) as textFile:
    textFileContent = textFile.readlines()					


# download images
for idx, val in enumerate(textFileContent):
    urllib.urlretrieve(val, dir+"/"+str(idx)+".jpg")		    
    
 


