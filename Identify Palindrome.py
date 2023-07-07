"""Sample Input 1
124

Sample Output 1
545

Explanation 1
The sum of 124 and its reverse 421 is 545 which is a palindrome.
 """


def isPalindrome(n):
    return str(n)[::-1]==str(n)
def rev(n):
    return int(str(n)[::-1])
n=int(input())
while(1):
    n=n+rev(n)
    if(isPalindrome(n)):
        print(n)
        break