#!/usr/bin/python

'''
Created on 08/08/2015

@author: karippain

'''
import urllib,os

"""relative file path"""
dir = os.path.dirname(__file__)						
ImageBook = os.path.join(dir, 'ImageCollection.txt')		#relative path text file 


"""read text file"""
with open(ImageBook) as textFile:
    textFileContent = textFile.readlines()					#text file data read 


"""download images"""
for idx,val in enumerate(textFileContent):
    urllib.urlretrieve(val, dir+"/"+str(idx)+".jpg")		#write url
    
    
 


