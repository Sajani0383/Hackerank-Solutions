# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for _ in range(T):
    a,b=input().split()
    try:
        print(int(a)//int(b))
    except(ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)