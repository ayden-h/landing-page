"""Finite diagnostics for the authored expositions; not substitutes for proofs."""
from pathlib import Path
from fractions import Fraction
from math import isqrt,sqrt,prod, factorial
import json,random,collections
import numpy as np
OUT=Path(__file__).resolve().parent
results={}
def record(name,value):results[name]=value;print(name,value,flush=True)

for n in range(1,31):
    dp=[0]+[10**100]*n
    for i in range(n+1):
        dp=[min(dp[t-x]+2**i*x*x for x in range(t+1)) for t in range(n+1)]
    assert dp[n]==n*(n+1)//2,(n,dp[n])
record('A11_independent_dynamic_program',{'n':list(range(1,31)),'passed':True})

for lam in [1,3,8,12,40]:
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                v=a/sqrt(a*a+lam*b*c)+b/sqrt(b*b+lam*a*c)+c/sqrt(c*c+lam*a*b)
                assert v+1e-12>=min(1,3/sqrt(1+lam))
record('radical_parameter_grid',{'triples_per_parameter':216,'parameters':[1,3,8,12,40],'passed':True})

for n in range(1,30):
    z=[Fraction(2)-Fraction(1,2**k) for k in range(n+1)]
    assert sum(z)-n*z[-1]==Fraction(n+1,2**n)
record('real_crossing_counterexample',{'indices_checked':29,'passed':True})

sol=[]
for x in range(-12,40):
    val=1+Fraction(2)**x+Fraction(2)**(2*x+1)
    if val.denominator==1 and isqrt(val.numerator)**2==val.numerator:sol.append((x,isqrt(val.numerator)))
