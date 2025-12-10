# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
n=int(input())
result=True
for _ in range(n):
    s=set(map(int,input().split()))
    if not(A>s):
        result=False
print(result)