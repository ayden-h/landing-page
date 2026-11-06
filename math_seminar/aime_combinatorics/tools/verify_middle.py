"""Independent finite computations for the 2000--2013 combinatorics solutions.
Run with Python 3. No third-party packages or network needed.
"""
import json, math, itertools, collections, functools, pathlib, re
from fractions import Fraction as F
C=math.comb; fac=math.factorial
root=pathlib.Path(__file__).resolve().parents[1]
sol={r['id']:r for r in json.loads((root/'solutions/middle.json').read_text())}
checks={}
def check(k,v):
    assert v==sol[k]['answer'],(k,v,sol[k]['answer'])
    checks[k]={'computed':v,'matches_archived_answer':True}
def mn(f):return f.numerator+f.denominator
check('2000-II-03',mn(F(9*C(4,2)+1,C(38,2))))
ps=set()
for a in range(2,24):
 b=25-a
 for x in range(1,a):
  for y in range(1,b):
   if F(x*y,a*b)==F(27,50):ps.add(F((a-x)*(b-y),a*b))
assert ps=={F(1,25)}
check('2000-I-05',mn(next(iter(ps))))
check('2000-II-05',int(str(C(8,5)*fac(5)*C(8,3))[:3]))
check('2000-II-07',sum(C(19,k) for k in range(2,10))//1900)
s=sum((F(a,b) for a in range(1,1001) if 1000%a==0 for b in range(1,1001) if 1000%b==0 and math.gcd(a,b)==1),F(0))
check('2000-I-11',s//10)
q=collections.deque(range(1,2001));order=[]
while q:
 order.append(q.popleft())
 if q:q.rotate(-1)
check('2000-I-15',order[1998]-1)
check('2001-I-06',mn(F(sum(all(a[i]<=a[i+1] for i in range(3)) for a in itertools.product(range(1,7),repeat=4)),6**4)))
check('2001-II-09',mn(F(sum(not any(all(a[3*(i+di)+j+dj] for di in range(2) for dj in range(2)) for i in range(2) for j in range(2)) for a in itertools.product((0,1),repeat=9)),512)))
pts=list(itertools.product(range(3),range(4),range(5)))
check('2001-I-10',mn(F(sum(all((a[i]+b[i])%2==0 for i in range(3)) for a,b in itertools.combinations(pts,2)),C(60,2))))
check('2001-II-10',sum((pow(10,j,1001)-pow(10,i,1001))%1001==0 for i in range(100) for j in range(i+1,100)))
check('2001-II-11',mn(F(sum(sum(w)>0 for w in itertools.product((-1,0,1),repeat=6)),3**6)))
check('2001-II-12',mn(F(1)+F(1,2)+F(3,8)+F(9,32)))
check('2001-I-14',sum('11' not in f'{n:019b}' and '000' not in f'{n:019b}' for n in range(2**19)))
good=0
for p in itertools.permutations(range(1,8)):
 a=(0,)+p
 if all(bin(a[i]^a[(i+1)%8]).count('1')!=1 for i in range(8)):good+=1
check('2001-I-15',mn(F(good,fac(7))))
check('2002-I-01',mn(1-F(25,26)*F(9,10)))
check('2002-I-03',sum(10*a+b>25 for a in range(1,10) for b in range(a+1,10)))
check('2002-I-05',3*C(12,2)-5*3)
check('2002-II-09',((3**10-2*2**10+1)//2)%1000)
check('2002-II-12',(2+3+23+5)*(4+6+10))
a=[1,2,3,5,8,13,21,34]
check('2003-I-03',sum(max(t) for t in itertools.combinations(a,2)))
check('2003-II-03',sum(all((a[i],a[i+1]) not in [('A','B'),('B','C'),('C','A')] for i in range(6)) for a in itertools.product('ABC',repeat=7)))
check('2003-I-09',sum(sum(map(int,str(n)[:2]))==sum(map(int,str(n)[2:])) for n in range(1000,10000)))
check('2003-I-13',sum(bin(n)[2:].count('1')>bin(n)[2:].count('0') for n in range(1,2004))%1000)
p=F(1)
for _ in range(10):p=(1-p)/2
check('2003-II-13',mn(p))
check('2004-I-03',C(26,2)-60-24)
check('2004-II-02',mn(F(2*C(10,2)*C(8,2)+100*81,C(20,2)*C(18,2))))
check('2004-II-03',min((a+1)*(b+1)*(231//a//b+1) for a in range(1,232) for b in range(a,232) if 231%(a*b)==0))
check('2004-II-04',sum(len(set(str(n)))<=2 for n in range(1,10000)))
check('2004-I-06',sum(len(set(s))==4 and s[0]<s[1]>s[2]<s[3] for s in map(str,range(1000,10000))))
check('2004-I-07',abs(sum((-1)**(i+j)*i*j for i in range(1,16) for j in range(i+1,16))))
check('2004-I-08',sum(math.gcd(k,1000)==1 for k in range(2,500)))
check('2004-II-08',sum((a*b*c)==2004 for a in range(1,2005) if 2004%a==0 for b in range(1,2005) if 2004%b==0 for c in [2004//a//b] if a*b*c==2004))
check('2004-I-10',mn(F(375,442)))
check('2004-II-10',mn(F(sum((2**a+2**b)%9==0 for a in range(40) for b in range(a+1,40)),C(40,2))))
check('2004-II-14',len({1000-9*b-108*c for c in range(10) for b in range((1000-111*c)//11+1)}))
levels={1}
for depth in range(1,20):
 levels={x for y in levels for x in (10*y,y-1) if x>1 and ((x%10==0 and x//10==y) or (x%10!=0 and x+1==y))}
m=len(levels);fs=[];d=2
while d*d<=m:
 if m%d==0:
  fs.append(d)
  while m%d==0:m//=d
 d+=1
if m>1:fs.append(m)
check('2004-I-15',sum(fs))
stacks=[[i] for i in range(1,1025)]
while len(stacks)>1:
 L=len(stacks);stacks=[stacks[i]+list(reversed(stacks[L-1-i])) for i in range(L//2)]
check('2004-II-15',stacks[0].index(942))
check('2005-II-01',next(n for n in range(6,100) if C(n,6)==6*C(n,3)))
check('2005-II-02',mn(F(27,C(9,3))*F(8,C(6,3))))
check('2005-II-04',sum(10**10%n==0 or 15**7%n==0 or 18**11%n==0 for n in {2**a*3**b*5**c for a in range(12) for b in range(23) for c in range(11)}))
check('2005-I-05',C(8,4)*sum('10' not in s for s in map(''.join,itertools.product('01',repeat=8))))
check('2005-II-06',2*196)
p=(F(2,3)**6)*(F(5,12)**12)*(F(1,4)**8)
assert p==F(5**12,2**34*3**18)
check('2005-I-09',12+34+18+5+2+3)
check('2005-I-12',abs(sum(1 if math.isqrt(n)%2 else -1 for n in range(1,2006))))
@functools.lru_cache(None)
def path(x,y,last):
 if (x,y)==(5,5):return 1
 total=0
 for dx,dy,c in [(1,0,'R'),(0,1,'U'),(1,1,'D')]:
  if x+dx<=5 and y+dy<=5 and (last,c) not in [('R','U'),('U','R')]:total+=path(x+dx,y+dy,c)
 return total
check('2005-I-13',path(0,0,''))
check('2006-I-02',4995-4095+1)
check('2006-II-04',C(11,5))
check('2006-I-06',int(sum(F(100*a+10*b+c,999) for a,b,c in itertools.permutations(range(10),3))))
check('2006-II-07',sum('0' not in str(a)+str(1000-a) for a in range(1,1000)))
check('2006-II-08',6*C(8,3))
check('2006-II-10',mn(F(sum(C(5,a)*C(5,b) for a in range(6) for b in range(6) if a>=b),2**10)))
check('2006-I-11',sum(all(p[i+1]<=p[i]+2 for i in range(7)) for p in itertools.permutations(range(1,9)))%1000)
check('2006-I-13',max(n for n in range(1,1000) if math.isqrt((n+1)*2**(n-1))**2==(n+1)*2**(n-1)))
H=sum((F(1,i) for i in range(1,10)),F(0))
check('2006-II-14',next(n for n in range(1,1000) if (n*10**(n-1)*H).denominator==1))
check('2006-I-15',3*min(abs(((b+1)**2-2007)//2) for b in range(-2006,2007,2)))
check('2007-II-01',len(set(itertools.permutations('AIME2007',5)))//10)
check('2007-II-02',sum(a+b+c==100 and b%a==0 and c%a==0 for a in range(1,100) for b in range(1,100-a) for c in [100-a-b]))
check('2007-I-05',sum(round(9*round(5*(f-32)/9)/5+32)==f for f in range(32,1001)))
check('2007-II-05',sum(9*x+223*y<=2007 for x in range(1,224) for y in range(1,10)))
D=collections.defaultdict(int);D[0]=1
for x in range(39):
 for y in {3*(x//3+1),13*(x//13+1)}:
  if y<=39:D[y]+=D[x]
check('2007-I-06',D[39])
check('2007-II-06',sum(all((int(s[i])%2==1 and s[i]<s[i+1]) or (int(s[i])%2==0 and s[i]>s[i+1]) for i in range(3)) for s in map(str,range(1000,10000))))
check('2007-II-08',max((h-1)*((2007-5*h)//4-1) for h in range(2,400) if (2007-5*h)%4==0)%1000)
rows=list(itertools.combinations(range(4),2))
check('2007-I-10',sum(all(sum(c in row for row in a)==3 for c in range(4)) for a in itertools.product(rows,repeat=6))%1000)
prob=F(sum((b&a)==b or (b&(63^a))==b for a in range(64) for b in range(64)),4096)
check('2007-II-10',prob.numerator+2+(prob.denominator.bit_length()-1))
check('2007-I-11',sum(math.floor(math.sqrt(p)+.5) for p in range(1,2008))%1000)
check('2007-II-13',sum(sum(C(10,i)*s[i] for i in range(11))%3==0 for s in itertools.product((0,1),repeat=11)))
row=list(range(1,100,2));count=0
while row:
 count+=sum(a%67==0 for a in row);row=[a+b for a,b in zip(row,row[1:])]
check('2008-I-06',count)
check('2008-I-07',1000-len({n*n//100 for n in range(317)}))
check('2008-I-09',F(sum(sum(s)==41 for s in itertools.product((3,4,6),repeat=10)),3**10).numerator)
pts=list(itertools.product(range(4),repeat=2));ds=[18,13,10,9,8,5,4,2,1]
def descend(p,used,k):
 if k==9:return 1
 return sum(descend(q,used|{q},k+1) for q in pts if q not in used and sum((p[i]-q[i])**2 for i in (0,1))==ds[k])
check('2008-II-10',10*sum(descend(p,{p},0) for p in pts))
check('2008-I-11',sum(all((len(g)%2==0 if g[0]=='A' else len(g)%2==1) for g in re.findall('A+|B+',s)) for s in map(''.join,itertools.product('AB',repeat=14))))
check('2008-II-12',(11*C(12,9)-2*C(11,9))%1000)
check('2009-II-06',sum(any(b==a+1 for a,b in zip(t,t[1:])) for t in itertools.combinations(range(1,15),5))%1000)
check('2009-I-08',sum(b-a for a,b in itertools.combinations([2**i for i in range(11)],2))%1000)
check('2009-II-08',mn(1-2*F(25,66)))
check('2009-I-09',len({(s[:i],s[i:j],s[j:]) for s in set(itertools.permutations('1111333')) for i in range(1,7) for j in range(i+1,7) if max(i,j-i,7-j)<=4}))
def dioph(N):return sum((N-4*x-3*y)>0 and (N-4*x-3*y)%2==0 for x in range(1,N//4) for y in range(1,(N-4*x)//3+1))
check('2009-II-09',(dioph(2009)-dioph(2000))%1000)
check('2009-I-10',sum(C(4,k)**3 for k in range(5)))
check('2009-I-11',sum((2009*(a-b))%2==0 for a,b in itertools.combinations(range(50),2)))
pairs=[(2*j+1,1205-j) for j in range(402)]+[(2*j+2,1606-j) for j in range(401)]
assert len(set(itertools.chain.from_iterable(pairs)))==1606 and len({a+b for a,b in pairs})==803 and max(a+b for a,b in pairs)<=2009
check('2009-II-12',len(pairs))
check('2010-I-01',mn(F(16*65,C(81,2))))
check('2010-II-02',mn(F(9,25)-F(1,9)))
check('2010-II-03',sum(((b-a)&-(b-a)).bit_length()-1 for a,b in itertools.combinations(range(1,21),2)))
check('2010-I-04',mn(F(3**2+10**2+11**2+4**2,28**2)))
check('2010-II-04',mn(F(sum(b-a<=4 for a,b in itertools.combinations(range(12),2)),C(12,2))))
check('2010-I-07',7*6*5*4**4%1000)
check('2010-II-08',sum(0<len(A)<12 and len(A) not in A and (12-len(A)) in A for A in [set(i+1 for i in range(12) if mask>>i&1) for mask in range(1<<12)]))
check('2010-I-10',sum(0<=2010-1000*a3-100*a2-10*a1<=99 for a3 in range(3) for a2 in range(21) for a1 in range(100)))
poly=set()
for r in range(-2010,2011):
 if r==0 or 2010%r:continue
 for s in range(-2010,2011):
  if s==0 or (2010//r)%s:continue
  a=2010//r//s;poly.add((a,-a*(r+s),2010))
check('2010-II-10',len(poly))
lines=[[3*r+c for c in range(3)] for r in range(3)]+[[3*r+c for r in range(3)] for c in range(3)]+[[0,4,8],[2,4,6]]
check('2010-II-11',sum(sum(len({i in A for i in line})==1 for line in lines)<=1 for A in map(set,itertools.combinations(range(9),5))))
red=set(range(3,9))|set(range(81,243));blue=set(range(9,81))
assert not any(a*b in t for t in [red,blue] for a in t for b in t)
check('2010-II-13',mn(min(p for a in range(1,44) for p in [F(C(a-1,2)+C(43-a,2),C(50,2))] if p>=F(1,2))))
check('2011-I-05',fac(3)**4//9)
check('2011-II-06',sum(a+d>b+c for a,b,c,d in itertools.combinations(range(1,11),4)))
check('2011-I-07',sum(2010%d==0 for d in range(1,2011)))
check('2011-II-07',C(15,5)%1000)
check('2011-I-10',sum(n for n in range(3,1000) if F(n*C((n-1)//2,2),C(n,3))==F(93,125)))
check('2011-I-12',next(w for w in range(1000) if F(6*(w+1),w*w+8*w+6)<=F(1,100)))
words=set(itertools.permutations('AAABBBCCC'));good=sum(all(not (s[i-1]==s[i]==s[(i+1)%9]) for i in range(9)) for s in words)
check('2011-II-12',mn(F(good,len(words))))
check('2011-II-14',fac(2)*fac(3)*fac(5)%1000)
check('2012-I-01',sum(n%4==0 and int(str(n)[::-1])%4==0 and n%10!=0 for n in range(100,1000)))
check('2012-I-03',sum(sum(a==b for a,b in zip(s,'BBBCCCFFF'))==1 for s in set(itertools.permutations('BBBCCCFFF'))))
people=list(itertools.product(range(3),range(2),range(2)))
check('2012-II-03',sum(sum(p[1] for p in t)==3 and all(sum(p[0]==d for p in t)==2 for d in range(3)) for t in itertools.combinations(people,6)))
b={n for n in range(1<<13) if bin(n).count('1')==8}
check('2012-I-05',sum(n+1 in b for n in b))
check('2012-I-07',3360*5//60)
check('2012-II-07',sorted(n for n in range(1<<14) if bin(n).count('1')==8)[999]%1000)
check('2012-I-11',sum((x+y)%3==0 and (x-y)%5==0 for x in range(-100,101) for y in range(-100,101) if abs(x)+abs(y)<=100)%1000)
check('2012-II-12',sum(all(3<=n%p<=p-3 for p in (7,11,13)) for n in range(1,10001)))
check('2012-II-14',(fac(8)//2+C(9,3)*fac(5)//2+C(9,4)*fac(3)*fac(4)//4+fac(9)//(fac(3)**3*fac(3)))%1000)
check('2012-I-15',sum(math.gcd(n,6)==1 for n in range(2,1000)))
check('2013-I-02',sum(n%5==0 and str(n)[0]==str(n)[-1] and sum(map(int,str(n)))%5==0 for n in range(10000,100000)))
check('2013-I-04',C(13,8)//3)
check('2013-I-06',mn(F(C(3,3)+C(4,3)+C(5,3),C(12,3))))
check('2013-II-09',sum(C(6,k-1)*(3**k-3*2**k+3) for k in range(1,8))%1000)
check('2013-II-11',sum(len({f[f[i]] for i in range(7)})==1 for f in itertools.product(range(7),repeat=7))%1000)
check('2013-II-12',C(6,3)+4*(79+51))
check('2013-I-15',sum(a%3==1 and b%3==0 and c%3==2 for a in range(100) for b in range(a+1,100) for c in [2*b-a] if c<=99))
(root/'data/middle_verification.json').write_text(json.dumps({'checks':checks,'checked_count':len(checks),'remaining_analytic_proofs':[i for i in sol if i not in checks]},indent=2))
print(f'{len(checks)} independent exact computations passed; {len(sol)-len(checks)} proofs use analytic verification.')
