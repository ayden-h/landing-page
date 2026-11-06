"""Independent exact checks for the sixteen newly authored 2026 records."""
from fractions import Fraction as F
from itertools import product, combinations
from math import isqrt
from pathlib import Path
import json
results=[]
def check(id,description,condition,detail):
 assert condition,(id,description,detail)
 results.append(dict(id=id,description=description,passed=True,detail=detail))
# Three motions.
speeds=[F(18,5),F(28,5),F(63,5)];times=[F(14,5),F(9,5),F(4,5)]
d=[v*t for v,t in zip(speeds,times)]
check('2026-I-01','Substitute all three original travel distances',len(set(d))==1 and d[0]==F(252,25),str(d[0]))
check('2026-I-03','Boundary center distance and area ratio',23200+42**2==158**2 and F(23200,200**2)==F(29,50),'29/50')
values={a+b+a*b for a in range(1,101) for b in range(a+1,101) if a+b+a*b<=100}
check('2026-I-04','Enumerate all unequal positive-factor representations',len(values)==70,str(len(values)))
check('2026-I-05','Substitute the recovered rotation cosine',5-4*F(29,36)==F(16,9),'squared displacement 16/9')
prime=all(1013%d for d in range(2,isqrt(1013)+1))
check('2026-I-06','Trial-divide 1013 and count exponent choices',prime and len(list(product(range(21),repeat=2)))==441,'1013 prime; 441 exponent pairs')
# Exact rotation, branch signs, and independent shoelace area.
A=(F(5),F(12));B=(F(0),F(0));C=(F(14),F(0));O=(F(7),F(33,8))
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def sub(p,q):return tuple(a-b for a,b in zip(p,q))
def rot(p,c,s):
 x,y=sub(p,O);return O[0]+c*x-s*y,O[1]+s*x+c*y
Ap,Bp,Cp=[rot(p,F(4,5),F(-3,5)) for p in [A,B,C]]
poly=[A,Ap,C,Cp,B,Bp]
area=abs(sum(cross(p,q) for p,q in zip(poly,poly[1:]+poly[:1])))/2
orient=lambda p:cross(sub(Cp,Bp),sub(p,Bp))
check('2026-I-10','Exact rotation, opposite-side signs, and shoelace',Ap[0]==Cp[0] and orient(Ap)*orient(B)<0 and area==F(1557,10),str(area))
# Reflection and actual common tangent plane.
G=(F(2),F(4,3));factor=2*(12-2*G[0]-3*G[1])/13
D=(G[0]+2*factor,G[1]+3*factor);r=F(122,39)
centers=[(0,0,F(1)),(6,0,F(2)),(0,4,F(3)),(*D,r)]
check('2026-I-12','Reflect centroid and verify all signed sphere-plane distances',D==(F(42,13),F(124,39)) and all(6*x+18*y-13*z+36==23*z for x,y,z in centers) and 6**2+18**2+13**2==23**2,str(r))
# Arithmetic in Q(sqrt(5)).
def add(p,q):return p[0]+q[0],p[1]+q[1]
def mul(p,q):return p[0]*q[0]+5*p[1]*q[1],p[0]*q[1]+p[1]*q[0]
def scale(a,p):return a*p[0],a*p[1]
phi=(F(1,2),F(1,2));iphi=(F(-1,2),F(1,2));J=scale(184,phi);K=scale(492,iphi)
closure=add(add((F(308),F(0)),mul(J,iphi)),scale(-1,mul(phi,K)))
perimeter2=add(add((F(308),F(0)),scale(2,J)),scale(2,K))
check('2026-I-14','Verify both cyclic quadratic identities in Q(sqrt(5))',closure==(0,0) and perimeter2==(0,676),str(perimeter2))
ds=[d for d in range(1,31) if 20%d==0 and 30%d==0]
check('2026-II-01','Enumerate all common differences for both variants',sum(4+10*d for d in ds)==196 and sum(4+9*d for d in ds)==178,str(ds))
bs=[b for b in range(15,2026) if (20*b-164)%16==0]
for b in bs:
 poly=[(0,0),(b,0),(b-14,14),(b-8,20),(0,20)]
 assert abs(sum(cross(p,q) for p,q in zip(poly,poly[1:]+poly[:1])))==2*(20*b-164)
check('2026-II-03','Enumerate the bounded integer lengths and check polygon areas',len(bs)==503 and (bs[0],bs[-1])==(17,2025),str(len(bs)))
stationary_squares=[F(0),F(80)]
radii2=[v*v/4-40*v+1681 for v in stationary_squares]
check('2026-II-06','Substitute every squared critical parameter',radii2==[1681,81],'radii 41,9')
triangles=[]
for leg in range(1,246):
 for base in range(1,2*leg):
  u2=F(base*base*leg,2*leg+base)
  if u2.denominator!=1:continue
  u=isqrt(u2.numerator)
  if u*u!=u2:continue
  if 6*(2*leg+base)==125*(2*u+base):triangles.append((leg,base,u))
check('2026-II-08','Exhaust all integral isosceles legs at most 245',triangles==[(245,10,7)],str(triangles))
S=sum((F(1,10**k-1) for k in range(1,111)),F(0))
scaled=10**100*S
# For k >=111, 1/(10^k-1) <=10^-k/(1-10^-111).
tail=F(10**101,9*(10**111-1))
lo=scaled.numerator//scaled.denominator;hi=(scaled+tail).numerator//(scaled+tail).denominator
check('2026-II-09','Direct rational series with rigorous omitted-tail bound',lo==hi and lo%1000==669,'both floor bounds have residue 669')
bases=[]
for a in range(26,425):
 bd=F(8*a,17);cd=F(9*a,17)
 ae=200-bd*bd/200;af=225-cd*cd/225
 if all(t.denominator==1 and t>0 for t in [bd,cd,ae,af]):bases.append(a)
check('2026-II-10','Enumerate every integral base within strict triangle bounds',bases==[85,170,255,340] and sum(bases)==850,str(bases))
a=4+0j;b=-2+1j;c=-2-1j
sums={sa*a+sb*b+sc*c for sa,sb,sc in product([-1,1],repeat=3)}
roots=[a*a,b*b,c*c]
check('2026-II-11','Expand the explicit Gaussian-integer roots and all signed sums',len(sums)==7 and sum(roots)==22 and sum(x*y for x,y in combinations(roots,2))==121 and roots[0]*roots[1]*roots[2]==400,'7 signed sums; Vieta coefficients 22,121,400')
vertices=[(-5,0,0),(5,0,0),(0,9,12),(0,-9,12)]
edges=sorted(sum((x-y)**2 for x,y in zip(p,q)) for p,q in combinations(vertices,2))
s=F(25,3);r=F(75,16)
check('2026-II-12','Verify six edges, both centers, and reduced center separation',edges==[100,250,250,250,250,324] and 25+s*s==81+(12-s)**2 and 3*r/5==(60-5*r)/13 and s-r==F(175,48),str(s-r))
out=dict(checks=len(results),all_passed=all(x['passed'] for x in results),results=results)
Path(__file__).with_name('early_agent_2026_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
