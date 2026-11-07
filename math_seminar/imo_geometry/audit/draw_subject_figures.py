from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(__file__).resolve().parent
INK='#18374A';ACC='#287C92';GOLD='#BA7538'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':INK,'text.color':INK,'axes.edgecolor':'#8B9AA5'})
def save(fig,subject,name):
    p=OUT/(subject+'_Research_Package')/'figures';p.mkdir(exist_ok=True)
    for ext in ['pdf','png']:fig.savefig(p/(name+'.'+ext),bbox_inches='tight',dpi=160)
    plt.close(fig)

x=np.linspace(.02,20,700);fig,ax=plt.subplots(figsize=(6.5,3.1))
ax.plot(x,np.minimum(1,3/np.sqrt(1+x)),color=ACC,lw=2.7)
ax.axvline(8,color=GOLD,lw=1,ls='--');ax.scatter([8],[1],c=GOLD,zorder=5)
ax.text(3,.83,'Boundary infimum\nnot attained',ha='center');ax.text(14,.93,'Equal variables\nattain the minimum',ha='center')
ax.set(xlabel=r'$\lambda$',ylabel='Sharp infimum',xlim=(0,20),ylim=(.6,1.09));ax.grid(axis='y',alpha=.2)
save(fig,'Algebra','radical_threshold')

fig,ax=plt.subplots(figsize=(6.5,2.9));ax.axis('off')
table=[[str(2**i*(2*j+1)) for j in range(6)] for i in range(4)]
t=ax.table(cellText=table,rowLabels=[f'row {i}' for i in range(4)],colLabels=[f'unit {j+1}' for j in range(6)],loc='center',cellLoc='center');t.scale(1,1.7)
for (i,j),cell in t.get_celld().items():
    cell.set_edgecolor('#D2DBDF')
    if i==0:cell.set_facecolor(INK);cell.get_text().set_color('white')
    elif j>=0 and int(table[i-1][j])<=12:cell.set_facecolor('#D7EDF0')
ax.set_title('Marginal costs: the shaded entries are exactly 1 through 12',fontsize=11,pad=12)
save(fig,'Algebra','marginal_costs')

def circle3(a,b,c):
    o=np.linalg.solve(2*np.array([b-a,c-a]),np.array([b@b-a@a,c@c-a@a]));return o,np.linalg.norm(a-o)
def circ(ax,o,r,color,alpha=1,lw=1.4):
    t=np.linspace(0,2*np.pi,600);ax.plot(o[0]+r*np.cos(t),o[1]+r*np.sin(t),c=color,alpha=alpha,lw=lw)
A=np.array([0.,3.]);B=np.array([-2.,0.]);C=np.array([1.,0.]);F=np.zeros(2);H=np.array([0.,2/3]);M=(B+C)/2;Ap=2*M-H;E=np.array([0.,-2/3]);O,rad=circle3(A,B,C)
qpar=H[1]*(H[1]-A[1])/(M[0]**2+H[1]**2);Q=H+qpar*(M-H)
R=np.array([-2*H[1]**2/M[0],-H[1]]);S=(R+H)/2
v=Q-R;other=((R-O)@(R-O)-rad*rad)/(v@v);K=R+other*v
fig,ax=plt.subplots(figsize=(6.8,5.2));circ(ax,O,rad,'#B2BCC3',lw=1)
o1,r1=circle3(K,Q,H);o2,r2=circle3(K,F,M);circ(ax,o1,r1,ACC);circ(ax,o2,r2,GOLD)
ax.plot([B[0],A[0],C[0],B[0]],[B[1],A[1],C[1],B[1]],c=INK,lw=1)
for u,vv in [(M,Q),(Ap,R),(H,R),(Q,R)]:ax.plot([u[0],vv[0]],[u[1],vv[1]],c='#8B9AA5',lw=.8,ls='--')
v=K-S;ax.plot([S[0]-v[0]*.7,S[0]+v[0]*1.8],[S[1]-v[1]*.7,S[1]+v[1]*1.8],c='#398455',lw=2)
offset={'A':(6,5),'B':(-14,-12),'C':(5,-14),'F':(-3,-15),'H':(-15,5),'M':(-12,-14),"A'":(-15,-12),'E':(-4,-15),'Q':(7,1),'R':(5,-6),'S':(-12,-15),'K':(7,5)}
for name,p in [('A',A),('B',B),('C',C),('F',F),('H',H),('M',M),("A'",Ap),('E',E),('Q',Q),('R',R),('S',S),('K',K)]:
    ax.scatter(*p,s=12,c=INK,zorder=5);ax.annotate(name,p,xytext=offset[name],textcoords='offset points',fontsize=10)
ax.set_aspect('equal');ax.axis('off');ax.set_xlim(-2.4,2.4);ax.set_ylim(-1.1,3.65)
save(fig,'Geometry','tangent_transfer')

fig,ax=plt.subplots(figsize=(6.5,3.0));xx=np.linspace(-.5,33,500);yy=xx**2-32*xx+60
ax.plot(xx,yy,c=ACC,lw=2);ax.axhline(0,c='#7F8A90',lw=.8);ax.scatter([2,30],[0,0],c=GOLD,zorder=5)
ax.annotate('smaller root 2',(2,0),xytext=(3,65),arrowprops=dict(arrowstyle='->',color=INK));ax.annotate('larger root 30',(30,0),xytext=(18,65),arrowprops=dict(arrowstyle='->',color=INK))
ax.text(16,-150,r'$x^2-4\cdot8x+(8^2-4)=0$',ha='center',fontsize=12)
ax.set(xlabel='Possible first coordinate x, with b = 8',ylabel='Quadratic value',ylim=(-210,125));ax.grid(axis='y',alpha=.2)
save(fig,'Number_Theory','vieta_jump')

# Exact coordinate residual checks for the illustrated geometry (floating-point diagnostics only).
checks={'Q_on_circumcircle':abs(np.linalg.norm(Q-O)-rad),'K_on_circumcircle':abs(np.linalg.norm(K-O)-rad),
        'AQ_perp_HQ':abs((A-Q)@(H-Q)),'QK_perp_HK':abs((Q-K)@(H-K)),
        'common_tangent_first':abs((S-K)@(K-o1)),'common_tangent_second':abs((S-K)@(K-o2))}
assert max(checks.values())<1e-10,checks
import json
(OUT/'Geometry_Research_Package/audit/figure_checks.json').write_text(json.dumps(checks,indent=2))
print(checks)
