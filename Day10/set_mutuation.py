# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int,input().split()))
num_other_sets=int(input())
for _ in range(num_other_sets):
    command,size=input().split()
    other_set=set(map(int,input().split()))
    if command=='intersection_update':
        A.intersection_update(other_set)
    elif command=='update':
        A.update(other_set)
    elif command=='symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif command=='difference_update':
        A.difference_update(other_set)
print(sum(A))