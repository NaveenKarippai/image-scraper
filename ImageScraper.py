#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2
import re
import ImageDownloader

scrap_url = 'http://www.people.com/people/jennifer_lawrence/'

url_response = urllib2.urlopen(scrap_url)
html_parse = BeautifulSoup(url_response)
img_elements = html_parse.findAll('img')
img_list = []

for element in img_elements:
	img_src = element['src']
	if not img_src.startswith('http'):
		img_src = '%s%s' % ('http:', img_src)
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', img_src)
	img_list.extend(urls)


images = ImageDownloader.ImagesDownload()
dirname, imageBookPath = images.filePath('ImageCollection.txt')
images.downloadImages(dirname, img_list)
