cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[-1]+fib[-2])
    return fib[:n]
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))