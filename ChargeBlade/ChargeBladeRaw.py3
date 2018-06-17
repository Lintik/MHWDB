import re

r = open('ChargeBlade.txt','r')
s = r.read()
w = open('ChargeBladeRaw.txt', 'w+')

st = re.findall(r"<td class=\"text-center align-middle text-muted\">[\da-z/<>]{3,}",s)
j = ""
for i in st:
	i = re.findall(r">[0-9]{2,}",i)
	j = ''.join(i)
	j = j[1:]
	print(j)
	w.write('\n' + j)
r.close()
w.close()
