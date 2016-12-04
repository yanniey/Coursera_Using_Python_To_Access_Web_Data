# Assignment 2:
# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.
import urllib
# import reg

from bs4 import BeautifulSoup

url = raw_input('Enter url - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

name = []

for i in range(0,count+1):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	if i < count:
		print("Retrieving: ", url)
	else:
		print("Last url: ", url)
		break

	tags = soup('a')
	nameList = []
	pos = 0
	for tag in tags:
		if pos == position -1:
			url = str(tag.get('href',None))
			name = url[41:-5]
			nameList.append(name)
			break
		pos +=1
print nameList[-1]

# Output:
# Enter url - http://python-data.dr-chuck.net/known_by_Kenza.html 
# Enter count: 7
# Enter position: 18
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Kenza.html ')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Rees.html')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Murrin.html')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Gustav.html')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Marieclare.html')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Rimal.html')
# ('Retrieving: ', 'http://python-data.dr-chuck.net/known_by_Lula.html')
# ('Last url: ', 'http://python-data.dr-chuck.net/known_by_Cator.html')
# Cator

