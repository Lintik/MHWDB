import re

r = open('SwitchAxe.txt','r')
s = r.read()
w = open('SwitchAxeElementRaw.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+|^ +\d+$|^ +\(\d+$",s, re.MULTILINE)
j = ""

comb = []
for i in range(len(st)):
	st[i] = st[i].strip(' (')
	print(st[i])

if not st[-1].isdigit():
	st.append('0')
	
for i in zip(st[:-1],st[1:]):
	if not i[0].isdigit():
		if i[1].isdigit():
			comb.append(i)
		else:
			comb.append([i[0], "0"])

x = open('SwitchAxeElement.txt','r')
y = x.read()

z = y.split()
print(z)
print(len(z))
for i in range(len(z)):
	if z[i] == "Elementless":
		comb[i] = [comb[i][0],'0']

for i in comb:
	w.write(i[1] + '\n')
r.close()
w.close()