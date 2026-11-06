"""Independent finite checks of selected recent mathematical arguments.
No downloaded problem statements or source solutions are included.
Run with Python 3.9 or newer; all claimed counts use exact integers/rationals.
"""
from itertools import combinations,permutations,product
from math import comb,ceil,factorial,isqrt
from fractions import Fraction
from collections import Counter
from pathlib import Path
import json
results=[]
def check(id,value,expected,method):
    assert value==expected,(id,value,expected)
    results.append(dict(id=id,result=str(value),method=method,passed=True))
check('2014-II-09',sum(any(all(bits[(i+j)%10] for j in range(3)) for i in range(10)) for bits in product(range(2),repeat=10)),581,'Enumerate all 1024 cyclic binary words.')
check('2015-I-14',sum((isqrt(n)*n-isqrt(n)*(isqrt(n)+1)//2)%2==0 for n in range(2,1001)),483,'Direct parity count for every allowed n.')
check('2016-II-13',sum(min(i+p[i-1] for i in range(1,7)) for p in permutations(range(1,7))),2619,'Enumerate all 720 rook permutations; sum their minimum scores.')
check('2018-I-09',sum(any(a+b==16 for a,b in combinations(s,2)) and any(a+b==24 for a,b in combinations(s,2)) for s in combinations(range(1,21),4)),210,'Enumerate every four-subset.')
check('2020-I-11',sum(1 for a,b,c in product(range(-10,11),repeat=3) if a==-6 or c==-20-6*a-2*b),510,'Enumerate every coefficient triple.')
candidates=[set(range(t,t+4)) for t in range(10,97) if any(a!=b and a%6==0 and b%7==0 for a,b in product(range(t,t+4),repeat=2))]
d=Counter(v for s in candidates for v in s)
survivors=[s for s in candidates if all(d[v]>1 for v in s)]
d2=Counter(v for s in survivors for v in s)
final=[s for s in survivors if all(d2[v]==1 for v in s)]
check('2021-II-11',sum(max(s) for s in final),258,'Enumerate candidate intervals and both knowledge announcements.')
check('2022-I-06',sum(not any(all(x+i*d in {3,4,5,a,b,30,40,50} for i in range(4)) for x in range(3,51) for d in range(1,16)) for a,b in combinations(range(6,30),2)),228,'Test all possible four-term progressions for every candidate pair.')
m=Fraction(1)
for p in permutations(range(1,10)):
    num=p[0]*p[1]*p[2]-p[3]*p[4]*p[5]
    if num>0:m=min(m,Fraction(num,p[6]*p[7]*p[8]))
check('2022-I-07',m,Fraction(1,288),'Exhaust all digit permutations.')
f=lambda b,c:b+ceil(c/b)-2+max(1,ceil((1001-b*ceil(c/b))/c))
possible=[c for c in range(3,90) if any(f(b,c)==97 for b in range(2,c))]
check('2022-II-14',possible,[11,88,89],'Evaluate exact optimal stamp formula for every smaller denomination pair.')
check('2023-I-11',sum(sum(bits[i]*bits[i+1] for i in range(9))==1 for bits in product(range(2),repeat=10)),235,'Enumerate all subsets directly.')
check('2024-I-11',sum(any(not any(bits[i] and bits[(i+r)%8] for i in range(8)) for r in range(8)) for bits in product(range(2),repeat=8)),115,'Test all rotations for all 256 colorings.')
check('2025-I-05',sum(int(''.join(map(str,p)))%22==0 for p in permutations(range(1,9))),2304,'Test divisibility for all 40320 digit permutations.')
cubes=Counter(n**3%2187 for n in range(1,730))
check('2025-I-15',sum(ca*cb*cubes[(-a-b)%2187] for a,ca in cubes.items() for b,cb in cubes.items()),885735,'Convolve exact cube-residue frequencies.')
# Four internal edges in cyclic order, plus two private exterior edges per cell.
check('2025-II-03',sum(all(v[i]+v[(i+1)%4]+v[4+2*i]+v[5+2*i]==2 for i in range(4)) for v in product(range(2),repeat=12)),82,'Enumerate every coloring of the twelve edges.')
check('2025-II-10',sum(not any(all(i+j in s for j in range(3)) for i in range(14)) for s in map(set,combinations(range(16),8))),2907,'Enumerate every eight-seat subset.')
check('2026-I-07',sum(all(p[p[p[p[p[p[a]]]]]]==a for a in range(6)) for p in permutations(range(6))),396,'Directly test the sixth iterate of every permutation.')
condition=favorable=0
for faces in product(range(6),repeat=6):
    visible={max(i+1 for i in range(6) if faces[i]==f) for f in set(faces)}
    if {2,4,6}<=visible:
        condition+=1;favorable+=len(set(faces))==5
check('2026-I-09',(condition,favorable),(14400,6480),'Enumerate all 46656 roll-face sequences.')
S=[0]*502
for k in range(10001):
    high,low=divmod(k,503)
    coefficient=(comb(19,high)*comb(443,low))%503 if high<=19 and low<=443 else 0
    S[k%502]=(S[k%502]+coefficient)%503
check('2026-I-13',S.count(0),39,'Lucas-theorem modular binomial calculation for all 10001 coefficients.')
def compositions(n):
    if n==0:yield ()
    for a in range(1,n+1):
        for tail in compositions(n-a):yield (a,)+tail
valid=0
for c in compositions(12):
    v=c[0]
    for b in c[1:]:v=v-b if v%2 and b%2==0 else v+b
    valid+=v==0
check('2026-II-14',valid,157,'Evaluate the operation on all 2048 compositions of 12.')
hist=Counter()
for a in product((-1,0,1),repeat=7):
    if sum(a)%3==0 and sum(a[i]*a[(i+1)%7]*a[(i+3)%7] for i in range(7))%3==0:hist[sum(x!=0 for x in a)]+=1
check('2026-II-15',[hist[i] for i in range(8)],[1,0,42,56,42,168,84,0],'Enumerate all 2187 residue tuples and both congruences.')
valid=0
for increments in product((-3,-2,-1,1,2,3),repeat=6):
    if sum(increments)!=12:continue
    values=[0]
    for d in increments:values.append(values[-1]+d)
    valid+=all(j-i<=abs(values[j]-values[i])<=3*(j-i) for i in range(7) for j in range(i+1,7))
check('2018-II-15',valid,185,'Enumerate all six-step increment sequences and every pairwise bound.')
out=Path(__file__).with_name('recent_independent_results.json');out.write_text(json.dumps(results,indent=2))
print(f'{len(results)} independent exact checks passed; report: {out}')
