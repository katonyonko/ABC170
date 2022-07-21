import io
import sys

_INPUT = """\
6
6 5
4 7 10 6 5
10 5
4 7 10 6 5
100 0

"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  X,N=map(int,input().split())
  if N==0:
    print(X)
  else:
    p=set(map(int,input().split()))
    i=-1
    for j in range(102):
      if abs(X-j)<abs(X-i) and not(j in p):
        i=j
    print(i)