import io
import sys

_INPUT = """\
6
3 5 2
3 2 3 4
.....
.@..@
..@..
1 6 4
1 1 1 6
......
3 3 1
2 1 2 3
.@.
.@.
.@.
10 10 3
7 10 8 4
..........
.@@@...@@@
...@...@.@
....@@....
.@...@@...
@.@.....@.
@@...@....
..........
........@.
.@...@....
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def Dijkstra(x,y):
    dir=[(-1,0),(0,1),(1,0),(0,-1)]
    done=[False]*(H*W*4)
    inf=10**20
    dist=[inf]*(H*W*4)
    h=[]
    for i in range(4):
      dist[(x*W+y)*4+i]=0
      heappush(h,(0,(x*W+y)*4+i))
    while h:
      tt,t=heappop(h)
      a,b,d=t//4//W,t//4%W,t%4
      if done[t]:
        continue
      done[t]=True
      for i in range(4):
        if i==d:
          if 0<=a+dir[i][0]<H and 0<=b+dir[i][1]<W and C[a+dir[i][0]][b+dir[i][1]]=='.' and dist[((a+dir[i][0])*W+b+dir[i][1])*4+i]>dist[t]+1:
            dist[((a+dir[i][0])*W+b+dir[i][1])*4+i]=dist[t]+1
            heappush(h,(dist[t]+1,((a+dir[i][0])*W+b+dir[i][1])*4+i))
        else:
          if dist[(a*W+b)*4+i]>((dist[t]-1)//K+1)*K:
            dist[(a*W+b)*4+i]=((dist[t]-1)//K+1)*K
            heappush(h,(((dist[t]-1)//K+1)*K,(a*W+b)*4+i))
    return dist

  H,W,K=map(int,input().split())
  x1,y1,x2,y2=map(int,input().split())
  C=[input() for _ in range(H)]
  ans=Dijkstra(x1-1,y1-1)
  ans=min([ans[((x2-1)*W+y2-1)*4+i] for i in range(4)])
  if ans==10**20: print(-1)
  else: print((ans-1)//K+1)