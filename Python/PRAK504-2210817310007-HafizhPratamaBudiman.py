def reverse(n,rev = 0):
    rev = 0
    while (n!=0) :
        rev*=10
        rev+=n%10
        n//=10
    return rev 

A,B = input().split()
A=reverse(int(A))
B=reverse(int(B))
C=A+B
print(reverse(C))