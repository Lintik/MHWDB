import re

r = open('DualBlades.txt','r')
s = r.read()
w1 = open('DualBladesSlot1.txt', 'w+')
w2 = open('DualBladesSlot2.txt', 'w+')
w3 = open('DualBladesSlot3.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+|zmdi zmdi-minus|zmdi zmdi-n-[0-9]-square",s, re.MULTILINE)
j = ""

for i in range(len(st)):
	temp = re.findall(r'\d',st[i])
	j = "0" if not temp else temp[0]
	print(st[i])
	if i % 4 == 1:
		w1.write(j + '\n')
	if i % 4 == 2:
		w2.write(j + '\n')
	if i % 4 == 3:
		w3.write(j + '\n')
	
print(len(st)//4)
r.close()
w1.close()
w2.close()
w3.close()