#!/usr/bin/python

import urllib
import os
from urlparse import urlparse
from os.path import splitext,basename
from multiprocessing import Pool,TimeoutError

class ImagesDownload(object):

	def __init__(self, pool_size = 5,timeout = 10,fileName = None):
		self.fileName = fileName
		self._pool_size = pool_size
		self._timeout = timeout
		
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
			textFileContent = textFile.read().splitlines() 
			return textFileContent

	# download images				
	def downloadImages(self, dirName, urlData):
		child_folder = 'pictures'
		# EAFP (see https://docs.python.org/2/glossary.html)
		try:
			os.makedirs(child_folder)
		except:
			pass
		dirName = os.path.join(dirName,child_folder)
		# We can use a process pool to do it in parallel
		process_pool = Pool(processes=self._pool_size)
		results = []

		for ud in urlData:
			# Lets use source images names instead of numbering
			filename = ''.join(splitext(basename(urlparse(ud).path)))
			results.append( process_pool.apply_async( urllib.urlretrieve, [ ud,  os.path.join(dirName,filename) ] ) )

		for result in results:
			try:
				result.get(self._timeout)
			except TimeoutError:
				print("Could not download image due to timeout")
			except Exception as e:
				print(e)


if __name__ == '__main__':
		images = ImagesDownload(fileName = 'ImageCollection.txt')
		dirName, imageBookPath = images.filePath()
		imageBookData = images.readFile(imageBookPath)
		images.downloadImages(dirName, imageBookData)




