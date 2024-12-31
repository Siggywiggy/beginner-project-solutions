#! python3
# a program to convert a number from one base to another - binary to hexadecimal
import pyinputplus as pyip


# a function to convert any number in any base to decimal
def to_decimal(number, base):
    # separating the digits in to a list of digits
    # using the optional parameter in int() method to convert alphabetical notation to a number for calculation (A-F)
    digits = [int(x, base) for x in str(number)]
    # reverse the digits to prepare for a for loop from 0 to len(number), could also reverse the range instead
    digits.reverse()
    result = int()
    # for loop to calculate each value of digit * base value ** exponent and sum in to result variable
    for x in range(0, len(str(number))):
        result += int(digits[x]) * base ** x

    return int(str(result), 10)


# a function to convert from decimal number to any base


def from_decimal_to_base(number, to_base):
    # if the number is already in decimal cant convert to decimal again
    if base == 10:
        print("Number is already in decimal, no need to convert to decimal again")
        return number

    number = int(number)
    result = str()

    while True:
        # find both quotient and remainder at once with divmod() method
        quotient, remainder = divmod(number, base)
        # or longer
        # quotient = number // base
        # remainder =  number % base

        # if the quotient == 0 then the remainder is 1
        if quotient == 0:
            result += str(remainder)
            # no need to further find the quotient as we have reached the final digit
            break
        else:
            # keep adding the remainder to the result
            result += str(remainder)
            # keep looping over the quotient
            number = quotient
    # negative slice of a string is reversed string - digits in correct order
    return int(str(result[::-1]))


def validity_checker(number, base):
    # cant convert to base 0
    if base == 0:
        print(f"incorrect base value {base}")
        return False
    # a list of valid digits in bases 2 - 16
    all_digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    # current valid base digits - a slice of all_digits
    valid_digits = all_digits[:base]
    # digits of the number we are checking
    digits_list = [x for x in str(number)]
    # check every digit against all digits in valid_digits
    for x in digits_list:
        if x not in valid_digits:
            return False

    # convert number to string, try converting back to integer using int()
    try:
        int(str(number), base)
    except ValueError:
        print(f"The number {number} is not in correct base - {base} ")
        return False
    else:
        return True


while True:

    number = pyip.inputNum(
        prompt="Please input the number you want to convert, in base 2-16: \n",
        allowRegexes=[r"^[0-9A-F]+$"],
    )

    from_base = pyip.inputInt(
        prompt="What base is the number in - please input a base between 2 and 16: \n",
        greaterThan=1,
        lessThan=17,
    )

    to_base = pyip.inputInt(
        prompt="What base to convert to - please input a base between 2 and 16: \n",
        greaterThan=1,
        lessThan=17,
    )
    # if the number is a number in the base it was declared to be in
    if validity_checker(number, from_base):
        if from_base == 10:
            result = from_decimal_to_base(number, to_base)
            print(
                f"number {number} in base {from_base} converted to base {to_base} is {result}"
            )
        elif to_base == 10:
            result = to_decimal(number, from_base)
            print(
                f"number {number} in base {from_base} converted to base {to_base} is {result}"
            )
        else:
            result = from_decimal_to_base(to_decimal(number, from_base), to_base)
            print(
                f"number {number} in base {from_base} converted to base {to_base} is {result}"
            )
    else:
        print("Number was incorrect, try again")
