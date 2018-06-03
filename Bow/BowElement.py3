import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowElement.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}|Fire|Water|Thunder|Ice|Dragon|Poison|Paralysis|Sleep|Blast",s)
eleset = set(['Fire','Water','Thunder','Ice','Dragon','Poison','Paralysis','Sleep','Blast'])
j = ""
for i in st:
	print(i)
r.close()
w.close()