# Assignment 2:
# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.
import urllib
from bs4 import BeautifulSoup

# url = raw_input('Enter - ')
# html = urllib.urlopen(url).read()
html = urllib.urlopen("http://python-data.dr-chuck.net/known_by_Fikret.html ").read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
	print tag.get('href',None)