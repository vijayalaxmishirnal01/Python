"""Sample Input
2
1
1
3
Sample Output
-1
Explanation
The total amount of cash in the ATM is 2, hence Sarah cannot withdraw an amount of 3."""

n=int(input())
a=[]
for i in range(n):
 a.append(int(input()))

def answer(s,e,k):
 if k==0:
  return 0

 if s>e or k<0:
  return 10**9

 else:
  return min(1+answer(s+1,e,k-a[s]),1+answer(s,e-1,k-a[e]))

k=int(input())
k1=answer(0,n-1,k)
if k1>=(10**9):
 print(-1)

else:
 print(k1)