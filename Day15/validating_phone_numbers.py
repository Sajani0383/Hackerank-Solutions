# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
for _ in range(n):
    s=input().strip()
    if re.fullmatch(r'[789]\d{9}',s):
        print("YES")
    else:
        print("NO")