#! python 3
# a program to find the nth term in fibonacci sequence


def fib_loop(n):
    num_1 = 1
    num_2 = 1
    loops = n
    result = 0
    while loops > 0:
        result = num_1 + num_2
        num_1 = num_2
        num_2 = result
        loops -= 1
    return result


print(fib_loop(10))


def fib_recursive(n, num_1, num_2):
    if n == 0:
        result = num_1 + num_2
    else:
        result = num_1 + fib_recursive(n - 1, num_1, num_2)
    return result


print(fib_recursive(10, 1, 1))
