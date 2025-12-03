def print_rangoli(size):
    # your code goes here
    alpha='abcdefghijklmnopqrstuvwxyz'
    width=4*size-3
    lines=[]
    for i in range(size):
        left=alpha[size-1:size-1-i:-1]
        right=alpha[size-1-i:size]
        line="-".join(left+right)
        lines.append(line.center(width,"-"))
    print("\n".join(lines+lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)