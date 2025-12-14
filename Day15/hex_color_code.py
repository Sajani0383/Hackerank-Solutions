# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
pattern=re.compile(r'(?<!^)(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))')
for _ in range(n):
    line=input()
    matches=pattern.findall(line)
    for m in matches:
        print(m)