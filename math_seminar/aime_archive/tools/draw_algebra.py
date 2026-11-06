"""Original plots illustrating the independently proved 2024-I-12 count."""
from pathlib import Path
import math,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[2]/'aime_algebra'
(root/'figures').mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10})
def H(t):return 4*np.abs(np.abs(np.abs(t)-.5)-.25)
fig,axes=plt.subplots(1,2,figsize=(12,5),layout='constrained')
t=np.linspace(0,1,12001)
axes[0].plot(t,H(np.sin(2*np.pi*t)),color='#196a9b',lw=.8,label='$y=F(x)$')
axes[0].plot(H(np.cos(3*np.pi*t)),t,color='#b74a31',lw=.8,label='$x=G(y)$')
axes[0].set(xlim=(0,1),ylim=(0,1),xlabel='$x$',ylabel='$y$',title='Full pattern in the unit square')
axes[0].set_aspect('equal');axes[0].legend(fontsize=9,loc='upper left',framealpha=.95)
a=np.linspace(0,15e-6,2000);b=np.linspace(0,.0004,2000)
axes[1].plot(1e6*a,1e3*4*np.sin(2*np.pi*a),color='#196a9b',lw=1.6)
axes[1].plot(1e6*8*np.sin(1.5*np.pi*b)**2,1e3*b,color='#b74a31',lw=1.6)
lo,hi=1e-8,2e-5
for _ in range(90):
 mid=(lo+hi)/2
 delta=8*math.sin(6*math.pi*math.sin(2*math.pi*mid))**2-mid
 if delta>0:hi=mid
 else:lo=mid
ar=(lo+hi)/2;br=4*math.sin(2*math.pi*ar)
axes[1].scatter([0,1e6*ar],[0,1e3*br],s=26,color='#20252a',zorder=4,clip_on=False)
axes[1].annotate('interior crossing',(1e6*ar,1e3*br),xytext=(5,.33),arrowprops={'arrowstyle':'->','color':'#444'},fontsize=9)
axes[1].set(xlim=(0,15),ylim=(0,.4),xlabel=r'$(1-x)\times10^6$',ylabel=r'$(1-y)\times10^3$',title='Magnified near $(1,1)$')
axes[1].grid(alpha=.18)
for ax in axes:
 for side in ('top','right'):ax.spines[side].set_visible(False)
for ext in ('png','svg'):fig.savefig(root/'figures'/('oscillatory_intersections.'+ext),dpi=220,bbox_inches='tight')
plt.close(fig)
print(json.dumps({'illustrative_interior_intersection':[1-ar,1-br],'proof':'Algebra Theory Chapter 18; numerical root is for plotting only.'}))
