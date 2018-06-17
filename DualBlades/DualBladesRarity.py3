import re

r = open('DualBlades.txt','r')
s = r.read()
w = open('DualBladesRarity.txt', 'w+')

st = re.findall(r"RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write('\n' + i[4:])
	
print(len(st))
r.close()
w.close()
