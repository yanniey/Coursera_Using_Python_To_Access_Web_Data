# Using Python to Access Web Data
### University of Michigan, Professor Charles Severance (My favorite Computer Science professor!), Coursera course
### 11/2016 - 12/2016

Summary:
Scrape, parse and read web data using web APIS. This is part 5 of the Coursera specialization "Python for Everybody".

Libraries learned:

* Urllib 
* regular expression (regex)
* XML (xml.etree.ElementTree)
* JSON (json)
* Google maps GEOJSON API
* Twitter API

Feedback:
Pretty good course for someone who's new to Python and web scraping. 

The assignments are quite easy to complete, I think it would be better if they had been more challenging.

![Course Completion Screenshot](https://github.com/yanniey/Coursera_Using_Python_To_Access_Web_Data/blob/master/Course%20completion%20screenshot.png?raw=true)

## Week6 JSON in Python
No attribute, only lists and dictionaries

```
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]
```

Another example:

```
import json

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']


```

For Twitter, also check twtest.py and twurl.py under Week 4's folder.

---
## Week 5 XML in Python
Use xml.etree.ElementTree library

Filename: xml1.py

```
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
<!-- use get() for the attribute -->

```

Filename: xml2.py

```
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")


```
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

---

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

---

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

