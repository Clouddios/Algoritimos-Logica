def fib(i):
    """ Retorna os i-éssimos números de Fibonacci
        fib(n)
    """
    if i == 0 or i == 1:
        return i
    else:
        return fib(i-1) + fib(i-2)

# for i in range(0, 30):
#     print(fib(i), end=" ")
