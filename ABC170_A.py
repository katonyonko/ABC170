import io
import sys

_INPUT = """\
6
0 2 3 4 5
1 2 0 4 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  x=list(map(int,input().split()))
  i=x.index(0)+1
  print(i)