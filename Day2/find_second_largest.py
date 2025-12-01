if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    m=list(set(arr))
    m.remove(max(m))
    print(max(m))
