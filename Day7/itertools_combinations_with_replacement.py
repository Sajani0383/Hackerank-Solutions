# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s,k=input().split()
k=int(k)
s=''.join(sorted(s))
for combo in combinations_with_replacement(s,k):
    print(''.join(combo))