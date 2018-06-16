import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowRaw.txt', 'w+')

st = re.findall(r"<td class=\"text-center align-middle text-muted\">.+",s)
j = ""
for i in st:
	i = re.findall(">[0-9]{2,}",i)
	j = ''.join(i)
	j = j[1:]
	print(j)
	w.write(j + '\n' )
r.close()
w.close()
