import re

r = open('HeavyBowgun.txt','r')
s = r.read()
w = open('HeavyBowgunName.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+",s)
j = ""
for i in st:
	i = re.findall(r">[ a-zA-Z\&\#\;\+0-9]{3,}",i)
	j = ''.join(i)
	j = j[1:]
	j = re.sub(r"\&\#039;", '\'',j)
	j = re.sub(r"\&quot;", '\"',j)
	j = re.sub(r"\&amp;", '&',j)
	print(j)
	w.write(j + '\n' )
	
print(len(st))
r.close()
w.close()
