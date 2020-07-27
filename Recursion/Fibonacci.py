def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# @param {integer} No. of the elements in fibonacci series 
for x in range(7):
    print(fib(x),end=", ")
