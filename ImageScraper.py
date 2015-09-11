#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import ImageDownloader
import urllib2
import re


response = urllib2.urlopen('http://adeleinbeautyland.blogspot.de/')

page = BeautifulSoup(response)
k = page.findAll('img')
l=[]
for h in k:
	m = h['src']

	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', m)
	if urls == []:
		pass
		# print 'this is bad'
	else:
		l.extend(urls)
		# print urls
# print l
print len(l)
for g in l:
	print g


images = ImageDownloader.ImagesDownload()
dirname, imageBookPath = images.filePath('ImageCollection.txt')
images.downloadImages(dirname, l)
