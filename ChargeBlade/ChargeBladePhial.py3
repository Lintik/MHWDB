import re

r = open('ChargeBlade.txt','r')
s = r.read()
w = open('ChargeBladePhial.txt', 'w+')

st = re.findall(r"^ +Power Element Phial|^ +Impact Phial", s, re.MULTILINE)

st = list(map(lambda x: x.strip(' '), st))

for i in st:
	print(i)
	w.write(i + '\n')

print(len(st))
w.close()
r.close()