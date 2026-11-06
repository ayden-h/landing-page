"""Exact finite checks for newly included early-era solutions; standard library only."""
import json
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
results=[]
def check(id,computed,expected,method):
    assert computed==expected,(id,computed,expected)
    results.append(dict(id=id,result=str(computed),expected=str(expected),passed=True,method=method))

check('1983-A-06',(pow(6,83,49)+pow(8,83,49))%49,35,'Independent modular exponentiation.')
prime=lambda n:n>1 and all(n%d for d in range(2,isqrt(n)+1))
check('1983-A-08',max(p for p in range(10,100) if prime(p) and comb(200,100)%p==0),61,'Form the exact binomial integer and test all two-digit primes.')
good=[]
for a in range(1,10):
    for b in range(10):
        diameter=10*a+b; chord=10*b+a; rad=diameter**2-chord**2
        if rad>0 and isqrt(rad)**2==rad:good.append(diameter)
check('1983-A-12',good,[65],'Exhaust all90 digit pairs and test the squared chord-distance difference.')
numbers=[int(''.join(ds)) for k in range(1,5) for ds in product('08',repeat=k) if ds[0]!='0']
check('1984-A-02',min(n for n in numbers if n%15==0)//15,592,'Exhaust all admissible numerals through four digits.')
@lru_cache(None)
def nested(n):return n-3 if n>=1000 else nested(nested(n+5))
check('1984-A-07',nested(84),997,'Evaluate the nested definition directly with memoization.')
odd_composites=[n for n in range(3,1001,2) if not prime(n)]
representable={a+b for a in odd_composites for b in odd_composites if a+b<=1000}
check('1984-A-14',max(n for n in range(2,1001,2) if n not in representable),38,'Enumerate all odd-composite sums through1000; the proof handles the infinite tail.')
matrix=[[Q(1,t-a) for a in [1,9,25,49]]+[Q(1)] for t in [4,16,36,64]]
for j in range(4):
    pivot=matrix[j][j]; matrix[j]=[x/pivot for x in matrix[j]]
    for i in range(4):
        if i!=j:
            factor=matrix[i][j]; matrix[i]=[a-factor*b for a,b in zip(matrix[i],matrix[j])]
check('1984-A-15',sum(row[-1] for row in matrix),Q(36),'Exact rational Gaussian elimination, independent of coefficient extraction.')
sol=[(a,b,a**3-3*a*b*b) for b in [1,107] for a in range(1,108) if b*(3*a*a-b*b)==107 and a**3-3*a*b*b>0]
check('1985-A-03',sol,[(6,1,198)],'Enumerate the prime-divisor cases and all possible positive a in their bounds.')
seq=[-999,493]
while len(seq)<2001:seq.append(seq[-1]-seq[-2])
check('1985-A-05',(sum(seq[:1492]),sum(seq[:1985]),sum(seq)),(1985,1492,986),'Generate all2001 recurrence terms directly and sum three prefixes.')
def area(a,b,c):return abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
A=(Q(0),Q(0));B=(Q(7),Q(0));C=(Q(4),Q(90));P=(Q(4),Q(20));D=(Q(6),Q(30));E=(Q(8,5),Q(36));F=(Q(4),Q(0))
check('1985-A-06',tuple(area(*v) for v in [(A,P,F),(B,P,F),(B,P,D),(C,P,E),(A,P,E),(C,P,D),(A,B,C)]),tuple(map(Q,[40,30,35,84,56,70,315])),'Construct rational coordinates realizing all givens; determinant areas verify the unknown regions.')
check('1985-A-13',max(gcd(n*n+100,(n+1)**2+100) for n in range(1,803)),401,'Direct gcd values across two complete401-residue periods.')
check('1986-A-05',max(n for n in range(1,901) if (n**3+100)%(n+10)==0),890,'Direct division for every n up to the proven divisor bound.')
check('1986-A-06',[(n,1986-n*(n+1)//2) for n in range(1,64) if 1<=1986-n*(n+1)//2<=n],[(62,33)],'Exhaust all feasible page counts below the triangular-sum bound.')
nice=[]
for n in range(2,34):
    ds=[d for d in range(2,n) if n%d==0]
    if prod(ds)==n:nice.append(n)
check('1987-A-03',(nice,sum(nice)),([6,8,10,14,15,21,22,26,27,33],182),'Directly multiply all distinct proper divisors through the tenth nice number.')
vals={(x*x,y*y,3*x*x*y*y) for x in range(-12,13) for y in range(-22,23) if y*y+3*x*x*y*y==30*x*x+517}
check('1987-A-05',sorted(vals),[(4,49,588)],'Enumerate all integer pairs within the bounds supplied by the positive factorization.')
N=3**11; lengths=[]
for k in range(1,isqrt(2*N)+1):
    if 2*N%k==0:
        twice_a=2*N//k-k+1
        if twice_a>=2 and twice_a%2==0:lengths.append(k)
check('1987-A-11',max(lengths),486,'Enumerate every feasible length below the positive-sum bound.')
num=prod((10+12*j)**4+324 for j in range(5));den=prod((4+12*j)**4+324 for j in range(5))
check('1987-A-14',Q(num,den),Q(373),'Form the exact large numerator and denominator, then reduce.')
s=462;p=21*s;c2=s*s-2*p
check('1987-A-15',(Q(p*p,s*s),Q(p*p*c2,(c2+p)**2)),(Q(441),Q(440)),'Verify both square-area equations with exact rational symmetric data.')
grid=[[50*i+13*j-5*i*j for i in range(5)] for j in range(5)]
assert all(len({row[i+1]-row[i] for i in range(4)})==1 for row in grid)
assert all(len({grid[j+1][i]-grid[j][i] for j in range(4)})==1 for i in range(5))
check('1988-A-06',(grid[3][1],grid[2][4],grid[1][2],grid[4][3]),(74,186,103,142),'Construct all25 cells and verify every row and column difference.')
check('1988-A-09',[n for n in range(1,1000) if n**3%1000==888],[192,442,692,942],'Exhaust all residues modulo1000 directly.')
poly=[0]*18;poly[0]=1;poly[16]=-1597;poly[17]=987
for degree in range(17,1,-1):
    coef=poly[degree];poly[degree]=0;poly[degree-1]+=coef;poly[degree-2]+=coef
check('1988-A-13',poly,[0]*18,'Perform exact polynomial long division instead of using the Fibonacci formula.')

check('1989-A-03',[(d,n) for d in range(10) for n in range(1,811) if Q(n,810)==Q(100*d+25,999)],[(9,750)],'Exhaust the digit and numerator ranges with exact fractions.')
check('1989-A-04',min(c for c in range(3,676) if isqrt(3*c)**2==3*c and any(k**3==5*c for k in range(1,16))),675,'Exhaust every possible smaller middle term and test square/cube conditions.')
check('1989-A-09',sum(n**5 for n in [133,110,84,27]),144**5,'Compute the fifth-power equation as exact integers.')
complex_reals=set()
for a3 in range(1,10):
    for a2,a1,a0 in product(range(10),repeat=3):
        if 26*a3-6*a2+a1==0:complex_reals.add(-18*a3+8*a2-3*a1+a0)
check('1989-A-14',(len(complex_reals),sum(complex_reals)),(20,490),'Enumerate every four-digit complex-base numeral using integer real/imaginary components.')
divisor_count=lambda n:sum(2 if d*d!=n else 1 for d in range(1,isqrt(n)+1) if n%d==0)
check('1990-A-05',min(n for n in range(75,32401,75) if divisor_count(n)==75)//75,432,'Test every eligible multiple up to the proposed global minimum directly.')
check('1990-A-10',len({(8*a+3*b)%144 for a in range(18) for b in range(48)}),144,'Enumerate all864 root-product exponents, independently checking the image size.')
valid=[]
for n in range(4,101):
    target=prod(range(1,n+1));start=1
    while True:
        value=prod(range(start,start+n-3))
        if value>=target:
            if value==target:valid.append(n)
            break
        start+=1
check('1990-A-11',max(valid),23,'Exhaust consecutive blocks for every n from4 through100; proof controls the infinite tail.')
check('1991-A-01',[(x,y,x*x+y*y) for x in range(1,72) for y in range(x,72) if x*y+x+y==71 and x*y*(x+y)==880],[(5,11,146)],'Exhaust positive integer pairs within the first-equation bound.')
check('1991-A-03',max(range(1001),key=lambda k:comb(1000,k)*5**(1000-k)),166,'Compare all1001 weighted binomial terms after multiplying by the common denominator5^1000.')
parameters={-(r+t) for r in range(-42,31) for t in range(r,31) if r*t==-6*(r+t)}
check('1991-A-08',(len(parameters),sorted(parameters)),(10,[-25,-8,-3,-1,0,24,25,27,32,49]),'Enumerate all shifted-factor-bounded integer root pairs and distinct parameters.')
check('1992-A-01',sum(Q(k,30) for k in range(1,300) if gcd(k,30)==1),Q(400),'Direct exact sum over all reduced numerators.')
triples=[]
for n in range(2,101):
    for k in range(1,n):
        u,v,w=comb(n,k-1),comb(n,k),comb(n,k+1)
        if 4*u==3*v and 5*v==4*w:triples.append((n,k))
check('1992-A-04',triples,[(62,27)],'Compare exact adjacent binomial integers in the first101 rows.')
check('1993-A-06',min(n for n in range(1,496) if all((n-k*(k-1)//2)%k==0 for k in [9,10,11])),495,'Test the arithmetic-series starting-term integrality for every smaller positive target.')
check('1993-A-09',[n for n in range(1,1994) if (n*(n+1)-1993*1994)%4000==0],[118,1993],'Enumerate all labels and compare their cumulative step residues.')
check('1994-A-01',[n*n-1 for n in range(2,3000) if (n*n-1)%3==0][1993]%1000,63,'Construct the actual increasing sequence through its1994th term.')
check('1994-A-04',sum(k.bit_length()-1 for k in range(1,313)),1994,'Compute each logarithm floor independently by integer bit length.')
# Verify the fold-point locus by direct intersections of all three crease pairs.
def solve2(a,b,c,d,e,f):
    det=a*d-b*c
    return ((e*d-b*f)/det,(a*f-e*c)/det)
def on_paper(p):return p[0]>=0 and p[1]>=0 and p[0]/3+p[1]/4<=1
fold_cases=0
vertices=[(Q(0),Q(0)),(Q(3),Q(0)),(Q(0),Q(4))]
for i in range(1,60):
    for j in range(1,80):
        x,y=Q(i,20),Q(j,20)
        if x/3+y/4>=1:continue
        creases=[(2*(x-vx),2*(y-vy),x*x+y*y-vx*vx-vy*vy) for vx,vy in vertices]
        intersections=[]
        for a,b in [(0,1),(1,2),(0,2)]:
            u,v,w=creases[a];q,r,t=creases[b]
            intersections.append(solve2(u,v,q,r,w,t))
        directly_valid=not any(on_paper(p) for p in intersections)
        lens_valid=x*x+y*y<3*x and x*x+y*y<4*y
        assert directly_valid==lens_valid,(x,y,intersections)
        fold_cases+=1
check('1994-A-15',fold_cases,2321,'Exact rational crease-intersection tests at every interior point of a1/20 grid in a3–4–5 triangle.')
check('1995-A-10',max(n for n in range(1,1001) if not any(n-42*j>1 and not prime(n-42*j) for j in range(1,(n-1)//42+1))),215,'Test every candidate through1000 directly for a positive composite remainder.')
def nearest_fourth(n):
    j=0
    while (2*j+1)**4<16*n:j+=1
    return j
check('1995-A-13',sum(Q(1,nearest_fourth(k)) for k in range(1,1996)),Q(400),'Find each nearest fourth root by exact integer midpoint comparisons, then sum individually.')
check('1997-A-03',[(x,y) for x in range(10,100) for y in range(100,1000) if 1000*x+y==9*x*y],[(14,112)],'Exhaust all two-digit and three-digit factor pairs.')
check('1997-A-06',max(n for n in range(7,201) for m in range(7,201) if Q(1,m)+Q(1,n)==Q(1,6)),42,'Enumerate integer polygon angle compatibilities over the proven relevant range.')
def sequence_length(x):
    a,b=1000,x;length=2
    while b>=0:
        a,b=b,a-b;length+=1
    return length
lengths=[sequence_length(x) for x in range(1,1001)]
check('1998-A-08',(max(lengths),[x for x in range(1,1001) if lengths[x-1]==max(lengths)]),(14,[618]),'Generate every subtractive sequence for1≤x≤1000; x>1000 stops immediately at term3.')
hexagon=[(5,0,0),(20,0,15),(20,10,20),(15,20,20),(0,20,5),(0,10,0)]
normal=[0,0,0]
for a,b in zip(hexagon,hexagon[1:]+hexagon[:1]):
    normal[0]+=a[1]*b[2]-a[2]*b[1]
    normal[1]+=a[2]*b[0]-a[0]*b[2]
    normal[2]+=a[0]*b[1]-a[1]*b[0]
check('1998-A-11',sum(v*v for v in normal)//4,525**2,'Compute the section area squared from the six spatial vertices by the vector polygon-area formula.')
box_solutions=[]
for m in range(1,21):
    for n in range(m,131):
        den=2*m*n-(m+2)*(n+2);num=2*(m+2)*(n+2)
        if den>0 and num%den==0 and num//den>=n:box_solutions.append((m,n,num//den))
check('1998-A-14',max(p for m,n,p in box_solutions),130,'Enumerate ordered integral dimension pairs within the analytic bound and solve exactly for the third.')
prime_progressions=[(p,d,p+4*d) for p in range(2,30) for d in range(1,30) if all(prime(p+j*d) for j in range(5))]
check('1999-A-01',min(v for p,d,v in prime_progressions),29,'Exhaust all progressions that could improve the proposed fifth prime.')
check('1999-A-03',[n for n in range(1,101) if isqrt(n*n-19*n+99)**2==n*n-19*n+99],[1,9,10,18],'Direct square test through100; factorization proves no later solutions.')
# Cayley–Menger uses only edge lengths, independently of the apex coordinates.
def determinant(matrix):
    mat=[[Q(x) for x in row] for row in matrix];value=Q(1);n=len(mat)
    for j in range(n):
        pivot=next((i for i in range(j,n) if mat[i][j]),None)
        if pivot is None:return Q(0)
        if pivot!=j:mat[j],mat[pivot]=mat[pivot],mat[j];value=-value
        p=mat[j][j];value*=p
        for i in range(j+1,n):
            factor=mat[i][j]/p
            for k in range(j,n):mat[i][k]-=factor*mat[j][k]
    return value
CM=[[0,1,1,1,1],[1,0,225,208,289],[1,225,0,289,208],[1,208,289,0,225],[1,289,208,225,0]]
check('1999-A-15',determinant(CM)/288,Q(408**2),'Independent Cayley–Menger determinant from the six preserved edge lengths.')

(ROOT/'checks/early_expanded_exact_results.json').write_text(json.dumps(results,indent=2)+'\n')
print(f'{len(results)} expanded early checks passed.')