assert sol==[(0,2),(4,23)];record('N01_integer_square_search',{'x_range':[-12,39],'nonnegative_y_solutions':sol})
fac={factorial(m):m for m in range(1,101)}
sol=[(fac[L],n) for n in range(1,21) if (L:=prod(2**n-2**i for i in range(n))) in fac]
assert sol==[(1,1),(3,2)];record('N08_factorial_search',{'n_range':[1,20],'m_range':[1,100],'solutions':sol})
sol=[(a,b,c) for a in range(1,81) for b in range(1,a+1) for c in range(1,b+1) if a**3+b**3+c**3==(a*b*c)**2]
assert sol==[(3,2,1)];record('N09_ordered_triple_search',{'maximum_coordinate':80,'solutions':sol})
def divisors(n):
    low=[i for i in range(1,isqrt(n)+1) if n%i==0];return sorted(set(low+[n//i for i in low]))
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
sol=[]
for n in range(1,5001):
    ds=divisors(n)
    if all(n%(d+1)==0 or prime(d+1) for d in ds):sol.append(n)
assert sol==[1,2,4,12];record('N14_divisor_search',{'n_range':[1,5000],'solutions':sol})
for n in range(4,3001):
    ds=divisors(n)
    if len(ds)==2:continue
    condition=all((ds[i+1]+ds[i+2])%ds[i]==0 for i in range(len(ds)-2))
    pp=sum(prime(d) for d in ds)==1
    assert condition==pp,n
record('N13_divisor_chain_search',{'n_range':[4,3000],'passed':True})
actual=set()
for a in range(1,301):
    for b in range(a,301):
        q,r=divmod(a*a+b*b,a*b+1)
        if not r:
            assert isqrt(q)**2==q;actual.add((a,b,q))
predicted={(1,1,1)}
for s in range(2,301):
    a,b=0,s
    while b<=300:
        if a>0:predicted.add((a,b,s*s))
        a,b=b,s*s*b-a
assert actual==predicted
record('Vieta_complete_finite_orbit_comparison',{'coordinate_limit':300,'pairs':sorted(actual),'passed':True})
for a0 in range(2,401):
    a=a0;seen=set();repeat=False
    for _ in range(2500):
        if a in seen:repeat=True;break
        seen.add(a);r=isqrt(a);a=r if r*r==a else a+3
    assert repeat==(a0%3==0),a0
record('N16_recurrence_search',{'initial_range':[2,400],'step_limit':2500,'passed':True})
assert all((5**n-3**n)%(2**n+65) for n in range(1,501))
record('N12_divisibility_search',{'n_range':[1,500],'passed':True})

def cross(a,b):return float(a[0]*b[1]-a[1]*b[0])
def intersect(a,v,b,w):return a+np.linalg.solve(np.array([v,-w]).T,b-a)[0]*v
def circle(a,b,c):
    o=np.linalg.solve(2*np.array([b-a,c-a]),np.array([b@b-a@a,c@c-a@a]));return o,np.linalg.norm(a-o)
def second_on_line(o,r,start,known):
    v=known-start;t=((start-o)@(start-o)-r*r)/(v@v);return start+t*v
rng=random.Random(271828);res=[];count=0
for _ in range(1200):
    ang=sorted(rng.uniform(0,2*np.pi) for _ in range(4));A,B,C,D=[np.array([np.cos(t),np.sin(t)]) for t in ang]
    ac=np.linalg.norm(A-C);bd=np.linalg.norm(B-D);ad=np.linalg.norm(A-D)
    if not(ac<bd<ad and (D-B)@(A-B)>0):continue
    u=(B-A)/np.linalg.norm(B-A);v=(D-C)/np.linalg.norm(D-C)
    E=D+ac*u
    if cross(D-A,E-A)*cross(D-A,C-A)>0:E=D-ac*u
    F=A+bd*v
    if cross(D-A,F-A)*cross(D-A,C-A)>0:F=A-bd*v
    P=intersect(B,E-B,C,F-C)
    T=np.linalg.solve(2*np.array([C-B,F-E]),np.array([C@C-B@B,F@F-E@E]))
    res.extend([abs(P@P-1),abs(T@T-1),abs(np.linalg.norm(E-B)-np.linalg.norm(F-C))]);count+=1
assert count>15 and max(res)<1e-8,(count,max(res));record('G15_original_configuration_checks',{'admissible_random_cases':count,'max_residual':max(res)})

res=[];count=0
R=np.array([1.,0.]);S=np.array([np.cos(1.2),np.sin(1.2)]);Rp=2*S-R
for t in np.linspace(.05,1.15,50):
    I=np.array([np.cos(t),np.sin(t)]);o,r=circle(I,S,Rp);disc=r*r-(1-o[0])**2
    if disc<=0:continue
    aa=[np.array([1.,o[1]+sqrt(disc)]),np.array([1.,o[1]-sqrt(disc)])];A=min(aa,key=lambda a:np.linalg.norm(a-R))
    J=second_on_line(np.zeros(2),1.,A,I)
    res.append(abs((J-Rp)@(Rp-o)));count+=1
assert count>5 and max(res)<1e-9,(count,max(res));record('G10_tangent_checks',{'admissible_cases':count,'max_dot_residual':max(res)})

res=[];count=0
for t in np.linspace(.4,2.4,30):
    B=np.zeros(2);C=np.array([1.,0.]);A=C+np.array([np.cos(t),np.sin(t)]);D=A+C;P=-1.4*A
    o,r=circle(A,C,D);Q=second_on_line(o,r,P,D)
    op,rp=circle(A,P,Q);v=C-P;R=P-2*(v@(P-op))/(v@v)*v
    X=intersect(A,Q-A,C,D-C)
    res.append(abs(cross(R-B,X-B)));count+=1
assert max(res)<1e-8;record('G12_concurrency_checks',{'cases':count,'max_cross_residual':max(res)})

report={'status':'passed','role':'Finite computations and numerical diagnostics only; the manuscripts contain the proofs.','checks':results}
if OUT.name=='audit':
    (OUT/'Verification_Results.json').write_text(json.dumps(report,indent=2))
else:
    for subject in ['Algebra','Geometry','Number_Theory']:
        p=OUT/(subject+'_Research_Package')/'audit';(p/'Verification_Results.json').write_text(json.dumps(report,indent=2))
        import shutil
        shutil.copy2(__file__,p/'verify_subjects.py')
    (OUT/'subject_verification.json').write_text(json.dumps(report,indent=2))
