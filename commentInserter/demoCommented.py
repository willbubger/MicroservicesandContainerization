import math
import random
import statistics

# Utility Functions ----------------------------------------------------------

# This is the function: "greet"
def greet(name):
    return f"Hello, {name}!"

# This is the function: "add"
def add(a, b):
    return a + b

# This is the function: "subtract"
def subtract(a, b):
    return a - b

# This is the function: "multiply"
def multiply(a, b):
    return a * b

# This is the function: "divide"
def divide(a, b):
    if b == 0:
        return None
    return a / b

# This is the function: "power"
def power(base, exp):
    return base ** exp

# This is the function: "sqrt"
def sqrt(num):
    return math.sqrt(num)

# This is the function: "factorial"
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# This is the function: "average"
def average(numbers):
    return sum(numbers) / len(numbers)

# This is the function: "median"
def median(numbers):
    return statistics.median(numbers)

# This is the function: "mode"
def mode(numbers):
    return statistics.mode(numbers)

# This is the function: "variance"
def variance(numbers):
    return statistics.variance(numbers)

# This is the function: "stdev"
def stdev(numbers):
    return statistics.stdev(numbers)

# This is the function: "generate_random_list"
def generate_random_list(n, start=0, end=100):
    return [random.randint(start, end) for _ in range(n)]

# This is the function: "sort_list"
def sort_list(lst):
    return sorted(lst)

# This is the function: "reverse_list"
def reverse_list(lst):
    return lst[::-1]

# This is the function: "unique_elements"
def unique_elements(lst):
    return list(set(lst))

# This is the function: "count_occurrences"
def count_occurrences(lst, value):
    return lst.count(value)

# This is the function: "merge_lists"
def merge_lists(a, b):
    return a + b

# This is the function: "flatten_list"
def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# This is the function: "list_sum"
def list_sum(lst):
    return sum(lst)

# This is the function: "list_product"
def list_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# This is the function: "list_difference"
def list_difference(a, b):
    return [x for x in a if x not in b]

# This is the function: "list_intersection"
def list_intersection(a, b):
    return [x for x in a if x in b]

# This is the function: "list_union"
def list_union(a, b):
    return list(set(a + b))

# This is the function: "even_numbers"
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# This is the function: "odd_numbers"
def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

# This is the function: "square_list"
def square_list(lst):
    return [x ** 2 for x in lst]

# This is the function: "cube_list"
def cube_list(lst):
    return [x ** 3 for x in lst]

# This is the function: "filter_positive"
def filter_positive(lst):
    return [x for x in lst if x > 0]

# This is the function: "filter_negative"
def filter_negative(lst):
    return [x for x in lst if x < 0]

# This is the function: "find_max"
def find_max(lst):
    return max(lst)

# This is the function: "find_min"
def find_min(lst):
    return min(lst)

# This is the function: "sum_of_squares"
def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

# This is the function: "sum_of_cubes"
def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

# This is the function: "cumulative_sum"
def cumulative_sum(lst):
    total = 0
    result = []
    for x in lst:
        total += x
        result.append(total)
    return result

# This is the function: "factorial_list"
def factorial_list(lst):
    return [math.factorial(x) for x in lst if x >= 0]

# This is the function: "is_prime"
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# This is the function: "primes_in_range"
def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

# This is the function: "fibonacci"
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# This is the function: "palindrome"
def palindrome(s):
    s = str(s)
    return s == s[::-1]

# This is the function: "count_vowels"
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)

# This is the function: "count_consonants"
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch.isalpha() and ch not in vowels)

# This is the function: "reverse_string"
def reverse_string(s):
    return s[::-1]

# This is the function: "is_anagram"
def is_anagram(a, b):
    return sorted(a) == sorted(b)

# This is the function: "capitalize_words"
def capitalize_words(s):
    return " ".join(w.capitalize() for w in s.split())

# This is the function: "word_count"
def word_count(s):
    return len(s.split())

# This is the function: "char_count"
def char_count(s):
    return len(s)

# This is the function: "remove_spaces"
def remove_spaces(s):
    return s.replace(" ", "")

# This is the function: "to_upper"
def to_upper(s):
    return s.upper()

# This is the function: "to_lower"
def to_lower(s):
    return s.lower()

# This is the function: "alternate_case"
def alternate_case(s):
    return "".join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(s))

# This is the function: "replace_vowels"
def replace_vowels(s, char='*'):
    vowels = 'aeiouAEIOU'
    return ''.join(char if ch in vowels else ch for ch in s)

# This is the function: "random_string"
def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

# This is the function: "join_strings"
def join_strings(lst, sep=", "):
    return sep.join(lst)

# This is the function: "split_string"
def split_string(s, sep=","):
    return s.split(sep)

# This is the function: "count_substring"
def count_substring(s, sub):
    return s.count(sub)

# This is the function: "starts_with"
def starts_with(s, prefix):
    return s.startswith(prefix)

