# Enter your code here. Read input from STDIN. Print output to STDOUT
K=int(input())
room_numbers=list(map(int,input().split()))
seen_once=set()
seen_multiple=set()
for room in room_numbers:
    if room in seen_once:
        seen_multiple.add(room)
        seen_once.discard(room)
    else:
        if room not in seen_multiple:
            seen_once.add(room)
print(seen_once.pop())