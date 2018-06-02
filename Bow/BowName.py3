import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowName.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}",s)
j = ""
for i in st:
	i = re.findall(">[ a-zA-Z\&\#\;0-9]{3,}",i)
	j = ''.join(i)
	j = j[1:]
	print(re.sub("\&\#039;", '\'',j));
	w.write(re.sub("\&\#039;", '\'',j) + '\n' )
r.close()
w.close()
