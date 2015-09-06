#!/usr/bin/python

'''
Created on 08/08/2015

@author: karippain
'''

import urllib
import os

# relative file path
def filePath(fileName):
	dirPath = os.path.dirname(__file__)						
	relFilePath = os.path.join(dirPath, fileName)
	return dirPath, relFilePath		

# read file content
def readFile(filePath):
	with open(filePath) as textFile:
	    textFileContent = textFile.readlines()
    	return textFileContent	

# download images				
def downloadImages(dirname, urlData):
	for idx, val in enumerate(urlData):
	    urllib.urlretrieve(val, dirname+"/"+str(idx)+".jpg")		    

try:
	dirname, imageBookPath = filePath('ImageCollection.txt')
	imageBookData = readFile(imageBookPath)
	downloadImages(dirname, imageBookData)    
except:
 	print "Error: unable to download"



