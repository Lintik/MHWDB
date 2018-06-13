import re

r = open('Gunlance.txt','r')
s = r.read()
w = open('GunlanceShelling.txt', 'w+')

st = re.findall("^ +Normal.+|^ +Wide.+|^ +Long.+",s, re.MULTILINE)

st = map(lambda x: s.strip(' '), st)

for i in st:
	print(st)
	
r.close()
w.close()
