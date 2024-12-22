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


# 16
def reverse_list(data: list):
    start = 0
    end = len(data) - 1
    while start < end:
        data[start], data[end] = data[end], data[start]
        start += 1
        end -= 1
    return data


# 17
def find_repeated_data(data: list):
    counter_data = {}
    repeated_data = []

    for item in data:
        if item in counter_data:
            counter_data[item] += 1
        else:
            counter_data[item] = 1

    for k, v in counter_data.items():
        if v > 1:
            repeated_data.append(k)

    print(counter_data)
    print(repeated_data)


# 18
def find_repeated_data_with_set(data: list):
    seen = set()
    repeated = set()

    for item in data:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)

    print(seen)
    print(repeated)


# 19
def find_repeated_words(data: str, my_word: str):
    counter = 0
    # splits the string into a list of words
    words = data.lower().split()
    my_word = my_word.lower()
    for word in words:
        if word == my_word:
            counter += 1

    print(f'{my_word} is repeated {counter} times in this text')


# 20
def sort_asc_desc(data: list):
    size = len(data)
    start = 0
    end = size // 2

    def sort_asc(start, end):
        for i in range(start, end):
            for j in range(i, end):
                if data[i] > data[j]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp

    sort_asc(start, end)
    print(data)

    def sort_desc(start, end):
        for i in range(start, end):
            for j in range(i, end):
                if data[i] < data[j]:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp

    start = size // 2
    end = size
    sort_desc(start, end)
    print(data)


# 20_1
def asc_desc_sort(data: list):
    mid = len(data) // 2
    first_half = data[:mid]
    second_half = data[mid:]

    first_half.sort()
    second_half.sort(reverse=True)

    # combine = first_half + second_half
    first_half.extend(second_half)

    print(first_half)


if __name__ == '__main__':

    # reversed_number = reverse_number(1234)
    # print("Reversed number:", reversed_number)

    # is_palindrome(123421)
    # print(find_gcd(98, 56))
    # print(find_lcd(12, 9))
    # print(pyramid_pattern(5))
    # print(reverse_list([1,2,3,4,5,6,7]))
    # find_repeated_data([11,1,2,2,3,1,7,7,7,8,2,9])
    # find_repeated_data_with_set([11, 1, 2, 2, 3, 1, 7, 7, 7, 8, 2, 9])
    # find_repeated_data(['leila', 'lili', 'didi', 'lili', 'miki', 'miki', 'hali'])
    # find_repeated_words('I am here for you not for him please you You am here listen', 'you')

    print(sort_asc_desc([50, 10, 70, 20, 30, 90, 112]))
    print('************')
    asc_desc_sort([50, 10, 70, 20, 30, 90, 112])
