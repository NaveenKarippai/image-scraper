#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2
import urlparse
import re
import ImageDownloader

class ImageScrapy(ImageDownloader.ImagesDownload):

	def __init__(self, scrap_link, *args,**kwargs):
		super(ImageScrapy,self).__init__(*args,**kwargs)
		self.scrap_url = scrap_link
		self.img_list = set() # Use set to avoid duplicates 

	# extract all img src from webpage
	def parseImgLinks(self):
		url_response = urllib2.urlopen(self.scrap_url)
		html_parse = BeautifulSoup(url_response)

		for src in [ e['src'] for e in html_parse.findAll('img') if not e['src'].startswith('//') ]:
			abs_url = src if urlparse.urlparse(src).netloc else urlparse.urljoin(self.scrap_url,src)
			self.img_list.add(abs_url)
		return self.img_list

if __name__ == '__main__':
		scrap_images = ImageScrapy('http://www.people.com/people/jennifer_lawrence/')
		dirName = scrap_images.filePath()
		img_list = scrap_images.parseImgLinks()
		scrap_images.downloadImages(dirName, img_list)
