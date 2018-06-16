import re

r = open('Bow.txt','r')
s = r.read()
w1 = open('BowArrowCls.txt', 'w+')
w2 = open('BowArrowPow.txt', 'w+')
w3 = open('BowArrowPar.txt', 'w+')
w4 = open('BowArrowPoi.txt', 'w+')
w5 = open('BowArrowSle.txt', 'w+')
w6 = open('BowArrowBla.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+|coating-1\">Cls|text-muted\">Cls|coating-2\">Pow|text-muted\">Pow|coating-3\">Par|text-muted\">Par|coating-4\">Poi|text-muted\">Poi|coating-5\">Sle|text-muted\">Sle|coating-6\">Bla|text-muted\">Bla",s)
j = ""

comb = []

for i in range(len(st)):
	print(st[i])
	if "coating" in st[i]:
		st[i] = "1"
	elif "text-muted" in st[i]:
		st[i] = "0"
	
for i in range(len(st)):
	if i % 7 == 0:
		continue
	elif i % 7 == 1:
		w1.write(str(st[i]) + '\n')
	elif i % 7 == 2:
		w2.write(str(st[i]) + '\n')	
	elif i % 7 == 3:
		w3.write(str(st[i]) + '\n')
	elif i % 7 == 4:
		w4.write(str(st[i]) + '\n')
	elif i % 7 == 5:
		w5.write(str(st[i]) + '\n')
	else:
		w6.write(str(st[i]) + '\n')

w1.close()
w2.close()
w3.close()
w4.close()
w5.close()
w6.close()

	
	
