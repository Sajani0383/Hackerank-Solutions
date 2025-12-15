# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 
n=int(input())
for _ in range(n):
    card=input().strip()
    pattern=r'^(4|5|6)\d{3}(-?\d{4}){3}$'
    repeat=r'(\d)(-?\1){3,}'
    if re.match(pattern,card )and not re.search(repeat,card):
        print("Valid")
    else:
        print("Invalid")     