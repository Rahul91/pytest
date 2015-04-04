#!/usr/bin/pyhton2.7

import string
import base64
from Tkinter import Tk
from tkFileDialog import askopenfilename
from githubpy import github
#from bs4 import BeautifulSoup


token = '33aa8aec26d79b1843d50385cdea04093b90570f'  #Github auth token for authorisation


root = Tk()
root.withdraw()
root.filename = askopenfilename()
filename = str(root.filename)
filename_rev = filename[::-1]

#print filename_rev
str_file =''
for i in range(30):
	if filename_rev[i] == "/":
		break
	else:
		str_file = str_file + filename_rev[i]



file_name = str_file[::-1]

commit_message = raw_input("Enter your commit Message :")

gh = github.GitHub(access_token=token)

##################################################################

with open(filename) as f:
	file_content = f.read()
	#print file_content

count = len(file_content)
#print count

enc_file = ''
content = ''

'''for j in range(count):
	con = str(file_content[j])
	print con
	content = content + con
	print content
	enc_file = enc_file  + str(base64.b64encode(con))
	#print enc_file
	#print base64.b64decode(enc_file)
'''
##################################################################
print ("----------------------------------------")
print (file_content)
encoded_file =  base64.b64encode(file_content)
#encoded_file = str(enc_file)

#print type(content)
#print encoded_file
decoded_file = base64.b64decode('aW1wb3J0IG9zCg==')
#print decoded_file
#encoded_file = 'aW1wb3J0IG9zCg=='


#encoded_file1 = base64.b64encode('import os')
#encoded_file2 = base64.b64encode('import sys')
#print type(encoded_file1)
#print encoded_file1

'''encoded_file = base64.b64encode('import os\nimport sys')
print encoded_file, type(encoded_file)
print enc_file, type(enc_file)
'''
gh.repos('Rahul91')('pytest')('contents')(file_name).put(path=file_content,message=commit_message,content=encoded_file)
#gh.repos('Rahul91')('pytest')('contents')(file_name).put(path=file_content,message=commit_message,content=encoded_file2)