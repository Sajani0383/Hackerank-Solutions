# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
fields=input().split()
Student=namedtuple('Student',fields)
total=0
for _ in range(n):
    data=input().split()
    student=Student(*data)
    total+=int(student.MARKS)
print(total/n)