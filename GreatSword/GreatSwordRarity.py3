import re

r = open('GreatSword.txt','r')
s = r.read()
w = open('GreatSwordRarity.txt', 'a')

st = re.findall("RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write('\n' + i[4:])
r.close()
w.close()
