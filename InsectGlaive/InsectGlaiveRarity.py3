import re

r = open('InsectGlaive.txt','r')
s = r.read()
w = open('InsectGlaiveRarity.txt', 'w+')

st = re.findall(r"RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write(i[4:] + '\n')
	
print(len(st))
r.close()
w.close()
