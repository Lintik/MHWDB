import re

r = open('ChargeBlade.txt','r')
s = r.read()
w = open('ChargeBladeRarity.txt', 'w+')

st = re.findall(r"RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write(i[4:] + '\n')
r.close()
w.close()
