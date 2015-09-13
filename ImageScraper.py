#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2
import re
import ImageDownloader

class ImageScrapy(ImageDownloader.ImagesDownload):

	def __init__(self, scrap_link):
		ImageDownloader.ImagesDownload.__init__(self)
		self.scrap_url = scrap_link
		self.img_list = []

	# extract all img src from webpage
	def parseImgLinks(self):
		url_response = urllib2.urlopen(self.scrap_url)
		html_parse = BeautifulSoup(url_response)
		img_elements = html_parse.findAll('img')
		for element in img_elements:
			img_src = element['src']
			if not img_src.startswith('http'):
				img_src = '%s%s' % ('http:', img_src)
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', img_src)
			self.img_list.extend(urls)
		return self.img_list

if __name__ == '__main__':

	try:
		scrap_images = ImageScrapy('http://www.people.com/people/jennifer_lawrence/')
		dirName = scrap_images.filePath()
		img_list = scrap_images.parseImgLinks()
		scrap_images.downloadImages(dirName, img_list)

	except:
		print "Error: unable to download"
