import numpy as np 
n=int(input())
a=[list(map(float,input().split())) for _ in range(n)]
det=np.linalg.det(a) 
print(round(det,2))