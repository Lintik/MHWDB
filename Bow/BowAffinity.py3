import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowAffinity.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}|\+[0-9]{2}\%|\-[0-9]{2}\%",s)
j = ""

comb = []
for i in range(len(st)):
	if st[i][-1] == '%':
		temp = re.findall(r'-\d+|\d+', st[i])
		st[i] = temp[0]
		
for i in zip(st[:-1], st[1:]):
	if i[0].isdigit():
		continue
	else:
		comb.append(i)
	
for i in range(len(comb)):
	if comb[i][1].isdigit():
		comb[i] = [comb[i][0], '0']
	print(comb[i])
		

r.close()
w.close()