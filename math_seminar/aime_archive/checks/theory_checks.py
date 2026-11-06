"""Finite exact checks of book identities and exercises; these supplement the proofs.

Only Python's standard library is required. Finite checks do not establish the
universal theorems, whose hypotheses and proofs appear in the theory volumes.
"""
from fractions import Fraction as F
from math import gcd, comb, factorial, isqrt
from collections import Counter
from pathlib import Path
import json

counts=Counter()
def check(subject,name,condition):
    assert condition,(subject,name)
    counts[(subject,name)]+=1

def factor(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out

def valuation(n,p):
    assert n
    n=abs(n);s=0
    while n%p==0:s+=1;n//=p
    return s

def tau(n):
    out=1
    for e in factor(n).values():out*=e+1
    return out

def norm2(v):return sum(x*x for x in v)
def sub(u,v):return tuple(a-b for a,b in zip(u,v))
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def cross(u,v):return u[0]*v[1]-u[1]*v[0]

# Number theory: direct enumeration versus structural counts.
for c in range(15):
    for n in range(1,61):check('number_theory','neighboring quadratic gcd',gcd(n*n+c,(n+1)**2+c)==gcd(4*c+1,2*n+1))
for m in range(2,161):
    check('number_theory','CRT idempotent count',sum((x*x-x)%m==0 for x in range(m))==2**len(factor(m)))
for a in range(1,8):
    m=2**a
    check('number_theory','two-power square roots',sum((x*x-1)%m==0 for x in range(m))==(1 if a==1 else 2 if a==2 else 4))
for m in range(1,25):
    for n in range(1,25):
        check('number_theory','exponential gcd parity criterion',(gcd(2**m+1,2**n-1)>1)==(valuation(n,2)>valuation(m,2)))
for p in (3,5,7):
    for b in range(1,12):
        if b%p==0:continue
        for h in range(1,5):
            a=b+p*h
            for n in range(1,16):
                check('number_theory','odd-prime exponent lifting',valuation(a**n-b**n,p)==valuation(a-b,p)+valuation(n,p))
for a in range(3,16,2):
    for b in range(1,a,2):
        for n in range(1,17):
            expected=valuation(a-b,2) if n%2 else valuation(a-b,2)+valuation(a+b,2)+valuation(n,2)-1
            check('number_theory','two-adic exponent lifting',valuation(a**n-b**n,2)==expected)
for n in range(1,101):
    check('number_theory','binary Lucas count',sum(comb(n,k)%2 for k in range(n+1))==2**bin(n).count('1'))
    r=isqrt(n)
    check('number_theory','hyperbola count',sum(n//k for k in range(1,n+1))==2*sum(n//k for k in range(1,r+1))-r*r)
for D in range(1,81):
    actual={n//gcd(n,D) for n in range(1,D+1)};pred=set()
    for u in range(1,D+1):
        bound=1
        for p,e in factor(D).items():
            if u%p:bound*=p**e
        if u<=bound:pred.add(u)
    check('number_theory','reduced numerator feasibility',actual==pred)
for a in range(2,15):
    for b in range(a+1,18):
        if gcd(a,b)>1:continue
        threshold=a*b-a-b
        representable={a*x+b*y for x in range(2*b+1) for y in range(2*a+1)}
        check('number_theory','Frobenius boundary',threshold not in representable and all(n in representable for n in range(threshold+1,threshold+a*b+1)))
for N in range(1,101):
    actual={k for k in range(1,N+1) for a in range(1,N+1) if k*(2*a+k-1)==2*N}
    predicted={k for k in range(1,2*N+1) if 2*N%k==0 and (q:=2*N//k)>=k+1 and (k+q)%2==1}
    check('number_theory','positive consecutive-sum lengths',actual==predicted)
check('number_theory','exercise 24 minimal divisor count',next(n for n in range(1,200) if tau(n)==18)==180)
check('number_theory','exercise 13 trailing base-twelve zeros',min(valuation(factorial(100),2)//2,valuation(factorial(100),3))==48)
check('number_theory','exercise 23 floor sum',sum(20//k for k in range(1,21))==66)
for a in range(2,5):
    n=factorial(a+1)-1
    prod=1
    for x in range(a+2,n+2):prod*=x
    check('number_theory','short factorial block attainment',prod==factorial(n))

# Algebra: exact rational samples, retaining exceptional branches.
for x in range(-5,6):
    for y in range(-5,6):
        s=x+y;A=x*x+y*y;B=x**3+y**3
        check('algebra','power-sum elimination',s**3-3*A*s+2*B==0 and 2*A-s*s==(x-y)**2)
        for z in (-3,0,4):
            check('algebra','cubic symmetric factorization',2*(x**3+y**3+z**3-3*x*y*z)==(x+y+z)*((x-y)**2+(y-z)**2+(z-x)**2))
for a in range(-3,4):
    for b in range(a+1,5):
        for w,v in ((1,2),(-2,3),(3,-1)):
            T=[w*a**k+v*b**k for k in range(7)];D=T[0]*T[2]-T[1]**2
            s=F(T[0]*T[3]-T[1]*T[2],D);p=F(T[1]*T[3]-T[2]**2,D)
            check('algebra','weighted moment recurrence',s==a+b and p==a*b and all(T[k+2]==s*T[k+1]-p*T[k] for k in range(5)))
for n in range(1,31):
    for t in (F(1,3),F(1,2),F(1),F(2),F(5,2)):
        terms=[comb(n,k)*t**k for k in range(n+1)];mx=max(terms)
        actual=[k for k,v in enumerate(terms) if v==mx];q=(n+1)*t/(1+t)
        expected=[int(q)-1,int(q)] if q.denominator==1 else [q.numerator//q.denominator]
        check('algebra','weighted binomial modes',actual==expected)
for m in range(1,16):
    for n in range(1,16):
        c=Counter((F(a,m)+F(b,n))%1 for a in range(m) for b in range(n))
        check('algebra','root-set product fibers',len(c)==m*n//gcd(m,n) and set(c.values())=={gcd(m,n)})
x=F(0)
for n in range(1,21):
    x=(2*x+1)/(x+2)
    check('algebra','fractional-linear iteration',x==F(3**n-1,3**n+1))
for d in range(2,8):
    for e in range(d+1,9):
        for n in range(-20,21):
            target=(n//d,n//e)
            singleton=all((k//d,k//e)!=target for k in (n-1,n+1))
            predicted=(n%d==0 or n%e==0) and ((n+1)%d==0 or (n+1)%e==0)
            check('algebra','singleton floor fibers',singleton==predicted)
check('algebra','exercise 14 singleton count',sum((n%3==0 or n%4==0) and ((n+1)%3==0 or (n+1)%4==0) for n in range(1,61))==10)

# Geometry: independently construct rational configurations and compare identities.
for u in range(-2,5):
    for v in range(1,5):
        A=(F(u),F(v));B=(F(0),F(0));C=(F(6),F(0))
        a2=norm2(sub(B,C));b2=norm2(sub(C,A));c2=norm2(sub(A,B))
        for m in range(1,6):
            n=6-m;D=(F(m),F(0));d2=norm2(sub(A,D))
            check('geometry','Stewart on rational triangles',b2*m+c2*n==6*(d2+m*n))
        for weights in ((1,1,1),(2,3,5),(-1,2,3)):
            alpha,beta,gamma=map(F,weights);s=alpha+beta+gamma
            X=tuple((alpha*A[i]+beta*B[i]+gamma*C[i])/s for i in (0,1));P=(F(3,2),F(-1,3))
            left=norm2(sub(X,P))
            right=(alpha*norm2(sub(A,P))+beta*norm2(sub(B,P))+gamma*norm2(sub(C,P)))/s-(beta*gamma*a2+gamma*alpha*b2+alpha*beta*c2)/s**2
            check('geometry','weighted squared-distance identity',left==right)
for a in range(1,7):
    for b in range(a+1,10):
        for t in (F(1,4),F(1,2),F(3,4)):
            x=a+(b-a)*t
            check('geometry','trapezoid section area coordinate',(a+x)*t/(a+b)==(x*x-a*a)/F(b*b-a*a))
for P in ((F(1),F(2)),(F(-3),F(1)),(F(4),F(0))):
    for Q in ((F(2),F(5)),(F(-1),F(-1))):
        Pi=tuple(4*x/norm2(P) for x in P);Qi=tuple(4*x/norm2(Q) for x in Q)
        check('geometry','inversion distance transformation',norm2(sub(Pi,Qi))==16*norm2(sub(P,Q))/(norm2(P)*norm2(Q)))
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                # Two perpendicular diagonals; the common sine factor is one.
                check('geometry','opposite-area balance',(a*b+c*d==b*c+d*a)==(a==c or b==d))
check('geometry','exercise 9 cyclic area',7*6*5*4==4*210)
check('geometry','exercise 17 tetrahedron face',20**2+15**2+12**2==769)

report={'purpose':'Finite exact checks supplement, and do not replace, written proofs. Counts are parameter cases, not separate theorems.',
        'total_cases':sum(counts.values()),'subjects':{}}
for subject in ('geometry','algebra','number_theory'):
    checks={name:n for (s,name),n in counts.items() if s==subject}
    report['subjects'][subject]={'cases':sum(checks.values()),'checks':checks}
root=Path(__file__).resolve().parents[1]
(root/'data/theory_check_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
