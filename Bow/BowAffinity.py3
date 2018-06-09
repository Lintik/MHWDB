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
	if re.match('[-]?\d+', i[0]):
		print(i)
	else:
		if '<' in i[1]:
			comb.append([i[0], '0'])
		else:
			comb.append(i)
		
for i in comb:
	print(i[1])
	w.write(i[1] + '\n')
r.close()
w.close()