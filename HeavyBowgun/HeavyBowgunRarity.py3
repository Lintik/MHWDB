import re

r = open('HeavyBowgun.txt','r')
s = r.read()
w = open('HeavyBowgunRarity.txt', 'w+')

st = re.findall(r"RARE[\d]",s)
for i in st:
	print(i[4:])
	w.write(i[4:] + '\n')
	
print(len(st))
r.close()
w.close()
