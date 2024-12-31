#! python3
# a program to find a number between 1 and 1000 that fits the following criteria:
"""
* The number has two or more digits.
* The number is prime.
* The number does NOT contain a 1 or 7 in it.
* The sum of all of the digits is less than or equal to 10.
*The first two digits add up to be odd.
* The second to last digit is even and greater than 1.
The last digit is equal to how many digits are in the number.
"""


# function to check the digits

def check_digits(num):
    digits = [i for i in str(num)]
    if len(digits) >= 2:
        if ('7' in digits) or ('1' in digits):
            print(f'{num} has a 7 or 1 in it, incorrect')
            return False
        else:
            sum = int()
            for digit in digits:
                sum += int(digit)
            if sum <= 10:
                # if the sum of first two digits divided by 2 leaves reminder of 0
                # it is odd and the program proceeds
                if ((int(digits[0]) + int(digits[1])) % 2) != 0:
                    # check if second to last digit is even  and greater then 1
                    if int(digits[-2]) % 2 == 0 and int(digits[-2]) > 1:
                        # check if the last digit is equal to the digits in the number
                        if int(digits[-1]) == len(digits):
                            return True
                        else:
                            print(f'the last digit {digits[-1]} is not equal to the amount of digits in the number')
                            return False
                    else:
                        print(f'Second to last digit {digits[-2]} is not even or its greater than 1')
                        return False
                else:
                    print(f'the first two digits {digits[0]} and {digits[1]} summed is an even number, incorrect')
                    return False
                    # check if second to last digit is even and greater than 1

            else:
                print(f'sum of digits in {num} is larger that 10, incorrect')
                return False
    else:
        return False


# function to check if the number is a prime number
def check_prime(num):
    # negative numbers, 0 and 1 are not primes
    if num > 1:
        # iterate from 2 to n // 2 (floor division)
        # if num is divisible without remainder by any number between
        # 2 and n // 2, it is not prime
        for i in range(2, (num // 2) + 1):
            if (num % i) == 0:
                # print(f'{num} is not a prime number, divisible by {i}')
                return False
        # if the number was not divisible by anything then its a prime number
        else:
            # print(f'{num} is a prime number')
            return True
    else:
        # print(f'{num} is not a prime number')
        return False


def main_loop():
    for num in range(1, 1001):
        if check_prime(num) and check_digits(num):
            print(f'{num} found!')
            return num
    else:
        return False


main_loop()