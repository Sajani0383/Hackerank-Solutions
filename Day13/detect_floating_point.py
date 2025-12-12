# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
pattern=r'^[+-]?\d*\.\d+$'
for _ in range(n):
    s=input()
    print(bool(re.match(pattern,s)))