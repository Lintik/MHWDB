import re

r = open('Gunlance.txt','r')
s = r.read()
w = open('GunlanceShelling.txt', 'w+')

st = re.findall("^ +Normal +Lv[0-9]$|^ +Wide +Lv[0-9]$|^ +Long +Lv[0-9]$",s, re.MULTILINE)
j = []

j = list(map(lambda x: re.sub(' +',' ', x).strip(), st))
for i in j:
	print(i)
	w.write(i + '\n')
print(len(st))
	
r.close()
w.close()
