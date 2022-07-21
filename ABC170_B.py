import io
import sys

_INPUT = """\
6
3 8
2 100
1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  x=list(map(int,input().split()))
  if x[0]*2<=x[1] and x[1]<=x[0]*4 and x[1]%2 ==0:
    print("Yes")
  else:
    print("No")