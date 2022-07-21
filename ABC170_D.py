import io
import sys

_INPUT = """\
6
5
24 11 8 3 16
4
5 5 5 5
10
33 18 45 28 8 19 89 86 2 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  B=set(A)
  A.sort()
  S=max(A)
  ans=[1]*S
  for i in range(len(A)):
    if ans[A[i]-1]!=0:
      if i>0 and A[i]==A[i-1]:
        ans[A[i]-1]=0
      for j in range(A[i]*2,S+1,A[i]):
        ans[j-1]=0
  k=0
  for i in A:
    if ans[i-1]==1:
      k+=1
  print(k)