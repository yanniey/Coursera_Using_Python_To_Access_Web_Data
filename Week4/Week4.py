import urllib
from bs4 import BeautifulSoup

# url = raw_input('Enter - ')
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_190810.html").read()

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
