import math
import string


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def reverse_array(arr: list) -> list:
    right, left = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        right += 1
        left -= 1


def find_largest(arr: list) -> int:
    return max(arr)


def find_smallest(arr: list) -> int:
    return min(arr)


def reverse_string(word) -> str:
    return word[::-1]


def find_min_max(arr: list):
    pass


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    counter = 0
    for c in s:
        if c in vowels:
            counter += 1

    return counter


def replace_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    for c in s:
        if c in vowels:
            s = s.replace(c, '*')
    return s


def missing_number(arr: list, N: int) -> int:
    pass


def sum_list(arr: list) -> int:
    pass


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n: int):
    fibo = [0, 1]

    for i in range(1, n):
        fibo.append(fibo[i-1] + fibo[i])
    # fibo.pop(0)
    return fibo


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_anagram(str1: str, str2: str) -> bool:
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


def count_words(sentence: str) -> int:
    pass


def reverse_words(sentence: str) -> str:
    pass


def second_largest(numbers: list) -> int:
    pass


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def find_duplicates(numbers: list) -> list:
    pass


def is_perfect_number(num: int) -> bool:
    pass


def is_power_of_two(num: int) -> bool:
    pass


if __name__ == '__main__':
    # print(is_palindrome("racecar"))  # Output: True
    # print(is_palindrome("raccar"))  # Output: False
    # print(find_largest([1, 3, 7, 2, 5, 11, 0]))  # Output: 7
    # print(is_prime(74))
    # print(count_vowels('leila'))
    # print(replace_vowels('leila cheshmi'))
    # print(missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10], 10))
    # print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(fibonacci(10))
    # print(fibonacci_iterative(10))
    # print(is_anagram('sima', 'misa'))
    # print(count_words("This is a simple sentence is num again."))
    # print(second_largest([10, 20, 4, 45, 99, 20, 100]))
    # print(reverse_words("Hello World leila"))  # Output: "World Hello"
    # print(factorial(7))
    # print(find_duplicates([1, 2, 3, 4, 2, 3, 5]))  # Output: [2, 3]
    #
    # print(is_perfect_number(6))  # Output: True (6 = 1 + 2 + 3)
    # print(is_perfect_number(28))  # Output: True (28 = 1 + 2 + 4 + 7 + 14)
    #
    # print(is_power_of_two(16))  # Output: True
    # print(is_power_of_two(18))  # Output: False





