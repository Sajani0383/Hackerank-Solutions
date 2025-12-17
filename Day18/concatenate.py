import numpy as np
n, m, p = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(m)])
print(np.concatenate((a, b), axis=0))