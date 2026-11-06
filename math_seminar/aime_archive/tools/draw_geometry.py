"""Draw original schematic figures with exact geometric constructions."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

OUT=Path(__file__).resolve().parents[2]/'aime_geometry/figures'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':11})
blue='#215878';gold='#a86414';grey='#65737c'

def canvas():
    f,a=plt.subplots(figsize=(6.4,3.7));a.set_aspect('equal');a.axis('off');return f,a
def point(a,p,label,offset=(.12,.12),color=blue):
    a.plot(*p,'o',color=color,ms=4);a.text(p[0]+offset[0],p[1]+offset[1],label,color=color)
def line(a,p,q,**kw):a.plot([p[0],q[0]],[p[1],q[1]],**kw)
def save(f,name):
    f.tight_layout(pad=.8)
    for ext in ('png','svg'):f.savefig(OUT/f'{name}.{ext}',dpi=220,bbox_inches='tight')
    plt.close(f)

f,ax=canvas();A=np.array([0.,4.]);B=np.array([-3.,0.]);C=np.array([5.,0.])
a=np.linalg.norm(B-C);b=np.linalg.norm(C-A);c=np.linalg.norm(A-B)
I=(a*A+b*B+c*C)/(a+b+c);r=I[1]
ax.add_patch(Polygon([A,B,C],closed=True,fill=False,edgecolor=blue,lw=1.7))
ax.add_patch(Circle(I,r,fill=False,edgecolor=gold,lw=1.7))
T=np.array([I[0],0.]);line(ax,I,T,color=gold,lw=1.3)
for p,s,o in ((A,'A',(-.1,.2)),(B,'B',(-.35,-.25)),(C,'C',(.1,-.25)),(I,'I',(.12,.12)),(T,'T',(.1,-.3))):point(ax,p,s,o)
ax.text(I[0]+.12,I[1]/2,'r',color=gold)
ax.text(-1.7,-.35,'y');ax.text(3.,-.35,'z')
ax.set_xlim(-3.8,5.8);ax.set_ylim(-.7,4.6);save(f,'incircle_tangent_lengths')

f,ax=canvas();R=5.;r=4.;d=6.;h=(R*R-r*r+d*d)/(2*d);v=np.sqrt(R*R-h*h)
for center,radius in (((0,0),R),((d,0),r)):ax.add_patch(Circle(center,radius,fill=False,lw=1.6,edgecolor=blue))
line(ax,(-5.4,0),(10.4,0),color=grey,lw=.8,ls='--');line(ax,(h,-v),(h,v),color=gold,lw=2)
for p,s,o in (((0,0),'O₁',(-.4,-.8)),((d,0),'O₂',(.1,-.8)),((h,v),'U',(.2,.1)),((h,-v),'V',(.2,-.1))):point(ax,p,s,o)
ax.annotate('',xy=(h,-.2),xytext=(0,-.2),arrowprops={'arrowstyle':'<->','color':gold});ax.text(h/2-.15,-.8,'h',color=gold)
ax.set_xlim(-5.5,10.7);ax.set_ylim(-5.5,5.5);save(f,'radical_axis')

f,ax=canvas();A=(0,3);B=(8,1);Bp=(8,-1);X=(6,0)
line(ax,(-1,0),(9,0),color=grey,lw=1.2)
line(ax,A,X,color=blue,lw=2);line(ax,X,B,color=blue,lw=2)
line(ax,X,Bp,color=gold,lw=1.5,ls='--');line(ax,B,Bp,color=grey,lw=1,ls=':')
for p,s,o in ((A,'A',(-.3,.2)),(B,'B',(.15,.1)),(Bp,"B′",(.15,-.2)),(X,'X',(-.3,-.4))):point(ax,p,s,o)
ax.text(-.7,-.4,r'$\ell$');ax.set_xlim(-1,9);ax.set_ylim(-1.7,3.6);save(f,'reflection_path')

f,ax=canvas();a=3.;b=9.;H=5.;x=np.sqrt((a*a+b*b)/2);t=H*(x-a)/(b-a)
ax.add_patch(Polygon([(-a/2,0),(a/2,0),(x/2,t),(-x/2,t)],color='#e8f0f4'))
ax.add_patch(Polygon([(-a/2,0),(a/2,0),(b/2,H),(-b/2,H)],closed=True,fill=False,edgecolor=blue,lw=1.7))
line(ax,(-x/2,t),(x/2,t),color=gold,lw=2)
ax.text(-.2,-.45,'a');ax.text(-.2,H+.2,'b');ax.text(-.2,t+.2,'x',color=gold)
ax.text(-.75,1.1,'half the area',fontsize=10);ax.set_xlim(-5.2,5.2);ax.set_ylim(-.7,5.7);save(f,'trapezoid_area_section')

f,ax=canvas();A=np.array([0.,4.]);B=np.array([-3.,0.]);C=np.array([5.,0.])
D=(B+2*C)/3;E=(C+3*A)/4;P=(6*A+B+2*C)/9
ax.add_patch(Polygon([P,B,C],closed=True,color='#e8f0f4'))
ax.add_patch(Polygon([A,B,C],closed=True,fill=False,edgecolor=blue,lw=1.6))
line(ax,A,D,color=gold,lw=1.4);line(ax,B,E,color=gold,lw=1.4)
for p,s,o in ((A,'A',(-.1,.2)),(B,'B',(-.35,-.25)),(C,'C',(.1,-.25)),(D,'D',(-.1,-.35)),(E,'E',(.2,.1)),(P,'P',(.16,-.15))):point(ax,p,s,o)
ax.set_xlim(-3.8,5.8);ax.set_ylim(-.7,4.6);save(f,'cevian_area')
print('Wrote five original geometry figures in PNG and SVG.')
