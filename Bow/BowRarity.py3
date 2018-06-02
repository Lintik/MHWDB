import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowRarity.txt', 'w+')

st = re.findall("RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write(i[4:] + '\n' )
r.close()
w.close()
