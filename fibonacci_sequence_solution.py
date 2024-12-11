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


def fib_recursive(n):
    if n <= 0:
        print("Incorrect input")
    if n == 1:
        return 0
        # first fibonacci number is 0
    elif n == 2:
        return 1
        # second fibonacci number is 1
    else:
        result = fib_recursive(n - 1) + fib_recursive(n - 2)
        # print(result)
    return result


print(fib_recursive(5))

# function to find nth fibonacci number with memoization (dynamic programming)
fib_array = [0, 1]  # initiate array with the first 2 fibonacci numbers


def fibonacci_dynamic_programming(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(fib_array):
        # check if the nth number already exists in the array -
        # at first only 2 numbers exist so first recursive stack dives down to 1 + 0, adding 1 to the array,
        # the step up in recursive stack now has 3 numbers in the array aka the third fib number also exists
        return fib_array[n - 1]
    else:
        temp_fib = fibonacci_dynamic_programming(n - 1) + fibonacci_dynamic_programming(
            n - 2
        )
        fib_array.append(temp_fib)  # adds the fibonacci number
        # to the array (0,1,1,2,3,5...)
        return temp_fib  # returns the final number that is appended to the fib_array aka the nth fibonacci number


print(fibonacci_dynamic_programming(5))
