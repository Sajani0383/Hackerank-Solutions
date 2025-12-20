# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan,degrees
ab=int(input())
bc=int(input())
theta=round(degrees(atan(ab/bc)))
print(theta,chr(176),sep='')