import io
import sys

_INPUT = """\
6
6 3
8 1
6 2
9 3
1 1
2 2
1 3
4 3
2 1
1 2
2 2
4208 1234
3056 5678
1 2020
2 2020
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class SegTree:
    X_unit = 1 << 30
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)
  from heapq import heappop, heappush
  N,Q=map(int,input().split())
  kind=[set() for _ in range(2*10**5)]
  kind_rate=[[] for _ in range(2*10**5)]
  max_rate=[1<<30]*(2*10**5)
  child=[[0,0]]*N
  for i in range(N):
    A,B=map(int,input().split())
    kind[B-1].add(i)
    heappush(kind_rate[B-1],(-A,i))
    if max_rate[B-1]==(1<<30) or A>max_rate[B-1]: max_rate[B-1]=A
    child[i]=[A,B-1]
  st=SegTree(2*10**5)
  st.build(max_rate)
  for i in range(Q):
    C,D=map(int,input().split())
    C-=1; D-=1
    rate,cur=child[C]
    child[C][1]=D
    kind[cur].remove(C)
    while len(kind_rate[cur])>0 and kind_rate[cur][0][1] not in kind[cur]: heappop(kind_rate[cur])
    if len(kind_rate[cur])==0:
      max_rate[cur]=(1<<30)
      st.set_val(cur,1<<30)
    else:
      max_rate[cur]=-kind_rate[cur][0][0]
      st.set_val(cur,-kind_rate[cur][0][0])
    kind[D].add(C)
    heappush(kind_rate[D],(-rate,C))
    if max_rate[D]==1<<30: max_rate[D]=rate
    else: max_rate[D]=max(max_rate[D],rate)
    st.set_val(D,max_rate[D])
    print(st.fold(0,2*10**5))