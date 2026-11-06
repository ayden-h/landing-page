"""Independent finite checks for selected 1983–1999 solution records.
Run with Python 3; uses exact arithmetic and no external dependencies.
These checks support, and do not replace, the written proofs.
"""
from itertools import combinations,product,permutations
from fractions import Fraction as F
from collections import Counter,defaultdict
from functools import lru_cache
from pathlib import Path
import json,math
results={}
def check(id,value,expected,note):
 assert value==expected,(id,value,expected)
 results[id]=dict(result=str(value),expected=str(expected),method=note)
check('1983-A-07',sum(any((b-a)%25 in (1,24) for a,b in combinations(t,2)) for t in combinations(range(25),3)),550,'Enumerated all 2300 selected seat triples.')
check('1983-A-10',sum(sorted(Counter(str(n)).values())==[1,1,2] for n in range(1000,2000)),432,'Enumerated all 1000 candidate numerals.')
s=0
for mask in range(1,128):
 a=[i+1 for i in range(7) if mask>>i&1][::-1]
 s+=sum(v*(-1)**j for j,v in enumerate(a))
check('1983-A-13',s,448,'Directly summed the 127 nonempty subset values.')
scores=defaultdict(set)
for c in range(31):
 for w in range(31-c):scores[30+4*c-w].add(c)
check('1984-A-10',min(s for s,c in scores.items() if s>80 and len(c)==1),119,'Enumerated all feasible correct/wrong counts.')
check('1984-A-11',sum(all(b-a>1 for a,b in zip(c,c[1:])) for c in combinations(range(12),5)),56,'Enumerated the 792 possible birch-position sets.')
check('1985-A-08',min(max(abs(a-b) for a,b in zip(z,[256,261,265,271,279,282,286])) for z in product([200,300],repeat=7) if sum(z)==1900),61,'Enumerated all binary rounding assignments using exact hundredths; proof excludes other integers.')
vec=[1,0,0,0]
for _ in range(7):vec=[sum(vec)-v for v in vec]
check('1985-A-12',F(vec[0],3**7),F(182,729),'Four-vertex integer walk count, independent of the scalar probability recurrence.')
vals=sorted(sum(3**i for i in range(8) if m>>i&1) for m in range(1,256))
check('1986-A-07',vals[99],981,'Enumerated and sorted every nonempty subset of the first eight ternary powers.')
candidates=[]
for n in range(100,1000):
 d=str(n);total=sum(int(''.join(p)) for p in permutations(d))-n
 if total==3194:candidates.append(n)
check('1986-A-10',candidates,[358],'Checked every three-digit original numeral, retaining multiplicities of all six position permutations.')
best=[0]
def subsetsearch(start,bits,total):
 best[0]=max(best[0],total)
 for v in range(start,16):
  shift=bits<<v
  if not bits&shift:subsetsearch(v+1,bits|shift,total+v)
subsetsearch(1,1,0)
check('1986-A-12',best[0],61,'Exhaustive subset-sum collision search over subsets of 1,…,15, pruning only provably invalid supersets.')
counts=0
for z in product('HT',repeat=15):
 c=Counter(''.join(z[i:i+2]) for i in range(14))
 counts+=c=={'HH':2,'HT':3,'TH':4,'TT':5}
check('1986-A-13',counts,560,'Enumerated all 32768 coin words and their 14 adjacent transitions.')
check('1987-A-01',sum(all(int(a)+int(b)<10 for a,b in zip(f'{m:04}',f'{1492-m:04}')) for m in range(1493)),300,'Enumerated all nonnegative summand pairs.')
orders=set()
def stackwalk(nextletter,stack,out):
 if nextletter==10 and not stack:
  for k in range(out.index(8)+1,10):orders.add(out[k:])
  return
 if nextletter<=9:stackwalk(nextletter+1,stack+(nextletter,),out)
 if stack:stackwalk(nextletter,stack[:-1],out+(stack[-1],))
stackwalk(1,(),())
check('1988-A-15',len(orders),704,'Enumerated all legal stack output histories and every lunch cut after the output of 8; deduplicated suffixes.')
bounds=[]
for k in range(2,122):
 low=[v for v in range(1,121) for _ in range(k-1)][:121-k]
 bounds.append(F((121-k)*1000-sum(low),121))
check('1989-A-11',max(bounds).__floor__(),947,'Exact capacity-minimal sums for every possible mode multiplicity 2,…,121.')
dp={0:0}
for _ in range(1989):
 nd={}
 for m,v in dp.items():
  for b in (0,1):
   if b and (m&(1<<3) or m&(1<<6)):continue
   nm=((m<<1)|b)&127;nd[nm]=max(nd.get(nm,-1),v+b)
 dp=nd
check('1989-A-13',max(dp.values()),905,'Exact seven-bit transfer dynamic program for all 1989 positions, forbidding separations 4 and 7.')
check('1990-A-01',[n for n in range(1,600) if n not in {i*i for i in range(25)}|{i**3 for i in range(10)}][499],528,'Direct filtering of all integers through 599.')
check('1990-A-09',sum('HH' not in ''.join(z) for z in product('HT',repeat=10)),144,'Enumerated all 1024 toss sequences.')
p=F(0)
for a in product('ab',repeat=3):
 for b in product('ab',repeat=3):
  if a<b:
   p+=F(2**(a.count('a')+b.count('b')),3**6)
