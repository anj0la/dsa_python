def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

def fib_2(n, memo):
    if memo[n]:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_2(n - 1, memo) + fib_2(n - 2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)

def fib_bottom_up(n):
    if n <= 2:
        return 1
    
    bottom_up = [1 if i == 1 or i == 2 else 0 for i in range(n + 1)]
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
        
    return bottom_up[n]
        

def main(n):
    print(f'fib({n}) = {fib(n)}')
    print(f'fib_memo({n}) = {fib_memo(n)}')
    print(f'fib_bottom_up({n}) = {fib_bottom_up(n)}')

if __name__ == '__main__':
    main(5)
    
