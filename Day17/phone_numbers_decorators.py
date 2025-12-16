def wrapper(f):
    def fun(l):
        formatted=[]
        for num in l:
            n=num[-10:]
            formatted.append("+91 {} {}".format(n[:5],n[5:]))
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 