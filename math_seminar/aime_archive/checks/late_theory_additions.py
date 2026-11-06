"""Exact finite checks for Geometry 13.3/14.11 and Number Theory 9.4/9.5."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
counts={}
# Q(sqrt(5)) represented by (rational part, sqrt(5) coefficient).
def qa(p,q):return p[0]+q[0],p[1]+q[1]
def qs(a,p):return a*p[0],a*p[1]
def qm(p,q):return p[0]*q[0]+5*p[1]*q[1],p[0]*q[1]+p[1]*q[0]
def qsum(seq):
 out=(F(0),F(0))
 for x in seq:out=qa(out,x)
 return out
phi=(F(1,2),F(1,2));iphi=(F(-1,2),F(1,2))
# Exact cyclotomic ring Q[zeta]/(1+zeta+...+zeta^4).
def red(poly):
 p=list(poly)+[F(0)]*max(0,4-len(poly))
 for k in range(len(p)-1,3,-1):
  c=p[k]
  for j in range(1,5):p[k-j]-=c
 return tuple(p[:4])
def rp(k):return red([F(0)]*k+[F(1)])
def ra(p,q):return tuple(a+b for a,b in zip(p,q))
def rm(p,q):
 t=[F(0)]*7
 for i in range(4):
  for j in range(4):t[i+j]+=p[i]*q[j]
 return red(t)
def embed(q):
 # sqrt(5)=1+2*zeta+2*zeta^4.
 return red([q[0]+q[1],2*q[1],0,0,2*q[1]])
cosines=[(F(2),F(0)),qs(-1,phi),iphi,iphi,qs(-1,phi)]
cases=0
for s,u,v in product([10,12,14],range(-2,3),range(-2,3)):
 # Positive side lengths, made from constant and second-frequency modes.
 assert s>2*(abs(u)+abs(v))
 sides=[qa((F(s),F(0)),qa(qs(u,cosines[i]),qs(v,cosines[(i-1)%5]))) for i in range(5)]
 closure=(F(0),)*4
 for i,a in enumerate(sides):closure=ra(closure,rm(embed(a),rp(i)))
 assert closure==(0,0,0,0)
 S=qsum(qm(a,a) for a in sides)
 J=qsum(qm(sides[i],sides[(i+1)%5]) for i in range(5))
 D=qa(qs(2,S),qm(J,iphi))
 P=qsum(sides)
 assert qm(P,P)==qm((0,1),qa(qs(2,D),qs(-3,S)))
 cases+=1
counts['equiangular_pentagons_with_exact_vector_closure']=cases
cases=0
for a,b in product([F(-1),F(-1,2),F(0),F(1,2),F(1)],repeat=2):
 c=F(5);q=a*a+b*b
 assert (2*a)**2+(2*b)**2+(q-1)**2==(q+1)**2
 for x,y in product(range(-2,3),repeat=2):
  r=a*x+b*y+c
  assert r>0
  assert 2*a*x+2*b*y+(q-1)*r+2*c==(q+1)*r
  cases+=1
counts['affine_sphere_radii_and_common_tangent_plane']=cases

def tau(n):return sum(n%d==0 for d in range(1,n+1))
cases=0
for b,N in product(range(2,21),range(1,31)):
 L=4
 U=sum((F(tau(N+j),b**j) for j in range(1,L+1)),F(0))+F(1,b**L)*(F(N+L,b-1)+F(b,(b-1)**2))
 if U>=1:continue
 # Independent original-denominator series, with an exact infinite tail bound.
 K=N+10
 X=sum((F(1,b**k-1) for k in range(1,K+1)),F(0))
 scaled=b**N*X
 tail=F(b**(N+1),(b-1)*(b**(K+1)-1))
 lo=scaled.numerator//scaled.denominator
 upper=scaled+tail;hi=upper.numerator//upper.denominator
 assert lo==hi
 ell=min(3,N)
 block=sum(tau(m)*b**(N-m) for m in range(N-ell+1,N+1))
 assert lo%b**ell==block%b**ell
 cases+=1
counts['carry_certificate_checked_against_original_infinite_series']=cases
out={'all_passed':True,'total_cases':sum(counts.values()),'cases':counts,'note':'Finite exact parameter checks supplement the written general proofs.'}
Path(__file__).with_name('late_theory_additions_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
