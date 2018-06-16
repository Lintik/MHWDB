import re

r = open('HeavyBowgun.txt','r')
s = r.read()
w = []
w.append(open('HeavyBowgunNrm1.txt', 'w+'))
w.append(open('HeavyBowgunNrm2.txt', 'w+'))
w.append(open('HeavyBowgunNrm3.txt', 'w+'))

w.append(open('HeavyBowgunRec1.txt', 'w+'))
w.append(open('HeavyBowgunRec2.txt', 'w+'))

w.append(open('HeavyBowgunFla.txt', 'w+'))

w.append(open('HeavyBowgunSli.txt', 'w+'))

w.append(open('HeavyBowgunPrc1.txt', 'w+'))
w.append(open('HeavyBowgunPrc2.txt', 'w+'))
w.append(open('HeavyBowgunPrc3.txt', 'w+'))

w.append(open('HeavyBowgunPoi1.txt', 'w+'))
w.append(open('HeavyBowgunPoi2.txt', 'w+'))

w.append(open('HeavyBowgunWat.txt', 'w+'))

w.append(open('HeavyBowgunWyz.txt', 'w+'))

w.append(open('HeavyBowgunSpr1.txt', 'w+'))
w.append(open('HeavyBowgunSpr2.txt', 'w+'))
w.append(open('HeavyBowgunSpr3.txt', 'w+'))

w.append(open('HeavyBowgunPar1.txt', 'w+'))
w.append(open('HeavyBowgunPar2.txt', 'w+'))

w.append(open('HeavyBowgunFre.txt', 'w+'))

w.append(open('HeavyBowgunDem.txt', 'w+'))

w.append(open('HeavyBowgunSti1.txt', 'w+'))
w.append(open('HeavyBowgunSti2.txt', 'w+'))
w.append(open('HeavyBowgunSti3.txt', 'w+'))

w.append(open('HeavyBowgunSle1.txt', 'w+'))
w.append(open('HeavyBowgunSle2.txt', 'w+'))

w.append(open('HeavyBowgunThn.txt', 'w+'))

w.append(open('HeavyBowgunArm.txt', 'w+'))

w.append(open('HeavyBowgunClu1.txt', 'w+'))
w.append(open('HeavyBowgunClu2.txt', 'w+'))
w.append(open('HeavyBowgunClu3.txt', 'w+'))

w.append(open('HeavyBowgunExh1.txt', 'w+'))
w.append(open('HeavyBowgunExh2.txt', 'w+'))

w.append(open('HeavyBowgunDra.txt', 'w+'))

w.append(open('HeavyBowgunTra.txt', 'w+'))

st = re.findall("Nrm.+$",s, re.MULTILINE)
comb = []
for i in st:
    comb.append(re.findall("\d+", i))
for i in comb:
    print(i)
    for j in range(len(i)):
        w[j].write(i[j] + '\n')
print(len(comb))

r.close()


