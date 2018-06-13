import re

r = open('Gunlance.txt','r')
s = r.read()
w = open('GunlanceElement.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/.+|Fire\)|Water\)|Thunder\)|Ice\)|Dragon\)|Poison\)|Paralysis\)|Sleep\)|Blast\)|Fire|Water|Thunder|Ice|Dragon|Poison|Paralysis|Sleep|Blast",s)
eleset = set(['Fire)','Water)','Thunder)','Ice)','Dragon)','Poison)','Paralysis)','Sleep)','Blast)','Fire','Water','Thunder','Ice','Dragon','Poison','Paralysis','Sleep','Blast'])
j = ""

comb = []
if st[-1] not in eleset:
	st.append("Elementless")
	
for i in zip(st[:-1], st[1:]):
	if i[0] not in eleset:
		comb.append(i)
		

		
print("There is {} bow in the set".format(len(comb)))		
for i in range(len(comb)):
	if comb[i][1] not in eleset:
		comb[i] = [comb[i][0],"Elementless"]
	elif comb[i][1][-1] == ')':
		comb[i] = [comb[i][0],'(' + comb[i][1]]
	print(comb[i])
	
for i in range(len(comb)):
	print(comb[i][1])
	w.write(comb[i][1] + '\n')

print(len(comb))
r.close()
w.close()