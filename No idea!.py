# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
n = int(n)
m = int(m)
a = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = 0
if n <= 2 * m:
    for i in range(n):
        if A.count(a[i]) > 0:
            c = c + A.count(a[i])

        elif B.count(a[i]) > 0:
            c = c - B.count(a[i])
else:
    for i in range(m):
        if a.count(A[i]) == 1:
            c = c + 1
        if a.count(B[i]) == 1:
            c = c - 1

print(c)

