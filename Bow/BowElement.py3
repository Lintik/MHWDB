import re

r = open('Bow.txt','r')
s = r.read()
w = open('BowElement.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}|Fire|Water|Thunder|Ice|Dragon|Poison|Paralysis|Sleep|Blast",s)
eleset = set(['Fire','Water','Thunder','Ice','Dragon','Poison','Paralysis','Sleep','Blast'])
j = ""

comb = []
for i in zip(st[:-1], st[1:]):
	if i[0] not in eleset:
		comb.append(i)
		
print("There is {} bow in the set".format(len(comb)))		
for i in range(len(comb)):
	if comb[i][1] not in eleset:
		comb[i][1] = "Elementless"
r.close()
w.close()