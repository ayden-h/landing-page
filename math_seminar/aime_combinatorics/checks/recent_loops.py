from functools import lru_cache
from collections import Counter

def count(n):
 full=(1<<(n*n))-1
 diag=sum(1<<(i*n+i) for i in range(n)); anti=sum(1<<(i*n+n-1-i) for i in range(n))
 loops=[];bycell=[[] for _ in range(n*n)]
 for r in range(n-1):
  for c in range(n-1):
   for h in range(2,n-r+1):
    for w in range(2,n-c+1):
     b=sum(1<<(i*n+j) for i in range(r,r+h) for j in range(c,c+w) if i in (r,r+h-1) or j in(c,c+w-1))
     if bin(b&diag).count("1")!=2 or bin(b&anti).count("1")!=2:continue
     idx=len(loops);loops.append((b,(r,c,h,w)))
     for i in range(n*n):
      if b>>i&1:bycell[i].append(idx)
 @lru_cache(None)
 def f(mask):
  if mask==full:return 1
  i=((full^mask)&-(full^mask)).bit_length()-1
  return sum(f(mask|loops[j][0]) for j in bycell[i] if not mask&loops[j][0])
 ans=f(0)
 first={dims[2:]:f(b) for b,dims in loops if dims[:2]==(0,0) and f(b)}
 print(n,len(loops),ans,first,'states',f.cache_info(),flush=True)
 return ans
for n in (2,4,6,8,10):count(n)
