"""1 <= N <= 10^3
1 <= A[i] <= 10^5
1 <= B[i] <= 10^5
Input Format for Custom Testing:

The first line contains an integer, N, denoting the number of elements in A.
Each line i of the N subsequent lines (where 0 <= i <= N) contains an integer describing Ai.
Each line i of the N subsequent lines (where 0 <= i <= N) contains an integer describing Bi.
Sample Test Cases

Sample Input 1
2
4
5
10
4
Sample Output 1
1"""

N=int(input())
people=[]
house=[]
#to read data of people and house arrays
for i in range(N): people.append(int(input()))
for i in range(N): house.append(int(input()))
count=0
for i in range(N):
    for j in range(N):
        if(people[i]<house[j]):
            count+=1
            house[j]=-1
            break
print(N-count)
print(N-count)