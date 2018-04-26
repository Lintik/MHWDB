import re

r = open('GreatSword.txt','r')
s = r.read()
w = open('GreatSwordName.txt', 'a')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}",s)
j = ""
for i in st:
	i = re.findall(">[ a-zA-Z\&\#\;0-9]{3,}",i)
	j = ''.join(i)
	j = j[1:]
	print(j)
	w.write('\n' + j)
r.close()
w.close()
