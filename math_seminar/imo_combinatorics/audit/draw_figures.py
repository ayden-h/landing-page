from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
P=Path(__file__).parent/'Combinatorics_Research_Package'/'figures';P.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
ink='#18374a';blue='#287c92';gold='#c68b36'

fig,ax=plt.subplots(figsize=(8,2.4));ax.set_xlim(-.65,7.65);ax.set_ylim(-.4,1.55);ax.axis('off')
for c in range(8):
    color=blue if c<4 else gold
    ax.add_patch(FancyArrowPatch((c,1),(c^2,0),arrowstyle='-|>',mutation_scale=12,lw=1.4,color=color,alpha=.8))
    for y in [0,1]:
        ax.plot(c,y,'o',color='white',markeredgecolor=ink,markersize=17,zorder=3)
        ax.text(c,y,str(c),ha='center',va='center',fontsize=10,color=ink,zorder=4)
    ax.text(c,1.29,f'{c:03b}',ha='center',va='center',fontsize=10,color=ink)
ax.text(3.5,-.31,'Height 2 flips the middle binary bit: destination = column XOR 2.',ha='center',fontsize=11,color=ink)
fig.tight_layout();fig.savefig(P/'bishop_xor.pdf',bbox_inches='tight');fig.savefig(P/'bishop_xor.png',dpi=180,bbox_inches='tight');plt.close(fig)

fig,ax=plt.subplots(figsize=(6.2,5.2));ax.set_xlim(-10,105);ax.set_ylim(108,-10);ax.set_aspect('equal');ax.axis('off')
for x,y,w,h,col,txt in [(0,0,24,75,'#c3dce4','1/75'),(24,0,76,75,'#e8be80','17/1900'),(0,75,24,25,'#eef0f2','0'),(24,75,76,25,'#c3dce4','1/76')]:
    ax.add_patch(Rectangle((x,y),w,h,facecolor=col,edgecolor=ink,lw=1.5))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=14,color=ink)
ax.text(12,-4,'24 columns',ha='center',fontsize=10,color=ink);ax.text(62,-4,'76 columns',ha='center',fontsize=10,color=ink)
ax.text(-5,37.5,'75 rows',rotation=90,ha='center',va='center',fontsize=10,color=ink);ax.text(-5,87.5,'25 rows',rotation=90,ha='center',va='center',fontsize=10,color=ink)
ax.text(50,106,'The 75 top rows and 76 right columns create 151 requirements.',ha='center',fontsize=9,color=ink)
fig.tight_layout();fig.savefig(P/'stochastic_blocks.pdf',bbox_inches='tight');fig.savefig(P/'stochastic_blocks.png',dpi=180,bbox_inches='tight');plt.close(fig)

k,n=5,8
fig,ax=plt.subplots(figsize=(5.7,5.7));ax.set_xlim(-.6,n+.3);ax.set_ylim(n+.7,-.6);ax.set_aspect('equal');ax.axis('off')
for i in range(n+1):ax.plot([0,n],[i,i],color='#c8ced2',lw=.6,zorder=0);ax.plot([i,i],[0,n],color='#c8ced2',lw=.6,zorder=0)
tiles=[(0,0,k,1,'H1'),(0,1,1,k,'V1'),(1,k,k,1,'H2'),(k,0,1,k,'V2')]
tiles += [(1,r,k,1,f'H{r-k+2}') for r in range(k+1,n)]
tiles += [(c,1,1,k,f'V{c-k+2}') for c in range(k+1,n)]
for x,y,w,h,label in tiles:
    ax.add_patch(Rectangle((x+.035,y+.035),w-.07,h-.07,facecolor='#e8be80' if w>1 else '#9cc6d3',edgecolor=ink,lw=1.0))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',color=ink,fontsize=11,rotation=0 if w>1 else 90)
ax.text(n/2,n+.4,'k = 5, n = 8: eight tiles; every remaining straight gap is shorter than five.',ha='center',fontsize=8.7,color=ink)
fig.tight_layout();fig.savefig(P/'maximal_tiles.pdf',bbox_inches='tight');fig.savefig(P/'maximal_tiles.png',dpi=180,bbox_inches='tight');plt.close(fig)
print('Three exact mathematical figures created.')
