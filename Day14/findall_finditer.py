# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
s=input()
matches=re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])',s)
if matches:
    for m in matches:
        print(m)
else:
    print(-1)