check('1991-A-10',p,F(532,729),'Summed exact probabilities over all 64 pairs of received strings.')
nums={F(n,999).numerator for n in range(1,999)}
check('1992-A-05',len(nums),660,'Reduced every numerator 1,…,998 over 999 and deduplicated.')
check('1992-A-06',sum(all(int(a)+int(b)<10 for a,b in zip(str(n),str(n+1))) for n in range(1000,2000)),156,'Direct decimal-digit carry test on all 1000 consecutive pairs.')
check('1992-A-15',1991-len({sum(m//5**j for j in range(1,7)) for m in range(1,7980)}-{0}),396,'Enumerated all distinct trailing-zero counts until the first value 1992.')
check('1993-A-01',sum(n%2==0 and len(set(str(n)))==4 for n in range(4001,7000)),728,'Enumerated every integer strictly between the endpoints.')
check('1993-A-08',sum((a|b)==63 for a in range(64) for b in range(a,64)),365,'Enumerated every unordered pair of six-bit subsets.')
check('1993-A-10',[(v,t,p) for v in range(1,61) for t in range(17) for p in range(17) if v*(t+p-2)==60 and v*(5*t+3*p)==480],[(30,2,2)],'Exhausted the integer incidence equations; no regular-face assumption.')
check('1994-A-06',sum(abs(a-b-c)==1 for a,b,c in product(range(-10,11),repeat=3)),660,'Enumerated all 21³ triples of line indices with unit altitude.')
@lru_cache(None)
def tile(u,h):
 if not u and not h:return F(1)
 r=2*u+h;ans=F(0)
 if u and h<2:ans+=F(2*u,r)*tile(u-1,h+1)
 if h:ans+=F(h,r)*tile(u,h-1)
 return ans
check('1994-A-09',tile(6,0),F(9,385),'Independent exact dynamic program by unopened pairs and held unmatched tiles.')
check('1994-A-11',len({2*a+5*b for a in range(95) for b in range(95-a)}),465,'Enumerated all feasible orientation-count pairs and deduplicated heights.')
hit=0
for walk in product([(1,0),(-1,0),(0,1),(0,-1)],repeat=6):
 x=y=0;found=False
 for dx,dy in walk:
  x+=dx;y+=dy;found|=(x,y)==(2,2)
 hit+=found
check('1995-A-03',F(hit,4**6),F(3,64),'Enumerated all 4096 six-step walks and tested first or later visits.')
check('1995-A-08',sum(x%y==0 and (x+1)%(y+1)==0 for x in range(1,101) for y in range(1,x)),85,'Checked every bounded integer pair directly.')
wins=0
edges=list(combinations(range(5),2))
for z in product((0,1),repeat=10):
 score=[0]*5
 for (a,b),bit in zip(edges,z):score[(a,b)[bit]]+=1
 wins+=all(0<s<4 for s in score)
check('1996-A-06',F(wins,1024),F(17,32),'Enumerated all 1024 labeled tournament orientations.')
rot=lambda z:(z[1],6-z[0])
orbits=set()
for pair in combinations(list(product(range(7),repeat=2)),2):
 rots=[]
 for _ in range(4):
  rots.append(tuple(sorted(pair)));pair=tuple(map(rot,pair))
 orbits.add(min(rots))
check('1996-A-07',len(orbits),300,'Canonicalized every marked-cell pair under four explicit coordinate rotations.')
closed=list(range(1,1025));right=False
while len(closed)>1:
 if right:closed=closed[::-1]
 closed=closed[1::2]
 if right:closed=closed[::-1]
 right=not right
check('1996-A-09',closed[0],342,'Simulated alternating passes over the actual list of closed lockers.')
check('1996-A-14',len({F(k,n) for n in [150,324,375] for k in range(1,n)})+1,768,'Built the exact union of all interior rational crossing times.')
rows=list(combinations(range(4),2));balanced=0
for ar in product(rows,repeat=4):balanced+=all(sum(j in row for row in ar)==2 for j in range(4))
check('1997-A-08',balanced,90,'Enumerated all 6⁴ row patterns and checked column sums.')
cards=list(product(range(3),repeat=3))
check('1997-A-10',sum(all(len({c[j] for c in tri}) in (1,3) for j in range(3)) for tri in combinations(cards,3)),117,'Checked all 2925 three-card subsets directly.')
check('1998-A-02',sum(x<=2*y<=60 and y<=2*x<=60 for x in range(1,61) for y in range(1,61)),480,'Directly tested all bounded positive lattice pairs.')
oddpatterns=0
for odd in combinations(range(9),5):oddpatterns+=all(sum(j in odd for j in range(3*i,3*i+3))%2 for i in range(3))
check('1998-A-04',F(oddpatterns,math.comb(9,5)),F(3,14),'Enumerated all 126 parity placements among the dealt positions.')
check('1998-A-07',sum(1 for a in range(1,99,2) for b in range(1,99-a,2) for c in range(1,99-a-b,2) if 98-a-b-c>0 and (98-a-b-c)%2),19600,'Enumerated the first three odd parts and tested the forced fourth.')
check('1999-A-07',sum((10-x)*(10-y)*(10-z)%4==0 for x,y,z in product(range(10),repeat=3)),650,'Checked the advance count for all 1000 switch labels.')
Path(__file__).with_name('early_exact_check_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('PASSED',len(results),'exact finite checks')
