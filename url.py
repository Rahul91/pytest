import urllib2

page = urllib2.urlopen("https://www.google.co.in")
text = page.read().decode("utf8")

print(text)
