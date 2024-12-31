#! python3
# a program that creates a list of all the numbers that are factors of the users number

# function to check if number is odd or even

def factoring_function(num):
    print(f'factoring {num} ...')
    factors = list()
    if num == 1:
        print(f'factor of {num} is only {num} itself')
        return num
    elif num == 0:
        return (f'{num} cant be factored')
    else:
        for i in range(2, abs(num) + 1):
            if abs(num) % i == 0:
                factors.append(i)
        else:
            factors.insert(0, 1)
        # if the num is only divisible by itself and 1 it's a prime number
        if len(factors) == 2:
            print(f'the number {num} is a prime number')
    # generate negative factors for negative input number
    if num < 0:
        negative_factors = [(number * -1) for number in factors]
        factors = sorted(factors + negative_factors)

    # generate a prettified string from the list
    string_output = ', '.join(str(number) for number in factors)

    return string_output


print(factoring_function(36))
print(factoring_function(-36))
print(factoring_function(5))