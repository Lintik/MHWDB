import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowRarity.txt', 'a')

st = re.findall("RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write('\n' + i[4:])
r.close()
w.close()
