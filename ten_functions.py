# 1
import math


def largest_three_numbers():
    a, b, c = 192, 77, 20
    max = a
    if b > max and b > c:
        max = b
    elif c > max and c > b:
        max = c

    return max


# 2
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# 3
def compound_interest():
    principal = 2300
    rate = 7
    times = 4
    years= 2
    # math.pow(base, exponent)
    total = principal * (1 + rate/times) ** (times * years)
    CI = total - principal
    return CI, total


# 4
def swap_two_numbers(num1, num2):

    print(num1, num2)
    sum = num1 + num2
    num1 = sum - num1
    num2 = sum - num2
    print(num1, num2)


# 5
def replace_zero():
    num = 10203040
    replace_number = int(str(num).replace('0', '1'))
    print(replace_number)


# 6
def binary_to_decimal():
    pass


#7
def is_leap_year(year: int):
    if year % 400 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year} is not a leap year")
    elif year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


# 8
def factorial(num: int):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


# 9
def is_armstrong(num: int):
    origin_num = num
    num_digit = 1
    digit = 0
    sum_digit = 0
    # find number of digit
    while num > 10:
        num_digit += 1
        num /= 10

    num = origin_num
    while num > 0:
        digit = int(num%10)
        sum_digit = sum_digit + math.pow(digit, num_digit)
        num /= 10

    if origin_num == sum_digit:
        print(f"{origin_num} is armstrong")
    else:
        print(f"{origin_num} is not armstrong")


def py_armstrong(num: int):
    str_num = str(num)
    num_digit = len(str_num)
    sum_digit = 0

    for dig in str_num:
        sum_digit += int(dig) ** num_digit

    if sum_digit == num:
        print(f"{num} is armstrong")
    else:
        print(f"{num} is not armstrong")


# 10
def find_roots(num: int):
    square_root = math.pow(num, 1/2)
    # square_root = num ** (1/2)
    print(square_root)


if __name__ == '__main__':
    # print(largest_three_numbers())
    # swap_two_numbers(10, 11)
    # replace_zero()
    # is_leap_year(2009)
    # print(factorial(5))
    # find_roots(2500)
    # is_armstrong(153)
    py_armstrong(153)
