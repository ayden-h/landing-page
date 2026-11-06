"""Independent small-case checks of the theory; no network or third-party packages."""
from itertools import combinations, product, permutations
from math import comb, factorial, gcd
from pathlib import Path
import json

checks = []
def equal(label, actual, expected):
    assert actual == expected, (label, actual, expected)
    checks.append(label)

for n in range(1,11):
    for k in range(1,n+1):
        for d in range(3):
            actual=sum(all(b-a>=d+1 for a,b in zip(t,t[1:])) for t in combinations(range(n),k))
            expected=comb(n-d*(k-1),k) if n>=k+d*(k-1) else 0
            equal(f'linear gaps {n,k,d}',actual,expected)
            actual=sum(all((t[(i+1)%k]-t[i])%n>=d+1 for i in range(k)) for t in combinations(range(n),k)) if k>1 else (n if n>=d+1 else 0)
            expected=n*comb(n-d*k-1,k-1)//k if n>=(d+1)*k else 0
            equal(f'circular gaps {n,k,d}',actual,expected)

for n in range(1,10):
    actual=0
    for bits in product((0,1),repeat=n):
        chosen=[i+1 for i,b in enumerate(bits) if b][::-1]
        actual+=sum(x*(-1)**j for j,x in enumerate(chosen))
    equal(f'alternating subsets {n}',actual,n*2**(n-1))

for a in range(7):
    for b in range(7):
        for h in range(4):
            if b>a+h:continue
            actual=0
            for north in combinations(range(a+b),b):
                north=set(north);height=0;ok=True
                for i in range(a+b):
                    height+=1 if i in north else -1
                    if height>h:ok=False;break
                actual+=ok
            bad=comb(a+b,b-h-1) if b-h-1>=0 else 0
            equal(f'reflection {a,b,h}',actual,comb(a+b,b)-bad)

for n in range(1,9):
    seen=set()
    for w in product((0,1),repeat=n):
        seen.add(min(w[i:]+w[:i] for i in range(n)))
    equal(f'necklaces {n}',len(seen),sum(2**gcd(n,r) for r in range(n))//n)

actual=0
for p in permutations(range(6)):
    ok=True
    for a in range(6):
        b=a
        for _ in range(6):b=p[b]
        if b!=a:ok=False;break
    actual+=ok
equal('2026 I7 cycle inventory',actual,396)
equal('odd coefficients row 2026',sum(comb(2026,k)%2 for k in range(2027)),256)
equal('exercise 19',sum(sum(t)%2==0 and all(b-a>1 for a,b in zip(t,t[1:])) for t in combinations(range(1,21),5)),2184)

for q in range(2,12):
    for p in range(1,q):
        if gcd(p,q)>1:continue
        for n in range(20):
            actual=len({p*a+q*b for a in range(n+1) for b in range(n-a+1)})
            equal(f'two generators {p,q,n}',actual,sum(n-a+1 for a in range(min(q-1,n)+1)))

for n in range(2,5):
    total=0
    for arrows in product((0,1),repeat=n*n):
        v=(0,0);seen=set()
        for _ in range(n*n):
            if v in seen:break
            seen.add(v);x,y=v
            v=((x+1)%n,y) if arrows[x*n+y] else (x,(y+1)%n)
        if len(seen)==n*n and v==(0,0):total+=1
    equal(f'directed torus {n}',total,sum(comb(n,k) for k in range(n+1) if gcd(k,n)==1))

root=Path(__file__).resolve().parents[1]
report={'checks_passed':len(checks),'scope':'Finite small-case cross-checks, not a substitute for general proofs.','labels':checks}
(root/'data'/'theory_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'{len(checks)} exact theory checks passed')
