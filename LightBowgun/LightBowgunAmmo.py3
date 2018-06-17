import re

r = open('LightBowgun.txt','r')
s = r.read()
w = []
w.append(open('LightBowgunNrm1.txt', 'w+'))
w.append(open('LightBowgunNrm2.txt', 'w+'))
w.append(open('LightBowgunNrm3.txt', 'w+'))

w.append(open('LightBowgunRec1.txt', 'w+'))
w.append(open('LightBowgunRec2.txt', 'w+'))

w.append(open('LightBowgunFla.txt', 'w+'))

w.append(open('LightBowgunSli.txt', 'w+'))

w.append(open('LightBowgunPrc1.txt', 'w+'))
w.append(open('LightBowgunPrc2.txt', 'w+'))
w.append(open('LightBowgunPrc3.txt', 'w+'))

w.append(open('LightBowgunPoi1.txt', 'w+'))
w.append(open('LightBowgunPoi2.txt', 'w+'))

w.append(open('LightBowgunWat.txt', 'w+'))

w.append(open('LightBowgunWyz.txt', 'w+'))

w.append(open('LightBowgunSpr1.txt', 'w+'))
w.append(open('LightBowgunSpr2.txt', 'w+'))
w.append(open('LightBowgunSpr3.txt', 'w+'))

w.append(open('LightBowgunPar1.txt', 'w+'))
w.append(open('LightBowgunPar2.txt', 'w+'))

w.append(open('LightBowgunFre.txt', 'w+'))

w.append(open('LightBowgunDem.txt', 'w+'))

w.append(open('LightBowgunSti1.txt', 'w+'))
w.append(open('LightBowgunSti2.txt', 'w+'))
w.append(open('LightBowgunSti3.txt', 'w+'))

w.append(open('LightBowgunSle1.txt', 'w+'))
w.append(open('LightBowgunSle2.txt', 'w+'))

w.append(open('LightBowgunThn.txt', 'w+'))

w.append(open('LightBowgunArm.txt', 'w+'))

w.append(open('LightBowgunClu1.txt', 'w+'))
w.append(open('LightBowgunClu2.txt', 'w+'))
w.append(open('LightBowgunClu3.txt', 'w+'))

w.append(open('LightBowgunExh1.txt', 'w+'))
w.append(open('LightBowgunExh2.txt', 'w+'))

w.append(open('LightBowgunDra.txt', 'w+'))

w.append(open('LightBowgunTra.txt', 'w+'))

st = re.findall("Nrm.+$",s, re.MULTILINE)
comb = []
for i in st:
    comb.append(re.findall(r"\d+", i))
for i in comb:
    print(i)
    for j in range(len(i)):
        w[j].write(i[j] + '\n')
print(len(comb))

r.close()


