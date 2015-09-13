#!/usr/bin/python

import urllib
import os

class ImagesDownload(object):

	def __init__(self, fileName = None):
		self.fileName = fileName
		
	# relative file path
	def filePath(self):
		dirPath = os.path.dirname(__file__)	
		if self.fileName != None:					
			relFilePath = os.path.join(dirPath, self.fileName)
			return dirPath, relFilePath		
		else:
			return dirPath

	# read file content
	def readFile(self, filePath):
		with open(filePath) as textFile:
		    textFileContent = textFile.readlines()
	    	return textFileContent	

	# download images				
	def downloadImages(self, dirName, urlData):
		if not os.path.exists('pictures'): os.makedirs('pictures')
		dirName = dirName+'/pictures'
		for idx, val in enumerate(urlData):
			urllib.urlretrieve(val, dirName+"/"+str(idx)+".jpg")		    

if __name__ == '__main__':

	try:
		images = ImagesDownload('ImageCollection.txt')
		dirName, imageBookPath = images.filePath()
		imageBookData = images.readFile(imageBookPath)
		images.downloadImages(dirName, imageBookData)

	except:
		print "Error: unable to download"




