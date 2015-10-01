import urllib
import os
from os.path import dirname
from multiprocessing import Pool, TimeoutError
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse, urljoin
from image_scraper.output.mixins import ProgressBarMixin
import urllib2


class ImagesDownload(ProgressBarMixin):

	def __init__(self, pool_size=5, timeout=10, fileName=None):
		super(ImagesDownload,self).__init__(name='   Downloading')
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
		failures = 0
		dirName = os.path.join(dirName,child_folder)
		process_pool = Pool(processes=self._pool_size)
		results = []

		for ud in urlData:
			abs_img = os.path.join(dirName,urlparse(ud).path.strip('/'))
			try:
				os.makedirs(dirname(abs_img))
			except:
				pass
			results.append( process_pool.apply_async( urllib.urlretrieve, [ ud,  abs_img ] ) )

		self.initialize_bar(max=len(results))
		for result in results:
			try:
				result.get(self._timeout)
			except Exception:
				failures += 1
			else:
				self.update_bar()

		self.finish_bar()
		if failures: print("   Completed with errors: Downloaded {0}/{1}".format(len(results) - failures, len(results)))
		self.finish_bar()


class ImageScrapy(ImagesDownload):

	def __init__(self, scrap_link, *args,**kwargs):
		super(ImageScrapy,self).__init__(*args,**kwargs)
		self.scrap_url = self.scrape_url_orig = scrap_link
		self.img_list = set() # Use set to avoid duplicates
		self.visited = dict()  # To avoid rescraping the same page

	def parseImgLinks(self,depth=1):
		url_response = None
		try:
			url_response = urllib2.urlopen(self.scrap_url,timeout=self._timeout)
		except Exception as e:
			print("   [ERROR]: Could not open {0}: {1}".format(self.scrap_url,e.reason))
			return self.img_list

		html_parse = BeautifulSoup(url_response)
		unique_images_found = 0
		total_images_found = 0
		self.visited[self.scrap_url] = 1

		for img in html_parse.findAll('img'):
			try:
				abs_url = urljoin(self.scrap_url,img['src']) if urlparse(img['src']).netloc == "" else img['src']
				if abs_url not in self.img_list:
					self.img_list.add(abs_url)
					unique_images_found += 1
				total_images_found += 1
			except:
				pass

		print("   [Found %d images / %d new]: %s" % (total_images_found,unique_images_found,self.scrap_url))
		if depth > 1:
			for a in html_parse.findAll('a'):
				try:
					if (urlparse(a['href']).netloc == "") or (urlparse(self.scrape_url_orig).netloc == urlparse(a['href']).netloc):
						self.scrap_url = urljoin(self.scrape_url_orig,a['href'])
						if self.scrap_url in self.visited: continue
						self.parseImgLinks(depth - 1)
				except:
					pass
		return self.img_list