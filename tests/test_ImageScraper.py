import unittest
import httpretty
import os
from ImageScraper import ImageScrapy

# Absolute path to http_resources dir.
HTTP_RESOURCES_PATH = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'http_resources' )

class ImageScrapyTest(unittest.TestCase):

    def setUp(self):
        self._resources = [ { 'site': 'https://help.github.com/articles/github-terms-of-service/',
                              'file': 'github1.html',
                              'result': set(['https://help.github.com/assets/images/site/invertocat.png'] ) },
                            { 'site': 'https://github.com/contact',
                              'file': 'github2.html',
                              'result': set(['https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif',
                                             'https://assets-cdn.github.com/images/modules/contact/heartocat.png',
                                             'https://avatars1.githubusercontent.com/u/508444?v=3&s=40']) },
                            { 'site': 'https://www.google.co.il',
                              'file': 'google1.html',
                              'result': set(['https://www.google.co.il/images/nav_logo231.png',
                                             'data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==']) }]

    def test_instantiation(self):
        self.assertIsInstance( ImageScrapy( self._resources[0]['site'] ), ImageScrapy, "Test ImageScrapy instance" )

    def test_parseImgLinks(self):
        httpretty.enable()
        resources_dir = os.path.dirname(os.path.abspath(__file__))
        for resource in self._resources:
            with open( os.path.join(HTTP_RESOURCES_PATH,resource['file']) ) as html:
                httpretty.register_uri(httpretty.GET, resource['site'],body=html.read())
                imgs = ImageScrapy(resource['site'])
                links = imgs.parseImgLinks()
                self.assertSetEqual( links, resource['result'], "Test HTML page link parsing")

        httpretty.disable()
        httpretty.reset()