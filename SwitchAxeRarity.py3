import re

r = open('SwitchAxe.txt','r')
s = r.read()
w = open('SwitchAxeRarity.txt', 'a')

st = re.findall("RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write('\n' + i[4:])
r.close()
w.close()