# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=int(input().strip())
letters=input().split()
k=int(input().strip())
all_combos=list(combinations(letters,k))
total=len(all_combos)
favourable=sum(1 for v in all_combos if 'a' in v)
print("{:.3f}".format(favourable/total))  