"""Independent finite and exact checks for authored2014–2021 solutions.
These checks supplement, and do not replace, the proofs in solutions/recent.json.
"""
from fractions import Fraction as F
from math import gcd,isqrt,sqrt,sin,cos,asin,pi
from itertools import combinations
import json
from pathlib import Path
checks=[]
def check(id,description,actual,expected):
 assert actual==expected,(id,actual,expected)
 checks.append(dict(id=id,check=description,result='passed',value=str(actual)))
check('2014-I-03','Enumerate all499 possible numerators',sum(gcd(a,1000)==1 for a in range(1,500)),200)
check('2014-I-08','Exhaust all four-digit residues satisfying idempotence',[a for a in range(1000,10000) if (a*a-a)%10000==0],[9376])
check('2014-II-04','Exhaust the digit equation',[(a,b,c) for a in range(1,10) for b in range(10) for c in range(10) if F(10*a+b,99)+F(100*a+10*b+c,999)==F(33,37)],[(4,4,7)])
def ds(n):return sum(map(int,str(n)))
check('2015-I-08','Exhaust all smaller candidates and verify first witness',next(n for n in range(1,1000) if ds(n)==ds(n+864)==20),695)
check('2015-I-10','Enumerate equal-sum root triples',list(combinations([1,2,3,5,6,7],3)) and [t for t in combinations([1,2,3,5,6,7],3) if sum(t)==12],[(1,5,6),(2,3,7)])
check('2015-I-11','Exact four-case integer test',[(b,F(64*b,b*b-128)) for b in range(12,16) if F(64*b,b*b-128).denominator==1],[(12,F(48))])
check('2015-II-03','Exhaust smaller multiples of17',next(n for n in range(17,1000,17) if ds(n)==17),476)
check('2015-II-06','Exhaust positive ordered square triples',[(a,b,c) for a in range(1,10) for b in range(a,10) for c in range(b,10) if a*a+b*b+c*c==81],[(1,4,8),(3,6,6),(4,4,7)])
check('2015-II-08','Exact bounded objective comparison',max(F(a**3*b**3+1,a**3+b**3) for a in range(1,21) for b in range(1,21) if F(a*b+1,a+b)<F(3,2)),F(31,5))
vals=[sum(sin(k) for k in range(1,n+1)) for n in range(1,630)]
check('2015-II-13','Numerical sine sums locate the hundredth negative partial sum',[n+1 for n,v in enumerate(vals) if v<0][99],628)
B=(F(-8,5),F(-4,5));D=(F(-8,13),F(12,13))
check('2015-II-15','Exact determinant of the constructed triangle',abs(B[0]*D[1]-B[1]*D[0])/2,F(64,65))
check('2016-I-05','Exhaust all feasible positive day counts',[(k,(748//k-k+1)//2,(638//k-k+1)//2) for k in range(2,26) if 748%k==638%k==0 and (748//k-k+1)%2==(638//k-k+1)%2==0 and 638//k-k+1>0],[(11,29,24)])
A=asin(.2);t=31/(200-62*sqrt(6));theta=__import__('math').atan(t)
literal=1600*t/(1+t*t);radical=248*(1600-496*sqrt(6))/(2561-992*sqrt(6))
assert abs(literal-radical)<1e-9
assert 40*sin((pi/2-A)/2)>31*sin((pi/2-A)/2+A)
assert abs(40*sin(theta)-31*sin(theta+A))<1e-10
checks.append(dict(id='2016-I-09',check='Numerically verify both exact boundary formulas, boundary incidence, and failure of the intended equality configuration',result='passed',value=literal))
seq=[]
for k in range(31):seq.extend([14*(6+k)**2,14*(6+k)*(7+k)])
assert all(seq[k]<seq[k+1] for k in range(len(seq)-1))
assert all(seq[2*k+1]**2==seq[2*k]*seq[2*k+2] and seq[2*k+1]+seq[2*k+3]==2*seq[2*k+2] for k in range(30))
check('2016-I-10','Check geometric/arithmetic identities through62 terms and specified thirteenth term',seq[12],2016)
def omega(n):
 s=0;p=2
 while p*p<=n:
  while n%p==0:s+=1;n//=p
  p+=1
 return s+(n>1)
check('2016-I-12','Factor every candidate up to the claimed first value',next(m for m in range(1,133) if omega(m*m-m+11)>=4),132)
check('2016-II-07','Exhaust all possible integer middle areas',[min([m for m in range(1008,2016) if m*m%2016==0]),max([m for m in range(1008,2016) if m*m%2016==0])],[1008,1848])
check('2016-II-09','Exhaust all bases and exponents allowed by neighboring sums',[(r,k,d) for r in range(2,10) for k in range(3,11) for d in range(1,100) if 1+(k-2)*d+r**(k-2)==100 and 1+k*d+r**k==1000],[(9,3,90)])
check('2017-I-05','Exhaust all nonzero octal digits',[(a,b,c,d) for a in range(1,8) for b in range(1,8) for c in range(1,8) for d in range(1,8) if 8*a+b+F(c,8)+F(d,64)==13*b+F(b,12)+F(a,144)],[(3,2,1,4)])
check('2017-I-09','Directly iterate recurrence modulo99',next(n for n in range(11,100) if (n*(n+1)//2-45)%99==0),45)
check('2017-I-14','Independent modular exponentiation',pow(2,192,1000),896)
nums=[F(i,2) for i in [103,275,365,471]]
check('2017-II-05','Verify all six pairwise sums of equality witness',sorted(a+b for a,b in combinations(nums,2)),list(map(F,[189,234,287,320,373,418])))
check('2017-II-06','Exhaust candidates through the larger solution', [n for n in range(1,169) if isqrt(n*n+85*n+2017)**2==n*n+85*n+2017],[27,168])
check('2017-II-08','Exact denominator test for every integer in the problem range',sum((n**6+6*n**5+30*n**4+120*n**3+360*n*n)%720==0 for n in range(1,2017)),134)
check('2018-I-02','Exhaust all allowed digits',[(a,b,c) for a in range(1,6) for b in range(14) for c in range(6) if 196*a+14*b+c==225*a+b+15*c==222*a+37*c],[(4,10,1)])
check('2018-I-11','Direct order computation modulo143²',next(n for n in range(1,196) if pow(3,n,143**2)==1),195)
check('2018-II-03','Exhaust every permitted base', [b for b in range(8,1000) if isqrt(3*b+6)**2==3*b+6 and any(v**3==2*b+7 for v in range(1,13))],[10,361])
z=[complex(20,12),complex(-10,-10),complex(-3,3)]
check('2018-II-05','Check all three products in a realizing triple',[z[0]*z[1],z[1]*z[2],z[2]*z[0]],[complex(-80,-320),60,complex(-96,24)])
check('2018-II-07','Square-test every one of2450 slice indices',sum(isqrt(6*k)**2==6*k for k in range(1,2451)),20)
pts=[(F(4),F(3)),(F(27,2),F(0)),(F(23),F(3)),(F(27),F(23,2)),(F(23),F(20)),(F(27,2),F(23)),(F(4),F(20))]
area=abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(pts,pts[1:]+pts[:1])))/2
check('2018-II-09','Independent exact shoelace calculation and homothety',area*F(4,9),F(184))
check('2019-I-01','Construct321 terms as exact integers and sum decimal digits',ds(sum(10**k-1 for k in range(1,322))),342)
def tau(n):return sum(n%d==0 for d in range(1,isqrt(n)+1))*2-(isqrt(n)**2==n)
check('2019-I-09','Exhaust n through sixth solution',[n for n in range(1,362) if tau(n)+tau(n+1)==7],[8,9,16,25,121,361])
check('2019-I-14','Trial every odd prime below98',[p for p in range(3,98,2) if tau(p)==2 and pow(2019,8,p)==p-1],[97])
check('2019-II-09','Exhaust all eligible multiples of20',sum(n for n in range(20,2019,20) if tau(n)==20)//20,472)
check('2019-II-10','Exact doubling orbit modulo7',[3*pow(2,n,7)%7<3.5 for n in range(30)],[n%3==0 for n in range(30)])
check('2020-I-03','Exhaust digit representations below621',min(121*a+11*b+c for a in range(1,8) for b in range(8) for c in range(8) if 120*a==512+53*b+7*c),621)
check('2020-I-04','Enumerate all divisor prefixes',sum(ds(10000*d+2020) for d in range(1,2021) if 2020%d==0),93)
check('2020-I-10','Exhaust all pairs with sum at most407',[(m,n) for n in range(1,204) for m in range(n+1,408-n) if gcd(m+n,210)==1 and m%n and pow(m,m)%pow(n,n)==0],[(286,121)])
N=2*4**10-1
check('2020-II-05','Exact minimum construction modulo1000',N%1000,151)
a,b=F(20),F(21)
for n in range(3,2021):a,b=b,(5*b+1)/(25*a)
check('2020-II-06','Iterate2020 terms with exact fractions',b,F(101,525))
z={1}
for n in range(2,102):
 z={n+sg*k for k in z if k>=0 for sg in [-1,1]}
 if n==100:check('2020-II-08','Construct distinct zeros at100',sum(z),495100)
check('2020-II-08','Construct distinct zeros at101',sum(z),510151)
check('2020-II-10','Verify all necessary divisor candidates',[(n,(n*(n+1)//2)**2%(n+5)) for n in [78,161,327]],[(78,17),(161,17),(327,100)])
check('2021-I-05','Exhaust bounded divisor-derived middle terms',[(a,d) for a in range(3,15) for d in range(1,10) if 3*a*a+2*d*d==a*d*d],[(5,5),(14,7)])
a=F(2020,2021);special=[]
for j in range(1,1001):
 if a.denominator-a.numerator==1:special.append(j)
 a=F(a.numerator+18,a.denominator+19)
check('2021-I-10','Iterate1000 reduced fractions independently',special,[1,2,8,18,30])
check('2021-I-14','Verify explicit prime-order witnesses',[next(k for k in range(1,p) if pow(a,k,p)==1) for a,p in [(3,43),(5,47)]],[42,46])
L=2*3*7*23*43*47
check('2021-I-14','All residues in both prime moduli satisfy the geometric-sum criterion',all(q==0 or (L%p==0 if q==1 else pow(q,L,p)==1) for p in [43,47] for q in range(p)),True)
check('2021-II-13','Exhaust all smaller positive exponents',next(n for n in range(1,798) if (pow(2,n,1000)+pow(5,n,1000)-n)%1000==0),797)
def square_functions(n):
 a=isqrt(n)
 if a*a<n:a+=1
 b=a
 if b%2!=n%2:b+=1
 return a*a-n+a,b*b-n+b
check('2021-II-15','Evaluate exact stopping formulas for all smaller n',next(n for n in range(1,259) if 7*square_functions(n)[0]==4*square_functions(n)[1]),258)
check('2022-I-02','Exhaust all decimal and octal-style base-nine digit bounds',[(a,b,c) for a in range(1,9) for b in range(1,9) for c in range(9) if 100*a+10*b+c==81*b+9*c+a],[(2,2,7)])
check('2022-I-14','Exhaust all positive integer cosine-law sides',[(a,b) for a in range(1,219) for b in range(a,219) if a*a+a*b+b*b==219**2],[(51,189)])
check('2022-II-06','Check the optimizing ordered sequence', [sum([F(-1,32)]*16+[F(0)]*59+[F(1,50)]*25),sum(abs(x) for x in [F(-1,32)]*16+[F(0)]*59+[F(1,50)]*25), F(1,50)+F(1,32)],[F(0),F(1),F(41,800)])
# With h=sqrt5, B=(4/7,6h/7), C=(38/7,8h/7).
check('2022-II-11','Exact reflected midpoint coefficients',[(F(4,7)+F(38,7))/2,(F(6,7)+F(8,7))/2],[F(3),F(1)])
check('2023-II-02','Exhaust decimal and octal palindromes below1000',max(n for n in range(1,1000) if str(n)==str(n)[::-1] and oct(n)[2:]==oct(n)[2:][::-1]),585)
check('2023-I-10','Sum all2023 floors directly',1349+sum((n*n-1349*n)//5 for n in range(1,2024)),944)
candidates=[]
for a in range(-31,32):
 for b in range(-31,32):
  p=a*a+b*b
  if p>=1000 or p<2 or tau(p)!=2:continue
  x=a*a*a-3*a*b*b;y=3*a*a*b-b*b*b
  if min(p,x,y)>0 and abs(x-y)<p<x+y:candidates.append(p)
check('2023-I-15','Exhaust every Gaussian integer with prime norm below1000',sorted(set(candidates)),[2,17,53,241,349])
c0,c1=2,9;count=0
for m in range(1,251):
 if c1%10==9:count+=1
 c0,c1=c1,9*c1-16*c0
check('2023-II-13','Compute exact power-sum integers for all250 multiples of4',count,167)
a=23;count=0
for n in range(1,1001):
 old=a
 if (a-1)%(2**(n+1)):a+=23*2**n
 count+=old==a
check('2023-II-15','Lift actual1000-bit multiples rather than the carry-state table',count,363)
check('2024-I-13','Enumerate all roots modulo289', [n for n in range(1,289) if (n**4+1)%289==0],[110,134,155,179])
check('2024-II-07','Exhaust every four-digit number',max(n for n in range(1000,10000) if all((n+(1-int(str(n)[i]))*10**(3-i))%7==0 for i in range(4))),5694)
counts=[]
for b in range(2,212):
 B=b-1
 counts.append(sum(1 for k in range(2,b) if k*(k-1)%B==0))
check('2024-II-14','Enumerate every permitted square root for every smaller base',next((i+2,c) for i,c in enumerate(counts) if c>10),(211,15))
parts=[]
def partitions(total,least=1,acc=()):
 if total==0:
  yield acc;return
 for x in range(least,total+1):yield from partitions(total-x,x,acc+(x,))
for a in partitions(30):
 if len(a)%2:continue
 f={x:a.count(x) for x in set(a)}
 if 9 not in f or any(v>=f[9] for x,v in f.items() if x!=9):continue
 t=a[len(a)//2-1]+a[len(a)//2]
 if t%2==0 and t//2 not in a:parts.append(a)
check('2024-II-02','Exhaust every integer partition of30',parts,[(5,7,9,9)])
check('2025-I-01','Exhaust all bases allowed by the fixed divisor bound',[b for b in range(10,50) if (9*b+7)%(b+7)==0],[21,49])
check('2025-I-04','Exhaust the full201-by201 lattice square',sum(12*x*x-x*y-6*y*y==0 for x in range(-100,101) for y in range(-100,101)),117)
check('2025-II-02','Test every candidate through the proven bound',[n for n in range(1,38) if (3*(n+3)*(n*n+9))%(n+2)==0],[1,11,37])
prod=F(1)
for k in range(4,64):prod*=F(k*k-1,k*k-4)
check('2025-II-04','Exact multiplication of every rational telescoping factor',3*prod,F(93,13))
a,b=25,11
for k in range(1,9):
 check('2025-II-13',f'Check exact reduction and sum at term{k}',a+b,3*12**(2**(k-1)))
 num=a*a-a*b+b*b;den=3*a*b;g=gcd(num,den);a,b=num//g,den//g
check('2025-II-13','Independent exponent reduction and CRT',[pow(2,2024,100),pow(12,16,125),next(n for n in range(1000) if n%8==0 and n%125==123)],[16,41,248])
for k,S,T in [(8,98,1008),(32,110,2016),(200,194,5040)]:
 M=2*S*T-127008-10116*k
 check('2025-II-15',f'All coefficients of the nonnegative square identity for k={k}',[2*S,S*S+2*T,T*T],[188+k,10116+188*k,127008*k])
 check('2025-II-15',f'Two distinct positive minimizing roots for k={k}', S>0 and T>0 and S*S>4*T, True)
out=Path(__file__).with_name('recent_all_subjects_results.json');out.write_text(json.dumps(dict(total=len(checks),passed=len(checks),checks=checks),indent=2))
print(f'{len(checks)} independent checks passed')
