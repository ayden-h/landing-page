"""Independent, scoped checks for newly authored middle-era solutions."""
import cmath,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks={}
def check(id,ok,detail):
 assert ok,(id,detail)
 checks[id]=detail
# Direct digit and divisor searches do not use the proof parametrizations.
check('2000-I-01',next(n for n in range(1,10) if all('0' in str(d) or '0' in str(10**n//d) for d in (2**a*5**b for a in range(n+1) for b in range(n+1))))==8,'Exhaustively checked every divisor factorization for powers 10^1 through 10^8.')
check('2000-I-02',[(u,v) for u in range(1,452) for v in range(1,u) if u*(u+3*v)==451]==[(11,10)],'Exhaustive bounded integer search of the reflected-polygon area equation.')
check('2000-I-06',sum(1 for x in range(1,1000000) if math.isqrt(x)**2==x and (math.isqrt(x)+2)**2<1000000)==997,'Exhaustive check over the full x range of the derived square condition; exhaustion relies on the analytic reduction.')
check('2000-I-07',F(1,5)*24*F(5,24)==1 and F(1,5)+F(24,5)==5 and 24+5==29 and F(5,24)+F(1,24)==F(1,4),'Exact substitution of all three variables into the original system and target.')
S=F(2525,49); xs=[(S-k)/2 for k in range(1,101)]
check('2000-I-10',sum(xs)==S and all(xs[k-1]==sum(xs)-xs[k-1]-k for k in range(1,101)) and xs[49]==F(75,98),'Exact substitution of all 100 entries into the original linear system.')
check('2000-II-02',sum(2 for y in range(-999999,1000000) if math.isqrt(y*y+4000000)**2==y*y+4000000)==98,'Brute-force integer-square test for every y in the analytically bounded range, counting both signs of x.')
valid=[]
for n in range(1,181):
 ds=[d for d in range(1,n+1) if n%d==0]
 if sum(d%2==1 for d in ds)==6 and sum(d%2==0 for d in ds)==12:valid.append(n)
check('2000-II-04',valid==[180],'Direct divisor enumeration for every positive integer through the claimed minimum.')
check('2000-II-08',F(110)==10*11 and F(110)+81*11==1001,'Exact check of perpendicular-diagonal and leg-length equations.')
angles=sum(math.atan(a/math.sqrt(647)) for a in [19,26,37,23])
check('2000-II-10',abs(angles-math.pi)<1e-12,'Independent numerical half-angle closure check for the claimed inradius.')
slopes={F(7-b,1-a) for a in range(-7,8) for b in range(-7,8) if a*a+b*b==50 and a not in [-1,1]}
check('2000-II-11',len(slopes)==8 and sum(abs(x) for x in slopes)==F(119,12),'Enumerated all integer leg vectors of squared norm 50 and summed distinct admissible slopes.')
N=sum((-1)**(k+1)*math.factorial(16*k) for k in range(1,126));digits=[];q=N;i=1
while q:
 q,r=divmod(q,i+1);digits.append(r);i+=1
check('2000-II-14',sum((-1)**i*d for i,d in enumerate(digits))==495 and sum(d*math.factorial(i+1) for i,d in enumerate(digits))==N,'Direct mixed-radix division of the full exact factorial integer, with reconstruction check.')
s=sum(1/(math.sin(math.radians(t))*math.sin(math.radians(t+1))) for t in range(45,135,2))
check('2000-II-15',abs(s*math.sin(math.radians(1))-1)<1e-12,'Numerically evaluated all 45 original trigonometric terms.')
check('2001-I-01',sum(n for n in range(10,100) if n%10 and n%(n//10)==0 and n%(n%10)==0)==630,'Exhaustive check of all 90 two-digit integers against both divisibility conditions.')
u=8*math.sqrt(3)/13;v=1-math.sqrt(3)*u
check('2001-I-05',abs(u*u+4*v*v-4)<1e-12 and abs(u*u+(v-1)**2-4*u*u)<1e-12,'Substituted the two lower vertices into the ellipse and independently compared squared side lengths.')
def digits7(n):
 out=[]
 while n:n,r=divmod(n,7);out.append(r)
 return out[::-1]
admissible=[n for n in range(1,343) if int(''.join(map(str,digits7(n))))==2*n]
check('2001-I-08',max(admissible)==315,'Exhaustive check of all N below 7^3; the analytic place-value argument supplies the global bound.')
check('2001-I-12',F(12)-11*F(2,3)==7*F(2,3),'Exact inside point-plane distance check for the claimed insphere center.')
seq=[None,211,375,420,523]
for n in range(5,976):seq.append(seq[-1]-seq[-2]+seq[-3]-seq[-4])
check('2001-II-03',seq[531]+seq[753]+seq[975]==898,'Directly generated every recurrence term through index 975 without using periodicity.')
P=(F(32,7),F(60,7));Q=(F(80,7),F(24,7))
check('2001-II-04',8*P[1]==15*P[0] and 10*Q[1]==3*Q[0] and tuple((a+b)/2 for a,b in zip(P,Q))==(8,6) and sum((a-b)**2 for a,b in zip(P,Q))==F(3600,49),'Exact endpoint substitution, midpoint check, and squared-distance calculation.')
check('2001-II-07',(70-15)**2+(10-75)**2==7250,'Exact squared-distance check between the derived incenters; geometric center derivation remains analytic.')
roots=[]
for k in range(24):
 t=15*k;z=cmath.exp(1j*math.radians(t))
 if abs(z**28-z**8-1)<1e-10:roots.append(t)
check('2001-II-14',roots==[15,75,105,165,195,255,285,345] and sum(roots[1::2])==840,'Checked every 15-degree candidate in the original complex equation; the analytic congruence proof establishes exhaustiveness.')
# Area of the five-sided wall by 3D vector cross products, independent of parameter-domain decomposition.
verts=[(2,0,0),(0,2,0),(6,8,6),(8,8,7),(8,6,6)]
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
cv=[0,0,0]
for a,b in zip(verts,verts[1:]+verts[:1]):
 c=cross(a,b);cv=[u+v for u,v in zip(cv,c)]
check('2001-II-15',sum(v*v for v in cv)==4*13**2*6,'Computed the exact squared area of a tunnel wall from its five vertices using the polygon cross-product formula.')
check('2002-I-04',sum((F(1,k*k+k) for k in range(28,812)),F())==F(1,29),'Summed all 784 original rational terms exactly for the claimed endpoints.')
collisions={}
for u in range(1,749):
 for v in range(u,(748-13*u)//21+1):collisions.setdefault(13*u+21*v,[]).append((u,v))
check('2002-I-08',[k for k,v in collisions.items() if len(v)>1]==[748] and collisions[748]==[(1,35),(22,22)],'Enumerated all positive ordered initial pairs with ninth term at most 748; found the unique first collision.')
z=F(1,137)+1j
for j in range(2002):z=(z+1j)/(z-1j)
check('2002-I-12',abs(z-(1+274j))<1e-6,'Numerically iterated the original complex map 2002 times, independently of the period-three reduction.')
check('2002-II-01',len({abs(n-int(str(n)[::-1])) for n in range(100,1000) if n%10})==9,'Exhaustively reversed every eligible three-digit integer and counted distinct differences.')
pts=[(7,12,10),(8,8,1),(11,3,9)]
check('2002-II-02',all(sum((a-b)**2 for a,b in zip(pts[i],pts[j]))==98 for i in range(3) for j in range(i)),'Exact pairwise squared-distance check for the three supplied cube vertices.')
check('2002-II-03',[(a,36,1296//a) for a in range(1,36) if 1296%a==0 and math.isqrt(36-a)**2==36-a]==[(27,36,48)],'Exhaustively checked every smaller integer first term against the square-gap and integral geometric-mean constraints.')
check('2002-II-04',sum(max(abs(u),abs(v),abs(u+v))<=200 for u in range(-200,201) for v in range(-200,201))==120601,'Independently enumerated the enclosed hexagonal-grid cells in axial coordinates.')
check('2002-II-05',sum(2**n*3**m for n in range(21) for m in range(21) if max(6*n,6*m)>2**n*3**m)==42,'Exhaustively tested exponent pairs through 20; the analytic monotonic bounds certify all larger pairs are excluded.')
check('2002-II-06',round(1000*sum(1/(n*n-4) for n in range(3,10001)))==521,'Numerically summed all 9998 original terms directly; the proof supplies the rigorous rounding margin.')
ss=0;first=None
for k in range(1,401):
 ss+=k*k
 if ss%200==0 and first is None:first=k
check('2002-II-07',first==112,'Directly accumulated square sums until the first multiple of 200, without congruence reduction.')
qs={2002//n for n in range(1,2003)}
check('2002-II-08',next(k for k in range(1,2003) if k not in qs)==49,'Enumerated every possible positive nonzero floor quotient and found the first missing value.')
r=(1+math.sqrt(5))/4;s=1-r
check('2002-II-11',0<r<1 and 0<s<1 and abs((1-r)*r*r-1/8)<1e-14 and abs(r*(1-r)-(math.sqrt(5)-1)/8)<1e-14,'Checked convergence, the prescribed third term, and the shared second term for the two distinct ratios.')
check('2002-II-14',F(152,3)**2+38**2==F(190,3)**2 and F(152,3)+38+F(190,3)==152 and 38*(F(152,3)-19)/F(190,3)==19,'Exact Pythagorean, perimeter, and point-to-hypotenuse tangency checks for the derived right triangle.')
check('2003-I-02',F(sum((2*k)**2-(2*k-1)**2 for k in range(1,51)),10000)==F(101,200),'Direct exact sum of all 50 green annular area coefficients.')
xs=[x for x in range(16,96) if math.isqrt(x*x-189)**2==x*x-189]
check('2003-I-07',xs==[17,33,95] and sum(30+2*x for x in xs)==380,'Enumerated every possible equal-side length within the factor-pair bound and tested the second distance by integer square roots.')
seqs=[(a-d,a,a+d,(a+d)**2//a) for d in range(1,10) for a in range(d+1,10001) if (a+d)**2%a==0 and (a+d)**2//a-(a-d)==30]
check('2003-I-08',seqs==[(18,27,36,48)],'Exhaustively checked steps 1 through 9 and middle terms through 10000; the analytic inequality narrows the unbounded problem to the two final steps.')
deg=math.pi/180;M=(2*math.sin(7*deg)*math.cos(23*deg),2*math.sin(7*deg)*math.sin(23*deg));B=(math.cos(106*deg),math.sin(106*deg))
check('2003-I-10',abs(sum((a-b)**2 for a,b in zip(M,B))-1)<1e-13,'Constructed M from its ray and sine-law distance, then independently checked the claimed hidden equal side numerically.')
fracs=[(v,u) for v in range(1,128) for u in range(1,v) if 251*v<=1000*u<252*v]
check('2003-I-14',fracs==[(127,32)],'Exhaustive integer comparison for all fractions of denominator at most 127 in the target decimal interval.')
check('2003-II-02',9876543120%8==0 and len(set(str(9876543120)))==10 and [v for v in [12,21,102,120,201,210] if v%8==0]==[120],'Checked all six suffix permutations, distinct digits, and divisibility of the full maximal-prefix candidate.')
# Exact convex polygon clipping provides a separate union-area computation.
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def polygon_area(poly):return abs(sum(det(a,b) for a,b in zip(poly,poly[1:]+poly[:1])))/2
def clip(poly,a,b):
 out=[];edge=sub(b,a)
 for p,q in zip(poly,poly[1:]+poly[:1]):
  fp=det(edge,sub(p,a));fq=det(edge,sub(q,a))
  if fp>=0:out.append(p)
  if (fp<0<fq) or (fq<0<fp):
   t=fp/(fp-fq);out.append(tuple(x+t*(y-x) for x,y in zip(p,q)))
 return out
tri=[(F(0),F(0)),(F(14),F(0)),(F(5),F(12))];G=tuple(sum(p[i] for p in tri)/3 for i in range(2));ref=[tuple(2*g-x for g,x in zip(G,p)) for p in tri];inter=tri
for a,b in zip(ref,ref[1:]+ref[:1]):inter=clip(inter,a,b)
check('2003-II-06',polygon_area(tri)+polygon_area(ref)-polygon_area(inter)==112,'Exact rational polygon clipping computed the intersection and union of the original 13-14-15 triangle and its centroid reflection.')
check('2003-II-08',[(17-2*n)*(36*n+60) for n in [1,2,3,8]]==[1440,1716,1848,348],'Constructed two explicit arithmetic sequences matching all three supplied products and checked their eighth product; uniqueness follows from quadratic interpolation.')
vals=[]
for a in range(1,197):
 t=math.isqrt(a*(a+60))
 if t*t==a*(a+60):
  c=2*a+60+2*t
  if math.isqrt(c)**2!=c:vals.append(2*a+60)
check('2003-II-10',max(vals)==156,'Brute-force exact radical-integrality tests for every possible smaller integer within the analytic factor-pair bound.')
vs=[(F(0),F(0)),(F(10),F(2)),(F(18),F(6)),(F(10),F(10)),(F(0),F(8)),(F(-8),F(4))]
edges=[sub(b,a) for a,b in zip(vs,vs[1:]+vs[:1])]
check('2003-II-14',all(x*x/3+y*y==F(112,3) for x,y in edges) and polygon_area(vs)==144 and all(det(edges[i],edges[(i+1)%6])>0 for i in range(6)),'Exact scaled-coordinate checks of all six equal lengths, positive turns, and area; actual x-coordinates are divided by sqrt(3).')
coeff=[0]*48
for i in range(24):
 for j in range(24):coeff[1+i+j]+=1
check('2003-II-15',coeff[24]==24 and all(coeff[24-j]==coeff[24+j]==24-j for j in range(1,24)) and abs(sum(abs(math.sin(k*math.pi/6)) for k in range(24))-(8+4*math.sqrt(3)))<1e-12,'Verified the exact polynomial coefficient convolution and independently summed the 24 trigonometric contributions numerically.')

# Additional independent checks of the 2006--2009 authoring batches.
check('2006-I-03',next(n for n in range(10,1000) if int(str(n)[1:])*29==n)==725,'Exhaustive decimal-deletion test of every integer below the claimed minimum and the candidate itself.')
prod=math.prod(math.factorial(n) for n in range(1,101));zeros=0
while prod%10==0:prod//=10;zeros+=1
check('2006-I-04',zeros==1124,'Constructed the full exact product of 100 factorials and repeatedly divided by ten, independently of the valuation sum.')
check('2006-I-05',2*13*4==104 and 2*13*18==468 and 2*4*18==144 and 2*13**2+3*4**2+5*18**2==2006,'Exact coefficient expansion of the proposed radical identity.')
check('2006-I-09',sum(12*u+66*v==6018 for u in range(502) for v in range(92))==46,'Exhaustive exponent-pair enumeration within bounds supplied by the exact prime-factor reduction.')
sols=[t/2 for t in range(201,400) if abs(math.cos(math.radians(3*t/2))**3+math.cos(math.radians(5*t/2))**3-8*math.cos(math.radians(4*t/2))**3*math.cos(math.radians(t/2))**3)<1e-10]
check('2006-I-12',sols==[112.5,126.0,150.0,157.5,162.0,198.0] and sum(sols)==906,'Substituted every half-degree candidate into the original trigonometric equation; the analytic factorization establishes exhaustiveness.')
prod=math.prod(range(1,200,2));v=0
while prod%3==0:prod//=3;v+=1
check('2006-II-03',v==49,'Constructed the exact product of the first 100 odd integers and counted factors of three directly.')
a=[1,1,1]
for i in range(3,30):a.append(sum(a[-3:]))
check('2006-II-11',sum(a[:28])==13346834 and a[-3:]==[6090307,11201821,20603361],'Generated all 30 terms from the original recurrence and directly summed the first 28.')
representations=[0]*1000
for start in range(1,1000,2):
 total=0
 for end in range(start,1000,2):
  total+=end
  if total>=1000:break
  representations[total]+=1
check('2006-II-13',sum(c==5 for c in representations)==15,'Enumerated every consecutive positive odd sequence with sum below 1000, independently of divisor-count classification.')
x,y,z=[v/(15*math.sqrt(7)) for v in (8,10,12)]
check('2006-II-15',max(abs(x-math.sqrt(y*y-1/16)-math.sqrt(z*z-1/16)),abs(y-math.sqrt(z*z-1/25)-math.sqrt(x*x-1/25)),abs(z-math.sqrt(x*x-1/36)-math.sqrt(y*y-1/36)))<1e-12,'Numerically substituted the proposed solution into all three original radical equations, including radical signs.')
check('2007-I-01',sum(k*k%24==0 for k in range(1,1000))==83,'Exhaustively tested divisibility for every eligible positive square root.')
check('2007-I-03',((9+15j)**2).imag==((9+15j)**3).imag,'Direct complex-power evaluation of the proposed positive imaginary part.')
A=(0.,0.);B=(20.,0.);C=(10.,10*(2+math.sqrt(3)))
def rotate2(p,t):return (p[0]*math.cos(t)-p[1]*math.sin(t),p[0]*math.sin(t)+p[1]*math.cos(t))
rot=[rotate2(p,math.pi/12) for p in [A,B,C]];poly=[A,B,C]
for a,b in zip(rot,rot[1:]+rot[:1]):poly=clip(poly,a,b)
expected=500*math.sqrt(2)-350*math.sqrt(3)+300*math.sqrt(6)-600
check('2007-I-12',abs(polygon_area(poly)-expected)<1e-9,'Independently clipped the original and rotated triangles numerically and compared their polygon area with the radical expression.')
verts=[(-1,1,math.sqrt(2)),(1.5,1.5,math.sqrt(2)/2),(2,0,0),(0,-2,0),(-1.5,-1.5,math.sqrt(2)/2)]
cv=[sum(cross(a,b)[j] for a,b in zip(verts,verts[1:]+verts[:1])) for j in range(3)]
check('2007-I-13',abs(sum(t*t for t in cv)/4-80)<1e-10,'Computed the section area by a 3D polygon cross product, independently of horizontal projection.')
a,b=3,3
for n in range(1,21):
 c,rem=divmod(b*b+2007,a);assert rem==0;a,b=b,c
check('2007-I-14',(a*a+b*b)//(a*b)==224 and a*a+b*b+2007==225*a*b,'Generated 20 exact nonlinear-recurrence steps and checked the floor and invariant; the proof extends them to index 2006.')
for sign in [-1,1]:
 x=(231+sign*3*math.sqrt(989))/10;y=(5*x-66)/3
 AA=(0.,0.);BB=(x,0.);CC=(x/2,x*math.sqrt(3)/2);FF=(5.,0.);EE=(y/2,y*math.sqrt(3)/2);DD=(CC[0]+2*(BB[0]-CC[0])/x,CC[1]+2*(BB[1]-CC[1])/x)
 v=sub(DD,EE);w=sub(FF,EE)
 assert abs(sum(i*j for i,j in zip(v,w))/(math.hypot(*v)*math.hypot(*w))-.5)<1e-12
 assert abs(polygon_area([DD,EE,FF])-14*math.sqrt(3))<1e-10
check('2007-I-15',True,'Constructed both candidate triangles in coordinates and independently checked the 60-degree angle, prescribed area, and segment placements.')
kcounts={k:sum(n%k==0 for n in range(k**3,(k+1)**3)) for k in range(1,40)}
check('2007-II-07',[k for k,c in kcounts.items() if c==70]==[22] and max(n//22 for n in range(22**3,23**3) if n%22==0)==553,'Directly enumerated the cube-root intervals through k=39; the analytic count proves no further k works.')
check('2007-II-12',sum(3**(21+5*j) for j in range(8))>=3**56 and sum(3**(21+5*j) for j in range(8))<=3**57 and sum(21+5*j for j in range(8))==308,'Exact large-integer substitution of the proposed progression into both original conditions.')
for x in range(-20,21):assert (1+x*x)**2*(1+(2*x*x)**2)**2==(1+(2*x**3+x)**2)**2
check('2007-II-14',25+100==125 and 26**2==676,'Checked the proposed polynomial identity at 41 integer inputs, more than its degree, and both numerical conditions; classification uniqueness remains analytic.')
check('2008-I-03',[(b,j,s) for b in range(1,38) for j in range(1,25) for s in range(1,19) if 2*b+3*j+4*s==74 and 4*b+2*j+3*s==91]==[(15,8,5)],'Exhaustively checked all positive integral rates within bounds from the first distance equation.')
check('2008-I-04',[(x,math.isqrt(x*x+84*x+2008)) for x in range(1,245) if math.isqrt(x*x+84*x+2008)**2==x*x+84*x+2008]==[(18,62)],'Direct square test through the factorization-derived global bound, finding the unique positive solution.')
check('2008-I-08',abs(sum(math.atan(1/k) for k in [3,4,5,47])-math.pi/4)<1e-15,'Direct numerical evaluation of the original four arctangents.')
check('2008-I-12',F(3749*3751,3750**2)<1 and F(3750*3751,3750**2)>1,'Exact crossing-span check for the attaining finite speed; the analytic headway bound excludes 3751 at every speed.')
x,y=F(5,19),F(16,19)
check('2008-I-13',x-x**3-F(3,2)*x*y*(1-x)==0 and y-y**3-F(3,2)*x*y*(1-x)==0,'Exact substitution into both independently variable basis coefficients; the analytic elimination proves this basis spans the constrained family.')
check('2008-II-01',sum(k*k*(1 if k%4 in [0,3] else -1) for k in range(1,101))==10100,'Directly evaluated all 100 signed square terms.')
check('2008-II-03',max((10-a)*(13-b)*(14-c) for a in range(10) for b in range(11) for c in range(11) if a+b+c==10)==729,'Exhaustively enumerated every nonnegative allocation of the ten unit slices with a positive remaining first dimension.')
check('2008-II-04',3**7-3**5+3**4-3**3+3**2+1==2008,'Exact reconstruction from the signed powers; the proof supplies uniqueness.')
a=[F(1),F(1)];b=[F(1),F(3)]
for n in range(2,33):a.append(a[-1]+a[-1]**2/a[-2]);b.append(b[-1]+b[-1]**2/b[-2])
check('2008-II-06',b[32]/a[32]==561,'Generated both original rational recurrences exactly through index 32 without using factorial formulas.')
s=0.;first=None
for n in range(1,252):
 s+=2*math.cos(n*n*math.pi/2008)*math.sin(n*math.pi/2008)
 if abs(s-round(s))<1e-10 and first is None:first=n
check('2008-II-08',first==251,'Directly summed the original trigonometric series at every candidate index through 251.')
z=5+0j
for n in range(150):z=cmath.exp(1j*math.pi/4)*z+10
check('2008-II-09',abs(z-(-5*math.sqrt(2)+(5+5*math.sqrt(2))*1j))<1e-10,'Numerically applied all 150 original rotation-and-translation moves.')
valid=[]
for n in range(1,182):
 if math.isqrt(2*n+79)**2==2*n+79:
  for t in range(105):
   if (t+1)**3-t**3==n*n:valid.append(n)
check('2008-II-15',max(valid)==181,'Directly checked both original square/cube conditions through the analytically established maximum, without using the factor-pair candidates.')
geo=[]
for n in range(100,1000):
 a,b,c=map(int,str(n))
 if len({a,b,c})==3 and b*b==a*c:geo.append(n)
check('2009-I-01',min(geo)==124 and max(geo)==964,'Exhaustively tested all 900 three-digit numbers for distinct geometric digits.')
check('2009-I-02',(-656+164j)/(-656+164j+697)==4j,'Exact floating complex division for integer components verifies the original quotient.')
check('2009-I-14',min(350+3*x+8*y+15*z for z in range(55) for y in range(82) for x in [163-2*y-3*z] if x>=0 and x+y+z<=350 and 15*x+80*y+255*z==4395)==905,'Enumerated every feasible frequency vector using the count and moment constraints, and minimized the second moment.')
check('2009-II-04',min(n for n in range(1,90) for c in range(1,46) if n-2*(c-1)>=0 and sum(n-2*j for j in range(c))==2009)==89,'Enumerated all nonnegative arithmetic-score contests with winner count at most 89.')
S=F()
for i in range(1,2010):S+=F(math.comb(2*i,i),2**(2*i))
check('2009-II-07',S.denominator==2**4010,'Summed all 2009 rational summands exactly and checked the fully reduced denominator.')
check('2009-II-11',[(m,n) for n in range(1,8) for m in range(n,52) if m*n-m//n-1==50]==[(19,3),(34,2)] or [(m,n) for n in range(1,8) for m in range(n,52) if m*n-m//n-1==50]==[(34,2),(19,3)],'Exhaustively counted integer points in every analytically bounded open interval.')
prod=math.prod(8*math.sin(k*math.pi/7) for k in range(1,7))
check('2009-II-13',abs(prod-28672)<1e-8,'Directly multiplied the twelve chord lengths using six paired altitude products.')
a=0.
for n in range(10):a=8*a/5+6*math.sqrt(4**n-a*a)/5
check('2009-II-14',math.floor(a)==983 and abs(a-24576/25)<1e-9,'Numerically iterated the original unnormalized radical recurrence through index ten.')

# 2010–2011: direct modular, finite, geometric, and exact substitution checks.
r=1
for k in range(1,1000):r=r*(pow(10,k,1000)-1)%1000
check('2010-I-02',r==109,'Direct modular multiplication of all 999 factors.')
x,y=F(256,81),F(64,27)
check('2010-I-03',y==F(3,4)*x and x**3==y**4 and x+y==F(448,81),'Exact positive-rational substitution: x^3=y^4 is equivalent to the original positive-power equation when y=3x/4.')
vertices={(u+du,v+dv) for u in range(-5,6) for v in range(-5,6) if u*u+v*v==25 for du in [0,1] for dv in [0,1]}
check('2010-I-08',max((F(x)-F(1,2))**2+(F(y)-F(1,2))**2 for x,y in vertices)==F(65,2) and max((x-u)**2+(y-v)**2 for x,y in vertices for u,v in vertices)==130,'Enumerated all closure-cell vertices, their distances from the proposed center, and all pairwise distances.')
for t in [F(-4),F(-15,7)]:assert (t+2)*(t+6)*(t+20)==t**3
check('2010-I-09',max(3*t+28 for t in [F(-4),F(-15,7)])==F(151,7),'Exact substitution of both analytically exhaustive product parameters and comparison of target values.')
check('2010-I-14',sum(len(str(k*109))-1 for k in range(1,101))==300 and sum(len(str(k*110))-1 for k in range(1,101))==301,'Evaluated the 100 original floor-log terms exactly using decimal lengths at the boundary integers.')
B=(20/3,math.sqrt(896)/3);M=(22/3,0);d=math.dist(B,M)
r1=(M[0]*B[1]/2)/((12+d+M[0])/2);r2=((15-M[0])*B[1]/2)/((13+d+15-M[0])/2)
check('2010-I-15',abs(d-10)<1e-12 and abs(r1-r2)<1e-12,'Constructed the proposed point in Cartesian coordinates and independently compared the two area-over-semiperimeter inradii; optimality and uniqueness remain analytic.')
from itertools import permutations
valid=[int(''.join(p)) for n in range(1,6) for p in permutations('02468',n) if p[0]!='0' and int(''.join(p))%36==0]
check('2010-II-01',max(valid)==8640,'Enumerated every decimal string of distinct even digits, excluding leading zero, and directly tested divisibility by 36.')
choices=[]
for b in range(-63,64):
 if b and 63%b==0:
  d=63//b
  for a in range(-12,13):
   if b+d==a*a and a*(b-d)>0:choices.append(a*(b-d))
linear=[r**3+63//r for r in range(-63,64) if r and 63%r==0 and r**3+63//r>0]
check('2010-II-06',min(choices+linear)==8,'Exhausted integral constant-factor pairs and integer roots in all factorization types; the coefficient bound |a|<=12 covers b+d<=126.')
roots=[4,4+6j,4-6j]
check('2010-II-07',sum(roots).imag==0 and abs((-sum(roots)+sum(roots[i]*roots[j] for i in range(3) for j in range(i+1,3))-math.prod(roots)).real)==136,'Direct Vieta coefficient computation for the proposed conjugate root triple.')
outer=[(math.cos(k*math.pi/3),math.sin(k*math.pi/3)) for k in range(6)]
inner=outer[:]
for k in range(6):
 a=outer[k];b=tuple((outer[(k+1)%6][j]+outer[(k+2)%6][j])/2 for j in range(2));inner=clip(inner,a,b)
check('2010-II-09',abs(polygon_area(inner)/polygon_area(outer)-F(4,7))<1e-12,'Independently clipped the outer hexagon by all six defining lines and computed the area ratio by shoelace.')
valid=[]
for perimeter in range(1,677):
 for t in range(1,perimeter//15+1):
  b1,b2=8*t,7*t
  if (perimeter-b1)%2 or (perimeter-b2)%2:continue
  a1,a2=(perimeter-b1)//2,(perimeter-b2)//2
  if 2*a1>b1 and 2*a2>b2 and b1*b1*(4*a1*a1-b1*b1)==b2*b2*(4*a2*a2-b2*b2):valid.append((perimeter,a1,b1,a2,b2))
check('2010-II-12',valid==[(676,218,240,233,210)],'Exhausted all integer-sided isosceles pairs with base ratio 8:7 and perimeter through 676, comparing exact squared areas.')
check('2010-II-15',-F(15)*(F(15,2)-F(70,9))/(F(13)*(F(13,2)-F(182,29)))==F(725,507),'Exact evaluation of the radical-axis affine ratio; the geometric power interpretation is established analytically.')
check('2011-I-01',F(18,10)+F(8,10)*F(2,3)==F(1,2)*(4+F(2,3)) and F(24,10)+F(8,10)*F(1,3)==F(1,2)*(5+F(1,3)),'Exact substitution into both final concentration balances.')
u,v=3*math.sqrt(21)/17,F(10,17);E=(12-9*u,10-9*v);H=(8*u,8*v)
check('2011-I-02',abs(math.dist(E,(12,10))-9)<1e-12 and abs(math.dist(H,(0,0))-8)<1e-12 and E[1]==H[1] and abs(math.dist(E,H)-(3*math.sqrt(21)-12))<1e-12,'Independent coordinate reconstruction verifies both segment lengths, equal heights, and the requested separation.')
# Project C onto the two normalized angle-bisector vectors directly.
A=(0.,0.);B=(125.,0.);cx=(117**2+125**2-120**2)/250;C=(cx,math.sqrt(117**2-cx*cx))
def projection(point,origin,vector):
 q=sub(point,origin);t=sum(q[i]*vector[i] for i in range(2))/sum(x*x for x in vector);return tuple(origin[i]+t*vector[i] for i in range(2))
vA=(1+C[0]/117,C[1]/117);vB=(-1+(C[0]-125)/120,C[1]/120)
N=projection(C,A,vA);M=projection(C,B,vB)
check('2011-I-04',abs(math.dist(M,N)-56)<1e-11,'Computed both perpendicular projections from Cartesian side-length coordinates, independently of the reflection proof.')
check('2011-I-06',F(2,9)*F(9,16)-F(9,8)==-1,'Exact substitution of the minimal coefficient into the vertex-form integer condition; minimality remains analytic.')
check('2011-I-09',F(24)*F(1,3)**3+F(1,3)**2==1 and 24*(1-F(1,9))/F(1,9)==192,'Exact substitution into the cubed trigonometric identity and target; the proof checks logarithm admissibility.')
res=[];v=1
while v not in res:res.append(v);v=2*v%1000
check('2011-I-11',v==8 and sum(res)%1000==7,'Generated the full modular orbit up to its first repetition and summed every distinct residue.')
h=(33-math.sqrt(294))/3
check('2011-I-13',0<h<10 and abs(sum((k-h)**2 for k in [10,11,12])-100)<1e-12,'Numerically checked the vertical-component identity and nearest-vertex branch.')
triples=[]
for a in range(-51,52):
 for b in range(a,52):
  c=-a-b
  if c>=b and a*b+a*c+b*c==-2011:triples.append((a,b,c))
check('2011-I-15',triples==[(-49,10,39),(-39,-10,49)] and all(sum(map(abs,t))==98 for t in triples),'Enumerated every sorted integer-root triple in the analytically proved magnitude bound 51.')
s=math.sqrt(810);E=(0,s/3);H=(s,2*s/3)
check('2011-II-02',all(abs(t-30)<1e-12 for t in [math.dist((s,0),E),math.dist(E,H),math.dist(H,(0,s))]),'Direct distance check of the nondegenerate trisection configuration.')
check('2011-II-03',[(a,d) for a in range(1,180) for d in range(1,180) if sum(a+k*d for k in range(18))==2880 and a+17*d<180]==[(143,2)],'Exhaustive integer search over all convex arithmetic-progressive angle lists.')
values=[8*cmath.exp(1j*k*math.pi/6) for k in range(12)]
check('2011-II-08',abs(sum(max(z.real,-z.imag) for z in values)-(16+math.sqrt(768)))<1e-12,'Computed all twelve complex roots numerically and maximized each allowed two-choice real contribution directly.')
xs=[F(1,3),F(19,60),F(1,3),F(0),F(1,60),F(0)]
check('2011-II-09',sum(xs)==1 and xs[0]*xs[2]*xs[4]+xs[1]*xs[3]*xs[5]==F(1,540) and sum(xs[k]*xs[(k+1)%6]*xs[(k+2)%6] for k in range(6))==F(19,540),'Exact substitution verifies the nonnegative equality witness and both original cubic expressions; the upper bound is analytic.')
# Choose F=(24,0), E=(52/3,8 sqrt14/3), then intersect the perpendicular chord lines.
E=(52/3,8*math.sqrt(14)/3);P=(24,(400-24*E[0])/E[1])
check('2011-II-10',abs(math.dist(E,(24,0))-12)<1e-12 and abs(sum(v*v for v in P)-4050/7)<1e-12,'Independent Cartesian intersection of the two chord lines gives OP squared and the specified midpoint distance.')
def determinant(matrix):
 if len(matrix)==1:return matrix[0][0]
 return sum((-1)**j*matrix[0][j]*determinant([row[:j]+row[j+1:] for row in matrix[1:]]) for j in range(len(matrix)))
check('2011-II-11',all(determinant([[10 if i==j else 3 if abs(i-j)==1 else 0 for j in range(n)] for i in range(n)])==(9**(n+1)-1)//8 for n in range(1,8)),'Independently computed determinants by full cofactor expansion for sizes 1 through 7; the infinite-series conclusion is analytic.')
s,p=6*math.sqrt(2),2*math.sqrt(6);P=(p,0);O1=((p-s)/2,(s-p)/2);O2=((p+s)/2,-(p+s)/2)
v1,v2=sub(O1,P),sub(O2,P)
check('2011-II-13',abs(math.dist(O1,(-s,0))-math.dist(O1,(0,s)))<1e-12 and abs(math.dist(O1,P)-math.dist(O1,(0,s)))<1e-12 and abs(sum(v1[i]*v2[i] for i in range(2))/(math.hypot(*v1)*math.hypot(*v2))+0.5)<1e-12,'Independent distance and dot-product checks verify the proposed circumcenter configuration and 120-degree angle.')

(ROOT/'data/middle_expansion_verification.json').write_text(json.dumps({'checked':len(checks),'checks':checks},indent=2)+'\n')
rows=json.loads((ROOT/'solutions/middle.json').read_text())
for row in rows:
 if row['id'] in checks:row['verification']=checks[row['id']]
(ROOT/'solutions/middle.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print(len(checks),'independent or explicitly scoped checks passed')
