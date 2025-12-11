# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x=map(int,input().split())
marks=[]
for _ in range(x):
    marks.append(list(map(float,input().split())))
for student in zip(*marks):
    avg=sum(student)/x
    print(f"{avg:.1f}")