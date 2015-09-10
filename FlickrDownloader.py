#!/usr/bin/python

# import ImageDownloader
import flickr_api

API_KEY =  xxxxxxxxxxx
API_SECRET = yyyyyyyyyyyy

flickr_api.set_keys(api_key = API_KEY, api_secret = API_SECRET)

a = flickr_api.auth.AuthHandler()
perms = "read"
url = a.get_authorization_url(perms)
print url

user = flickr_api.Person.findByEmail('adelabohackova@hotmail.com')
photos = user.getPublicPhotos() # otherwise
# print photos
# print photos.info # total number of photos
p.save('12725043825') # downloading the photo file

