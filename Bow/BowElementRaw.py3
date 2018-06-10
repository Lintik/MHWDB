import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowElementRaw.txt', 'w+')

st = re.findall(r"\b\d{3}",s)
j = ""

comb = []
for i in range(len(st)):
	print(st[i])
	