# This is the function: "ends_with"
def ends_with(s, suffix):
    return s.endswith(suffix)

# This is the function: "is_digit"
def is_digit(s):
    return s.isdigit()

# This is the function: "is_alpha"
def is_alpha(s):
    return s.isalpha()

# This is the function: "is_alnum"
def is_alnum(s):
    return s.isalnum()

# This is the function: "string_to_list"
def string_to_list(s):
    return list(s)

# This is the function: "list_to_string"
def list_to_string(lst):
    return "".join(lst)

# This is the function: "sum_matrix"
def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)

# This is the function: "transpose"
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# This is the function: "diagonal_sum"
def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# This is the function: "upper_triangle"
def upper_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j >= i else 0 for j in range(n)] for i in range(n)]

# This is the function: "lower_triangle"
def lower_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j <= i else 0 for j in range(n)] for i in range(n)]

# This is the function: "identity_matrix"
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# This is the function: "scalar_multiply"
def scalar_multiply(matrix, scalar):
    return [[x * scalar for x in row] for row in matrix]

# This is the function: "matrix_add"
def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# This is the function: "matrix_subtract"
def matrix_subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# This is the function: "matrix_multiply"
def matrix_multiply(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# This is the function: "trace"
def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# This is the function: "flatten_matrix"
def flatten_matrix(matrix):
    return [x for row in matrix for x in row]

# This is the function: "reshape_flat"
def reshape_flat(flat, rows, cols):
    return [flat[i*cols:(i+1)*cols] for i in range(rows)]

# This is the function: "make_grid"
def make_grid(n, val=0):
    return [[val for _ in range(n)] for _ in range(n)]

# This is the function: "border_grid"
def border_grid(n):
    grid = make_grid(n)
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                grid[i][j] = 1
    return grid

# This is the function: "random_matrix"
def random_matrix(n, m, start=0, end=9):
    return [[random.randint(start, end) for _ in range(m)] for _ in range(n)]

# This is the function: "pretty_print_matrix"
def pretty_print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# This is the function: "identity_check"
def identity_check(a, b):
    return a is b

# This is the function: "equality_check"
def equality_check(a, b):
    return a == b

# This is the function: "greater_than"
def greater_than(a, b):
    return a > b

# This is the function: "less_than"
def less_than(a, b):
    return a < b

# This is the function: "range_sum"
def range_sum(start, end):
    return sum(range(start, end + 1))

# This is the function: "range_product"
def range_product(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

# This is the function: "absolute_difference"
def absolute_difference(a, b):
    return abs(a - b)

# This is the function: "hypotenuse"
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# This is the function: "area_circle"
def area_circle(r):
    return math.pi * r * r

# This is the function: "area_square"
def area_square(side):
    return side * side

# This is the function: "area_rectangle"
def area_rectangle(length, width):
    return length * width

# This is the function: "area_triangle"
def area_triangle(base, height):
    return 0.5 * base * height

# This is the function: "perimeter_rectangle"
def perimeter_rectangle(length, width):
    return 2 * (length + width)

# This is the function: "perimeter_square"
def perimeter_square(side):
    return 4 * side

# This is the function: "circumference_circle"
def circumference_circle(r):
    return 2 * math.pi * r

# This is the function: "simple_interest"
def simple_interest(p, r, t):
    return (p * r * t) / 100

# This is the function: "compound_interest"
def compound_interest(p, r, t):
    return p * ((1 + r/100)**t) - p

# This is the function: "celsius_to_fahrenheit"
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# This is the function: "fahrenheit_to_celsius"
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# This is the function: "km_to_miles"
def km_to_miles(km):
    return km * 0.621371

# This is the function: "miles_to_km"
def miles_to_km(miles):
    return miles / 0.621371

# This is the function: "seconds_to_minutes"
def seconds_to_minutes(s):
    return s / 60

# This is the function: "minutes_to_hours"
def minutes_to_hours(m):
    return m / 60

# This is the function: "hours_to_days"
def hours_to_days(h):
    return h / 24

# This is the function: "days_to_weeks"
def days_to_weeks(d):
    return d / 7

# This is the function: "leap_year"
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# This is the function: "is_even"
def is_even(n):
    return n % 2 == 0

# This is the function: "is_odd"
def is_odd(n):
    return n % 2 != 0

# This is the function: "sign"
def sign(n):
    if n > 0: return 1
    if n < 0: return -1
    return 0

# This is the function: "clamp"
def clamp(n, low, high):
    return max(low, min(n, high))

# This is the function: "distance_2d"
def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# This is the function: "midpoint_2d"
def midpoint_2d(x1, y1, x2, y2):
    return ((x1+x2)/2, (y1+y2)/2)

# This is the function: "slope"
def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

# ---------------------------------------------------------------------------
# DRIVER CODE (just to hit 500 lines)
# ---------------------------------------------------------------------------

# This is the function: "main"
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
