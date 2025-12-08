# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t=int(input().strip())
for  _ in range(t):
    n=int(input().strip())
    blocks=deque(map(int,input().split()))
    last=float('inf')
    possible=True
    while blocks:
        if blocks[0]<=last and blocks[-1]<=last:
            if blocks[0]>=blocks[-1]:
                last=blocks.popleft()
            else:
                last=blocks.pop()
        elif blocks[0]<=last:
            last=blocks.popleft()
        elif blocks[-1]<=last:
            last=blocks.pop()
        else:
            possible=False
            break
    print("Yes" if possible else "No")                                
 