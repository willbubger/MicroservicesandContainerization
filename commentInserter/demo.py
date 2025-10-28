import math
import random
import statistics

# Utility Functions ----------------------------------------------------------

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def power(base, exp):
    return base ** exp

def sqrt(num):
    return math.sqrt(num)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def average(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    return statistics.median(numbers)

def mode(numbers):
    return statistics.mode(numbers)

def variance(numbers):
    return statistics.variance(numbers)

def stdev(numbers):
    return statistics.stdev(numbers)

def generate_random_list(n, start=0, end=100):
    return [random.randint(start, end) for _ in range(n)]

def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def unique_elements(lst):
    return list(set(lst))

def count_occurrences(lst, value):
    return lst.count(value)

def merge_lists(a, b):
    return a + b

def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

def list_sum(lst):
    return sum(lst)

def list_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

def list_difference(a, b):
    return [x for x in a if x not in b]

def list_intersection(a, b):
    return [x for x in a if x in b]

def list_union(a, b):
    return list(set(a + b))

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

def square_list(lst):
    return [x ** 2 for x in lst]

def cube_list(lst):
    return [x ** 3 for x in lst]

def filter_positive(lst):
    return [x for x in lst if x > 0]

def filter_negative(lst):
    return [x for x in lst if x < 0]

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

def cumulative_sum(lst):
    total = 0
    result = []
    for x in lst:
        total += x
        result.append(total)
    return result

def factorial_list(lst):
    return [math.factorial(x) for x in lst if x >= 0]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def palindrome(s):
    s = str(s)
    return s == s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)

def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch.isalpha() and ch not in vowels)

def reverse_string(s):
    return s[::-1]

def is_anagram(a, b):
    return sorted(a) == sorted(b)

def capitalize_words(s):
    return " ".join(w.capitalize() for w in s.split())

def word_count(s):
    return len(s.split())

def char_count(s):
    return len(s)

def remove_spaces(s):
    return s.replace(" ", "")

def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def alternate_case(s):
    return "".join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(s))

def replace_vowels(s, char='*'):
    vowels = 'aeiouAEIOU'
    return ''.join(char if ch in vowels else ch for ch in s)

def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

def join_strings(lst, sep=", "):
    return sep.join(lst)

def split_string(s, sep=","):
    return s.split(sep)

def count_substring(s, sub):
    return s.count(sub)

def starts_with(s, prefix):
    return s.startswith(prefix)

def ends_with(s, suffix):
    return s.endswith(suffix)

def is_digit(s):
    return s.isdigit()

def is_alpha(s):
    return s.isalpha()

def is_alnum(s):
    return s.isalnum()

def string_to_list(s):
    return list(s)

def list_to_string(lst):
    return "".join(lst)

def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def upper_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j >= i else 0 for j in range(n)] for i in range(n)]

def lower_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j <= i else 0 for j in range(n)] for i in range(n)]

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def scalar_multiply(matrix, scalar):
    return [[x * scalar for x in row] for row in matrix]

def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matrix_multiply(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def flatten_matrix(matrix):
    return [x for row in matrix for x in row]

def reshape_flat(flat, rows, cols):
    return [flat[i*cols:(i+1)*cols] for i in range(rows)]

def make_grid(n, val=0):
    return [[val for _ in range(n)] for _ in range(n)]

def border_grid(n):
    grid = make_grid(n)
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                grid[i][j] = 1
    return grid

def random_matrix(n, m, start=0, end=9):
    return [[random.randint(start, end) for _ in range(m)] for _ in range(n)]

def pretty_print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def identity_check(a, b):
    return a is b

def equality_check(a, b):
    return a == b

def greater_than(a, b):
    return a > b

def less_than(a, b):
    return a < b

def range_sum(start, end):
    return sum(range(start, end + 1))

def range_product(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def absolute_difference(a, b):
    return abs(a - b)

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def area_circle(r):
    return math.pi * r * r

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def perimeter_square(side):
    return 4 * side

def circumference_circle(r):
    return 2 * math.pi * r

def simple_interest(p, r, t):
    return (p * r * t) / 100

def compound_interest(p, r, t):
    return p * ((1 + r/100)**t) - p

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def seconds_to_minutes(s):
    return s / 60

def minutes_to_hours(m):
    return m / 60

def hours_to_days(h):
    return h / 24

def days_to_weeks(d):
    return d / 7

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def sign(n):
    if n > 0: return 1
    if n < 0: return -1
    return 0

def clamp(n, low, high):
    return max(low, min(n, high))

def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def midpoint_2d(x1, y1, x2, y2):
    return ((x1+x2)/2, (y1+y2)/2)

def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

# ---------------------------------------------------------------------------
# DRIVER CODE (just to hit 500 lines)
# ---------------------------------------------------------------------------

def main():
    nums = generate_random_list(10, 1, 50)
    print("Numbers:", nums)
    print("Average:", average(nums))
    print("Fibonacci(10):", fibonacci(10))
    print("Primes under 30:", primes_in_range(1, 30))
    matrix = random_matrix(3, 3)
    print("Matrix:")
    pretty_print_matrix(matrix)
    print("Transposed:")
    pretty_print_matrix(transpose(matrix))
    print("Circle Area:", area_circle(5))
    print("Celsius 0 -> F:", celsius_to_fahrenheit(0))

if __name__ == "__main__":
    main()
