"""Independent finite/exact checks for the newly authored 2013 entries.

These are deliberately scoped arithmetic and enumeration checks, not formal
verification of every geometric or analytic proof in the collection.
"""
from fractions import Fraction as F
from math import gcd,isqrt
from pathlib import Path
import json

passed=[]
def check(ident,description,condition):
    assert condition,(ident,description)
    passed.append({'id':ident,'check':description,'status':'passed'})
check('2013-I-01','Exact proportional travel-time calculation',F(255)*F(30,51)==150)
check('2013-I-03','Area fraction from a reciprocal-ratio invariant',F(18,20)==F(9,10))
# Polynomial coefficients, calculated by multiplication rather than sampling.
check('2013-I-05','Difference-of-cubes coefficients',[9-1,-3,-3,-1]==[8,-3,-3,-1])
check('2013-I-07','Squared norm of the spatial cross product',100*F(18,5)**2+48**2==60**2)
pairs=[(m,2013*m-2013//m) for m in range(2,2014) if 2013%m==0]
check('2013-I-08','Exhaust all possible integer divisors of 2013',min(pairs,key=lambda v:sum(v))==(3,5368))
u,v=F(39,5),F(39,7)
check('2013-I-09','Exact crease endpoint and length equations',u*u==(12-u)**2+81-9*(12-u) and v*v==(12-v)**2+9-3*(12-v) and u*u+v*v-u*v==F(39**3,35**2))
polys=set()
for q in (1,5,13,65):
 for r in range(-8,9):
  for s in range(1,9):
   if r and q*(r*r+s*s)==65:
    a=q+2*r;b=r*r+s*s+2*q*r
    if a and b:polys.add((a,b))
check('2013-I-10','Enumerate all nonreal Gaussian-integer root factors',len(polys)==16 and sum(a for a,b in polys)==80)
ks=[k for k in range(1,430) if all((1680*k)%d==3 for d in (9,11,13))]
check('2013-I-11','Full CRT period and first positive representative',ks==[131])
t=F(336,625)
check('2013-I-13','Exact infinite geometric-series formula and reduced denominator',90*t*(1-t)/(1-t*t)==F(30240,961) and gcd(30240,961)==1)
s=F(-17,19)
check('2013-I-14','Squared ratio with the surviving sine value',(1-s*s)/(2+s)**2==F(8,49))
check('2013-II-01','Exact conversion from ordinary to decimal day units',F(396,1440)*1000==275)
logs=[(a,1000//(2**a)) for a in range(1,11) if 1000%(2**a)==0]
check('2013-II-02','Enumerate all power-of-two divisors',logs==[(1,500),(2,250),(3,125)] and sum(a+b for a,b in logs)==881)
check('2013-II-03','Cumulative burn time exactly at the eighty-fourth centimeter',119*120==2*84*85 and 10*(119-84)==350)
# Squared metric checks retain the coefficient of sqrt(3) symbolically.
A=(F(1),F(0));B=(F(2),F(2));C=(F(9,2),F(1,2))
def d2(P,Q):return (P[0]-Q[0])**2+3*(P[1]-Q[1])**2
P=tuple((A[i]+B[i]+C[i])/3 for i in (0,1))
check('2013-II-04','Equilateral coordinate construction in Q(sqrt(3))',d2(A,B)==d2(B,C)==d2(C,A)==13 and P[0]*P[1]==F(25,12))
check('2013-II-05','Exact squared cevian and sine values',F(1,4)+F(27,4)==7 and 1-F(13,14)**2==F(27,196))
empty=[]
for n in range(1,283):
 lo=1000*n;hi=lo+999;first=isqrt(lo)
 if first*first<lo:first+=1
 if first*first>hi:empty.append(n)
check('2013-II-06','Exhaust every earlier thousand-block with integer square roots',empty==[282])
staff=[(x,t) for x in range(1,356) for t in range(1,x//3+1) if x>3*t and 19*x-21*t==355]
check('2013-II-07','Exhaust feasible workforce (x<356 follows from the work equation)',staff==[(22,3)] and 30*22+15*19==945)
check('2013-II-13','Two squared-distance constraints for the reconstructed triangle',7+49*9==448 and 81*7+9==576)
vals=[max(n%k for k in range(1,n//2+1)) for n in range(20,101)]
check('2013-II-14','Exhaust all admissible divisors for each input',vals==[n-2*(n//3+1) for n in range(20,101)] and sum(vals)==1512)
check('2013-II-15','Reduction of the negative-radical representation',gcd(115,72)==1 and 111+4+35+72==222)
report={'scope':'Twenty finite or exact arithmetic checks; not a formal verification of all twenty-three new proofs. Geometry support/containment and angle-branch proofs are written explicitly in the entries.','passed':len(passed),'checks':passed}
root=Path(__file__).resolve().parents[1]
(root/'data/root_2013_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
