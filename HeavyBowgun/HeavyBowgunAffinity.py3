import re

r = open('HeavyBowgun.txt','r')
s = r.read()
w = open('HeavyBowgunAffinity.txt', 'w+')

st = re.findall(r"<a href=\"https://mhworld.kiranico.com/weapon/.+|\+[0-9]{2}\%|\-[0-9]{2}\%",s)
j = ""

comb = []
for i in range(len(st)):
	if st[i][-1] == '%':
		temp = re.findall(r'-\d+|\d+', st[i])
		st[i] = temp[0]

if not re.match(r'[-]?\d+', st[-1]):
	st.append('0')
	
for i in zip(st[:-1], st[1:]):
	if re.match(r'[-]?\d+', i[0]):
		print(i)
	else:
		if '<' in i[1]:
			comb.append([i[0], '0'])
		else:
			comb.append(i)
		
for i in comb:
	print(i[1])
	w.write(i[1] + '\n')
	
print(len(comb))
r.close()
w.close()