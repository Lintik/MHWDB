import re

r = open('Bow.txt','r')
s = r.read()
w1 = open('BowArrowCls.txt', 'w+')
w2 = open('BowArrowPow.txt', 'w+')
w3 = open('BowArrowPar.txt', 'w+')
w4 = open('BowArrowPoi.txt', 'w+')
w5 = open('BowArrowSle.txt', 'w+')
w6 = open('BowArrowBla.txt', 'w+')

st = re.findall("<a href=\"https://mhworld.kiranico.com/weapon/[0-9\&\#\;\'a-zA-Z-></\" ]{3,}",s)
j = ""

comb = []
