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

match non-blank character
```
'@([^ ]*)'
```