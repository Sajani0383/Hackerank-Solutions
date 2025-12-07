# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
words=[]
count={}
for _ in range(n):
    w=input().strip()
    if w not in count:
        words.append(w)
    count[w]=count.get(w,0)+1
print(len(words))
print(*[count[w] for w in words])
