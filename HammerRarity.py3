import re

r = open('Hammer.txt','r')
s = r.read()
w = open('HammerRarity.txt', 'a')

st = re.findall("RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write('\n' + i[4:])
r.close()
w.close()