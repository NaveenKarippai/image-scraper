#!/usr/bin/python

import os
import sys

# system path
fileName = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])   # directory of directory of file
sys.path.append(os.path.dirname(os.path.dirname(fileName)))

import ImageDownloader
import unittest

class TestImageDownloader(unittest.TestCase, ImageDownloader.ImagesDownload):

	def setUp(self):
		self.images = ImageDownloader.ImagesDownload(fileName = None)
		self.mock_data = ['a.png', 'b.jpg', 'c.jpg']

	def test_instance(self):
		self.assertIsInstance(self.images, ImageDownloader.ImagesDownload, 'class ImagesDownload instantiation fail')   

	def test_filePath(self):
		path = self.images.filePath()
		self.assertIsInstance(path, str, 'class ImagesDownload method filePath fail')

	def test_readFile(self):
		fileData = self.images.readFile(self.images.filePath()+'/tests/mock_test/mock_image_directory.txt')
		self.assertItemsEqual(fileData, self.mock_data,'class ImagesDownload method readFile fail')

	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()