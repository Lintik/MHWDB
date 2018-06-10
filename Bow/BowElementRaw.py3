import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowElementRaw.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/.+|^ +\d+$|^ +\(\d+$",s, re.MULTILINE)
j = ""

comb = []
for i in range(len(st)):
	st[i] = st[i].strip(' (')
	print(st[i])
	
for i in zip(st[:-1],st[1:]):
	if not i[0].isdigit():
		if i[1].isdigit():
			comb.append(i)
		else:
			comb.append([i[0], "0"])

for i in comb:
	w.write(i[1] + '\n')
r.close()
w.close()