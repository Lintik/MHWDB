import re

r = open('LightBowgun.txt','r')
s = r.read()
w = open('LightBowgunRaw.txt', 'a')

st = re.findall("<td class=\"text-center align-middle text-muted\">[\da-z/<>]{3,}",s)
j = ""
for i in st:
	i = re.findall(">[0-9]{2,}",i)
	j = ''.join(i)
	j = j[1:]
	print(j)
	w.write('\n' + j)

print(len(st))
r.close()
w.close()
