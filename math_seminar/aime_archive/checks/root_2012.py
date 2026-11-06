"""Scoped exact and finite checks of the newly written 2012 solutions."""
from fractions import Fraction as F
from math import gcd,isqrt
from pathlib import Path
import json
passed=[]
def check(ident,description,condition):
 assert condition,(ident,description)
 passed.append({'id':ident,'check':description,'status':'passed'})
check('2012-I-02','Odd increment total and arithmetic mean',sum(range(1,22,2))==836-715 and F(715,11)*3==195)
# Direct physical simulation by relative speed, independent of the proof's
# accumulated-mile recurrence. After S leaves the horse at post one, B picks up.
walk={'B':F(4),'S':F(5,2)};rider='B';other='S';post=1;pickup=F(1,4);other_position=1+F(5,2)*(pickup-F(1,6));history=[]
for step in range(30):
 dt=(other_position-post)/(6-walk[other]);catch=post+6*dt;catch_time=pickup+dt
 history.append(catch)
 if catch.denominator==1:break
 next_post=catch.numerator//catch.denominator+1
 arrival=pickup+F(next_post-post,6)
 next_pickup=pickup+(next_post-other_position)/walk[other]
 assert next_pickup>arrival
 other_position=next_post+walk[rider]*(next_pickup-arrival)
 rider,other=other,rider;post=next_post;pickup=next_pickup
check('2012-I-04','Simulate actual catch-up times and horse waiting at each post',catch==19 and catch_time==F(13,3) and len(history)==10 and all(x.denominator>1 for x in history[:-1]))
check('2012-I-06','Reduce every possible positive root angle',all(F(k,71).denominator==F(71-k,71).denominator==71 for k in range(1,71)))
# Independent integral by elementary antiderivatives: for fixed y in [0,1],
# x runs y/2..1 and z runs 0..(2x-y)/4.
volume=F(1,4)-F(1,8)+F(1,48)
check('2012-I-08','Exact planar-section integral',volume==F(7,48) and 1-volume==F(41,48))
for k in (F(-7,3),F(1),F(12)):
 X=F(-1,6);Y=-1-k/12;Z=-2+5*k/12
 check('2012-I-09','Substitute three free-parameter values in all logarithmic coordinates',2*(Y+1)/X==2*(Z+2)/(X+1)==(Y+Z+3)/(4*X+1)==k and X+5*Y+Z==F(-43,6))
roots=[u for u in range(1,2485) if u*u%1000==256]
check('2012-I-10','Enumerate all positive square roots up to the tenth candidate',roots==[16,484,516,984,1016,1484,1516,1984,2016,2484] and (roots[-1]**2-256)//1000==6170)
check('2012-I-12','Exact normalized side and projection squares',4**2+48==8**2 and 11**2+48==13**2)
check('2012-I-13','Both quadratic-surd squared-side values annihilate the eliminated polynomial',25**2+12**2*3-50*25+193==0 and 2*25*12-50*12==0 and 25**2>12**2*3)
for a,b in ((3,4),(5,12),(7,24),(2,3)):
 points=[(F(-a,3),F(-b,3)),(F(2*a,3),F(-b,3)),(F(-a,3),F(2*b,3))]
 check('2012-I-14','Translate independent right triangles to their centroids',sum(x*x+y*y for x,y in points)==F(2,3)*(a*a+b*b))
pairs=[(m,n) for m in range(1,101) for n in range(1,168) if 20*m+12*n==2012]
check('2012-II-01','Enumerate all positive lattice points in the bounding rectangle',len(pairs)==34)
check('2012-II-02','Nonzero-ratio target and explicit zero-ratio alternative',27*F(11,3)**2==363 and 27*0**14==99*0**10 and 27*0**8==0)
L,W,d=F(6),F(7,5),F(24,5)
check('2012-II-04','Reconstruct all three route lengths and verify containment',2*L+W-d==F(43,5) and W+d==F(31,5) and W*W+d*d==25 and L>W and 0<d<L)
check('2012-II-05','Slant height, altitude, and volume',F(25,2)**2-F(15,2)**2==100 and 225*10//3==750)
check('2012-II-06','Squared modulus and fourth power of maximizing direction',(-375)**2+500**2==625**2 and -375+500==125)
# Gaussian rational arithmetic for an explicit original-equation witness.
def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def div(z,w):
 d=w[0]**2+w[1]**2
 return((z[0]*w[0]+z[1]*w[1])/d,(z[1]*w[0]-z[0]*w[1])/d)
def add(z,w):return(z[0]+w[0],z[1]+w[1])
z=(F(1),F(-1));w=(F(2),F(4))
check('2012-II-08','Substitute Gaussian-rational witness into both original equations',add(z,div((F(0),F(20)),w))==(5,1) and add(w,div((F(0),F(12)),z))==(-4,10) and mul(z,w)==(6,2))
check('2012-II-09','Exact squared trigonometric ratios and final sum',9*F(3,35)+F(1,4)*F(32,35)==1 and F(3,2)-F(19,29)==F(49,58))
valid=[]
for n in range(1,1000):
 k=isqrt(n);x=F(n,k)
 if x.numerator//x.denominator==k:valid.append(n)
check('2012-II-10','Enumerate each integer output with its only possible floor branch',len(valid)==496)
def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
M=[[6,-7],[9,3]]
check('2012-II-11','Exact matrix cube and candidate orbit',matmul(matmul(M,M),M)==[[-729,0],[0,-729]])
x=F(5,3);orbit=[]
for _ in range(3):x=(6*x-7)/(9*x+3);orbit.append(x)
check('2012-II-11','All intermediate iterates stay in the domain',orbit==[F(1,6),F(-4,3),F(5,3)])
x,ycoef=F(120,19),F(-30,19);norm=x*x+3*ycoef*ycoef
check('2012-II-15','Reconstruct second circle intersection in Q(sqrt(3))',norm-8*x-2*ycoef==0 and norm-F(79,8)*x+15==0 and norm==F(900,19))
report={'scope':'Finite and exact checks supplement the written proofs. Repeated parameter cases count separately. No claim of formal verification of all geometry or analytic arguments.','passed':len(passed),'checks':passed}
root=Path(__file__).resolve().parents[1]
(root/'data/root_2012_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':len(passed),'unique_problem_ids':len({r['id'] for r in passed})},indent=2))
