import numpy as np 
coeffs=list(map(float,input().split()))
x=float(input())
print(np.polyval(coeffs,x))