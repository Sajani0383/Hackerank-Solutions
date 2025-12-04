# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S,k=input().split()
k=int(k)
result=sorted(permutations(S,k))
for p in result:
    print(''.join(p))