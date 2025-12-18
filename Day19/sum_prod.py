# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np 
n,m=map(int,input().split())
a=np.array([list(map(int,input().split())) for _ in range(n)])
print(np.prod(np.sum(a,axis=0)))