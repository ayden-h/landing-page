"""Finite checks supporting (not replacing) the written proofs. Standard library only."""
from fractions import Fraction
from itertools import combinations, product
from collections import deque
import json
from pathlib import Path

results={}

def toggles(n):
    out=[]
    for r in range(n):
        for c in range(n):
            out.append(sum(1<<(i*n+j) for i,j in [(r,c),(r-1,c),(r+1,c),(r,c-1),(r,c+1)] if 0<=i<n and 0<=j<n))
    return out

cols=toggles(5)
basis={}
for j,col in enumerate(cols):
    v,recipe=col,1<<j
    while v:
        p=v.bit_length()-1
        if p not in basis:
            basis[p]=(v,recipe);break
        bv,br=basis[p];v^=bv;recipe^=br
reachable={}
for j in range(25):
    v,recipe=1<<j,0
    while v and v.bit_length()-1 in basis:
        bv,br=basis[v.bit_length()-1];v^=bv;recipe^=br
    if not v:
        reachable[f'{j//5+1},{j%5+1}']=[[i//5+1,i%5+1] for i in range(25) if recipe>>i&1]
assert set(reachable)=={'2,2','2,4','3,3','4,2','4,4'}
results['W04']={'rank':len(basis),'reachable_singletons_and_switches':reachable}

vertices=list(product(range(1,5),repeat=2))
adj=lambda a,b: sorted([abs(a[0]-b[0]),abs(a[1]-b[1])])==[1,2]
cycles=[]
for s in combinations(vertices,4):
    if all(sum(adj(a,b) for b in s)==2 for a in s):cycles.append(frozenset(s))
def cover(left,chosen):
    if not left:return chosen
    p=min(left)
    for cy in cycles:
        if p in cy and cy<=left:
            ans=cover(left-cy,chosen+[sorted(cy)])
            if ans:return ans
knight_cycles=cover(set(vertices),[])
assert knight_cycles and len(knight_cycles)==4
results['W16']={'four_knight_cycles_in_4x4':knight_cycles}

bishop_checks={}
for N in [2,4,8,16]:
    seen={(0,0)};queue=deque(seen)
    while queue:
        row,mask=queue.popleft()
        for bit in range(N.bit_length()-1):
            h=1<<bit
            for dr in [-h,h]:
                state=(row+dr,mask^h)
                if 0<=state[0]<N and state not in seen:seen.add(state);queue.append(state)
    bottom=sorted(mask for row,mask in seen if row==N-1)
    assert bottom==list(range(1,N,2))
    bishop_checks[str(N)]=bottom
results['W09']={'bottom_xor_masks':bishop_checks}

def val(a):return (a&-a).bit_length()-1
for total in range(2,151):
    moves={a:[] for a in range(1,total)}
    for a in moves:
        b=total-a
        if a%2==0:moves[a].append(a//2)
        if b%2==0:moves[a].append(a+b//2)
    status={a:'L' for a in moves if not moves[a]}
    changed=True
    while changed:
        changed=False
        for a,ms in moves.items():
            if a in status:continue
            if any(status.get(b)=='L' for b in ms):status[a]='W';changed=True
            elif all(status.get(b)=='W' for b in ms):status[a]='L';changed=True
    for a in moves:
        x,y=val(a),val(total-a)
        predicted=('L' if x%2==0 else 'W') if x==y else ('W' if min(x,y)%2 else 'D')
        assert status.get(a,'D')==predicted,(a,total-a,status.get(a),predicted)
results['W23']={'all_ordered_positive_pairs_with_sum_at_most':150,'retrograde_classification':'matches proof, including draws'}

tile_checks=0
for k in range(2,15):
    for n in range(k,2*k):
        if n==k:
            tiles=[{(r,c) for c in range(k)} for r in range(n)]
        elif n==2*k-1:
            tiles=[{(r,c) for c in range(k-1,n)} if r==k-1 else {(r,c) for c in range(k)} for r in range(n)]
        else:
            tiles=[{(0,c) for c in range(k)},{(r,0) for r in range(1,k+1)},{(k,c) for c in range(1,k+1)},{(r,k) for r in range(k)}]
            tiles += [{(r,c) for c in range(1,k+1)} for r in range(k+1,n)]
            tiles += [{(r,c) for r in range(1,k+1)} for c in range(k+1,n)]
        occupied=set().union(*tiles)
        assert len(occupied)==k*len(tiles)
        for r in range(n):
            for c in range(n-k+1):assert any((r,j) in occupied for j in range(c,c+k))
        for c in range(n):
            for r in range(n-k+1):assert any((i,c) in occupied for i in range(r,r+k))
        expected=n if n==k else min(n,2*n-2*k+2)
        assert len(tiles)==expected
        tile_checks+=1
results['W24']={'maximal_nonoverlapping_constructions_checked':tile_checks,'k_range':[2,14]}

sharp_checks=[]
for n in range(2,5):
    for B in range(n,2*n):
        d=B-n+1;k=max(range(d,n+1),key=lambda x:x*(n+d-x));l=k-d;q=n-l
        tau=Fraction(d,k*q)
        matrix=[[Fraction(1,k) if i<k and j<l else tau if i<k else Fraction(0) if j<l else Fraction(1,q) for j in range(n)] for i in range(n)]
        assert all(sum(row)==1 for row in matrix)
        assert all(sum(matrix[i][j] for i in range(n))==1 for j in range(n))
        best=Fraction(0)
        for selected in combinations(range(n*n),B):
            rows=[Fraction(0)]*n;colsums=[Fraction(0)]*n
            for t in selected:
                i,j=divmod(t,n);rows[i]+=matrix[i][j];colsums[j]+=matrix[i][j]
            best=max(best,min(rows+colsums))
        assert best==tau,(n,B,best,tau)
        sharp_checks.append({'n':n,'B':B,'best':str(best)})
results['W18']={'sharp_example_exhaustive_subsets':sharp_checks}

grid=[set(range(r*8,(r+1)*8)) for r in range(7)]+[{r*8+c for r in range(7)} for c in range(8)]
assert min(len(set().union(*(grid[i] for i in inds))) for inds in combinations(range(15),7))==40
results['W13']={'seven_set_unions_checked':6435,'minimum_union':40}

mat=[[1,1,1,-1],[1,1,-1,1],[1,-1,-1,-1],[-1,1,-1,-1]]
assert sum(map(sum,mat))==0
assert all(abs(sum(row))==2 for row in mat)
assert all(abs(sum(mat[i][j] for i in range(4)))==2 for j in range(4))
results['W21']={'4x4_tile':'all row and column imbalances equal 2; total zero'}

def terminal_states(state,memo):
    if state in memo:return memo[state]
    active=[i for i,a in enumerate(state) if a>1]
    if len(active)<2:return {state}
    import math
    out=set()
    for i,j in combinations(active,2):
        a,b=state[i],state[j];g=math.gcd(a,b)
        nxt=tuple(sorted([x for h,x in enumerate(state) if h not in (i,j)]+[g,a*b//(g*g)]))
        assert (math.prod(nxt),sum(x>1 for x in nxt))<(math.prod(state),len(active))
        out|=terminal_states(nxt,memo)
    memo[state]=out;return out
memo={}
for triple in combinations(range(2,10),3):assert len(terminal_states(tuple(triple),memo))==1
results['W01']={'distinct_initial_triples_from_2_through_9':56,'unique_terminal_multisets':True}

target=Path(__file__).with_name('verification_results.json')
target.write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
