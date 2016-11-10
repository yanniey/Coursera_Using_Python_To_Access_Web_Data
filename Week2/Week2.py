import re
hand = open('regex_sum_190805.txt')
list = []
sum = 0

for line in hand:
	line = line.strip()
	if re.search('[0-9]+', line):
		ListOfNumber = [int(s) for s in re.findall('[0-9]+',line)]
		for number in ListOfNumber:
			sum += int(number)
print(sum)
