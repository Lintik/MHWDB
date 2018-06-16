import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowName.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+",s)
j = ""
for i in st:
	i = re.findall(r">[ a-zA-Z\&\#\;0-9]{3,}",i)
	j = ''.join(i)
	j = j[1:]
	print(re.sub(r"\&\#039;", '\'',j))
	w.write(re.sub(r"\&\#039;", '\'',j) + '\n' )
r.close()
w.close()
