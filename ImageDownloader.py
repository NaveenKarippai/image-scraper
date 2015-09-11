#!/usr/bin/python

'''
created on 08/08/2015

@author: Naveen Karippai
'''

import urllib
import os

class ImagesDownload(object):
		
	# relative file path
	def filePath(self, fileName):
		dirPath = os.path.dirname(__file__)						
		relFilePath = os.path.join(dirPath, fileName)
		return dirPath, relFilePath		

	# read file content
	def readFile(self, filePath):
		with open(filePath) as textFile:
		    textFileContent = textFile.readlines()
	    	return textFileContent	

	# download images				
	def downloadImages(self, dirname, urlData):
		if not os.path.exists('pictures'): os.makedirs('pictures')
		dirname = dirname+'/pictures'
		for idx, val in enumerate(urlData):
			urllib.urlretrieve(val, dirname+"/"+str(idx)+".jpg")		    

if __name__ == '__main__':

	try:
		images = ImagesDownload()
		dirname, imageBookPath = images.filePath('ImageCollection.txt')
		imageBookData = images.readFile(imageBookPath)
		images.downloadImages(dirname, imageBookData)

	except:
		print "Error: unable to download"




