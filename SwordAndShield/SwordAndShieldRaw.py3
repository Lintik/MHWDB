import re

r = open('SwordAndShield.txt','r')
s = r.read()
w = open('SwordAndShieldRaw.txt', 'w+')

st = re.findall(r"<td class=\"text-center align-middle text-muted\">[\da-z/<>]{3,}",s)
j = ""
for i in st:
	i = re.findall(r">[0-9]{2,}",i)
	j = ''.join(i)
	j = j[1:]
	print(j)
	w.write(j + '\n')

print(len(st))
r.close()
w.close()
