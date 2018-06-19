import re

r = open('SwitchAxe.txt','r')
s = r.read()
w = open('SwitchAxePhial.txt', 'w+')

st = re.findall(r"^.+Phial",s,re.MULTILINE)

st = list(map(lambda x: x.strip(), st))
for i in st:
    w.write(i + '\n')
    print(i)

print(len(st))
r.close()
w.close()