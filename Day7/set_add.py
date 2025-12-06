# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
countries=set()
for _ in range(n):
    country=input().strip()
    countries.add(country)
print(len(countries))