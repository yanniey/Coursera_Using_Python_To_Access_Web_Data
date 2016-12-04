# Using Python to Access Web Data
## University of Michigan, Professor Charles Severance (My favorite Computer Science professor!), Coursera course
### 11/2016 - 

Summary:
To be continued...


---

## Week 4 Parsing HTML with Beautiful Soup

Find hyperlinks on a specific webpage.
```
import urllib
from BeautifulSoup import *

url = raw_input('Enter -')

<!-- html is a string of the entire web page -->
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

<!-- Each tag is a dictionary of HTML attributes  -->
tags = soup('a')

for tag in tag:
print tag.get('href', None)
```

## Week 3 Networked Programs
#### socket library(connecting to web servers on the internet)

```
import sock
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80)

```
#### Urllib
Talk to the web on an application level
```
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
fro line in fhand:
	print line.strip()
```

## Week 2 Regular Expression
use re.search() like find()


#### find()
```
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.find('From:') >=0:
    print line
```

#### re.search()

```
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('From:',line):
    print line
```

#### startswith()

```
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.startswith('From:'):
    print line
```

#### re.search()
```
import re
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^From:',line):
    print line
```

re.search() returns True or False;
re.findall() extracts the matching strings;

#### re.findall()
```
import re
x = "this is the line we are searching for. I have 2 apples and 3 bananas."
y = re.findall('[0-9]+',x)
print(y)
z = re.findall('[AEIOU]+',x)
```

#### Non-greedy matching: 
use ? to help + and *, doesn't need to find the longest string that matches the criteria
returns the shortest list that matches the criteria

```
y = re.findall('^F.+?:',x)
```

#### Starting at the beginning of the line, look for the string "From ", matching non-blank character
^ means "not"

```
'^From .*@([^ ]*)'
```

