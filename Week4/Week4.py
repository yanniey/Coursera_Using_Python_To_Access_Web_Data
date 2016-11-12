# Assignment 1:
# In this assignment you will write a Python program to use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
sum = 0
list = []

tags = soup('span')
for tag in tags:
	list.append([int(number) for number in tag.contents])

new_list = [item for sublist in list for item in sublist]
for x in new_list:
	sum+=x

print(sum)
