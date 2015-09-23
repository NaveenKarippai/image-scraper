import urllib
import os
from os.path import splitext,basename
from multiprocessing import Pool,TimeoutError
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse,urljoin
import urllib2

class ImagesDownload(object):

	def __init__(self, pool_size = 5,timeout = 10,fileName = None):
		self.fileName = fileName
		self._pool_size = pool_size
		self._timeout = timeout

	# relative file path
	def filePath(self):
		dirPath = os.curdir
		if self.fileName != None:
			relFilePath = os.path.abspath(self.fileName)
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


class ImageScrapy(ImagesDownload):

	def __init__(self, scrap_link, *args,**kwargs):
		super(ImageScrapy,self).__init__(*args,**kwargs)
		self.scrap_url = scrap_link
		self.img_list = set() # Use set to avoid duplicates

	# extract all img src from webpage
	def parseImgLinks(self):
		url_response = urllib2.urlopen(self.scrap_url)
		html_parse = BeautifulSoup(url_response)

		for src in [ e['src'] for e in html_parse.findAll('img') if not e['src'].startswith('//') ]:
			abs_url = src if urlparse(src).netloc else urljoin(self.scrap_url,src)
			self.img_list.add(abs_url)
		return self.img_list
