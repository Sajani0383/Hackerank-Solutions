# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
eng_sub=set(map(int,input().split()))
b=int(input())
french_sub=set(map(int,input().split()))
sym_diff=eng_sub^french_sub
print(len(sym_diff))