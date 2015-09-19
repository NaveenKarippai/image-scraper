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

	def test_instance(self):
		self.assertIsInstance(self.images, ImageDownloader.ImagesDownload, 'ImagesDownload class instantiation fail')   

	# def test_filePath(self):
	# 	k = self.images.filePath()
	# 	print k
	# 	self.assertEqual(str(m), 'str', 'fail')

	def tearDown(self):
		pass

if __name__ == '__main__':
    unittest.main()