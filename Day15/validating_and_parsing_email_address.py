# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
pattern=re.compile(r'<[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>')
for _ in range(n):
    line=input().strip()
    name,email=line.split()
    if pattern.fullmatch(email):
        print(line)