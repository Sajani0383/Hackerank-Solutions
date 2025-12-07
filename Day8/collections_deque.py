# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    cmd=input().split()
    if cmd[0]=="append":
        d.append(int(cmd[1]))
    elif cmd[0]=="appendleft":
        d.appendleft(int(cmd[1]))
    elif cmd[0]=="pop":
        if d:
            d.pop()
    elif cmd[0]=="popleft":
        if d:
            d.popleft()
print(*d)