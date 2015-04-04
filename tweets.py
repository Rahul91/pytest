#!/usr/bin/python2.7

import urllib2
from bs4 import BeautifulSoup

#username = input("Enter your twitter handle/username : ")
#print username
username = "MishraRahul91"
url2 = urllib2.urlopen("https://twitter.com/%s" %(username))
soup2 = BeautifulSoup(url2)
var3 = soup2.find('title')
print var3.text

#var2 = soup2.find_all('p', {"class" : "ProfileTweet-text js-tweet-text u-dir"})
for items in var2:
	print items.text
	print " "

