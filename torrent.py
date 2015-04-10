import urllib2
from bs4 import BeautifulSoup

url = urllib2.urlopen("http://torbox.net/?page1")

soup = BeautifulSoup(url)


var = soup.find('title')
var1 = soup.find('td', {"class" : "name"})
#var2 = soup.find("div", {"class" : "current-weather-city"})


print var.text
print var1

#print type (var1.get_text)
#print var1.get_text()
#print ("Current temperature is : %s", %var1)
#print var2.text