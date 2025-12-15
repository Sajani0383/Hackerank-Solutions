# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for _ in range(t):
    uid = input().strip()

    if len(uid) != 10:
        print("Invalid")
        continue

    if not uid.isalnum():
        print("Invalid")
        continue

    if len(set(uid)) != 10:
        print("Invalid")
        continue

    if len(re.findall(r'[A-Z]', uid)) < 2:
        print("Invalid")
        continue

    if len(re.findall(r'\d', uid)) < 3:
        print("Invalid")
        continue

    print("Valid")