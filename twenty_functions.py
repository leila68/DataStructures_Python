# 11
import math


def reverse_number(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
        num //= 10  # // Floor Division: It rounds the result and / True Division
    return reversed_num


# 12
def is_palindrome(num: int):
    rev_num = reverse_number(num)
    if rev_num == num:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")


# 13
def find_gcd(num1, num2):
    gcd_val = num1 if num1 < num2 else num2
    while gcd_val > 0:
        if num1 % gcd_val == 0 and num2 % gcd_val == 0:
            return gcd_val
        gcd_val -= 1

    return gcd_val


# 14
def find_lcd(num1, num2):
    gcd_val = find_gcd(num1, num2)
    lcd_val = abs(num1 * num2) // gcd_val
    return lcd_val


# 15
def pyramid_pattern(N: int):
    for i in range(1, N+1):
        for j in range(1, N-i+1):
            print(" ", end='')
        for k in range(1, 2*i):
            print("*", end='')
        print('')
    return "Pattern Completed" # to avoid print None


if __name__ == '__main__':

    # reversed_number = reverse_number(1234)
    # print("Reversed number:", reversed_number)

    # is_palindrome(123421)
    # print(find_gcd(98, 56))
    # print(find_lcd(12, 9))
    print(pyramid_pattern(5))