# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
print(*sorted(s,key=lambda x:(x.isdigit(),x.isdigit() and int(x) % 2==0,x.isupper () ,x)),sep='')