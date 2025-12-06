# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
items=OrderedDict()
for _ in range(n):
    *name,price=input().split()
    item_name=" ".join(name)
    price=int(price)
    if item_name in items:
        items[item_name]+=price
    else:
        items[item_name]=price
for item,total in items.items():
    print(item,total)