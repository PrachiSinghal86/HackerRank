# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    a,b,n=input().split()
    n=int(n)
    a1=a
    b1=b
    c1=a+b
    while(len(c1)<n):
        x=c1
        c1=b1+c1
        b1=x
    print(c1[n-1])
