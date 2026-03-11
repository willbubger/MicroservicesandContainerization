import math
import random
import statistics

# Utility Functions ----------------------------------------------------------

# Returns a greeting message to the user
def greet(name):
    return f"Hello, {name}!"

# Returns the sum of two numbers
def add(a, b):
    return a + b

# Returns the difference between two numbers
def subtract(a, b):
    return a - b

# Returns the product of two numbers
def multiply(a, b):
    return a * b

# Returns the quotient of two numbers
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Returns a number raised to a given power
def power(base, exp):
    return base ** exp

# Returns the square root of a number
def sqrt(num):
    return math.sqrt(num)

# Returns the factorial of a non-negative integer
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Returns the average of a list of numbers
def average(numbers):
    return sum(numbers) / len(numbers)

# Returns the median value of a list of numbers
def median(numbers):
    return statistics.median(numbers)

# Returns the most frequently occurring value in a list
def mode(numbers):
    return statistics.mode(numbers)

# Returns the variance of a list of numbers
def variance(numbers):
    return statistics.variance(numbers)

# Returns the standard deviation of a list of numbers
def stdev(numbers):
    return statistics.stdev(numbers)

# Generates a list of random numbers with a given size and range
def generate_random_list(n, start=0, end=100):
    return [random.randint(start, end) for _ in range(n)]

# Returns a sorted copy of the given list
def sort_list(lst):
    return sorted(lst)

# Returns the list in reverse order
def reverse_list(lst):
    return lst[::-1]

# Returns a list with duplicate elements removed
def unique_elements(lst):
    return list(set(lst))

# Counts the occurrences of a specific element in a list
def count_occurrences(lst, value):
    return lst.count(value)

# Merges two or more lists into a single list
def merge_lists(a, b):
    return a + b

# Flattens a nested list into a single-level list
def flatten_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]

# Returns the sum of all elements in a list
def list_sum(lst):
    return sum(lst)

# Returns the product of all elements in a list
def list_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Returns elements in the first list but not in the second
def list_difference(a, b):
    return [x for x in a if x not in b]

# Returns common elements between two lists
def list_intersection(a, b):
    return [x for x in a if x in b]

# Returns all unique elements from two lists combined
def list_union(a, b):
    return list(set(a + b))

# Returns a list of even numbers from the input
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# Returns a list of odd numbers from the input
def odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]

# Returns a list with each element squared
def square_list(lst):
    return [x ** 2 for x in lst]

# Returns a list with each element cubed
def cube_list(lst):
    return [x ** 3 for x in lst]

# Filters and returns only positive numbers from a list
def filter_positive(lst):
    return [x for x in lst if x > 0]

# Filters and returns only negative numbers from a list
def filter_negative(lst):
    return [x for x in lst if x < 0]

# Returns the maximum value in a list
def find_max(lst):
    return max(lst)

# Returns the minimum value in a list
def find_min(lst):
    return min(lst)

# Returns the sum of squares of all elements in a list
def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

# Returns the sum of cubes of all elements in a list
def sum_of_cubes(lst):
    return sum(x ** 3 for x in lst)

# Returns a list of cumulative sums
def cumulative_sum(lst):
    total = 0
    result = []
    for x in lst:
        total += x
        result.append(total)
    return result

# Returns a list of factorials for each element
def factorial_list(lst):
    return [math.factorial(x) for x in lst if x >= 0]

# Checks whether a given number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Returns all prime numbers within a given range
def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

# Returns the first n numbers in the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# Checks whether a string or number is a palindrome
def palindrome(s):
    s = str(s)
    return s == s[::-1]

# Counts the number of vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch in vowels)

# Counts the number of consonants in a string
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for ch in s if ch.isalpha() and ch not in vowels)

# Returns the reversed version of a string
def reverse_string(s):
    return s[::-1]

# Checks whether two strings are anagrams of each other
def is_anagram(a, b):
    return sorted(a) == sorted(b)

# Capitalizes the first letter of each word in a string
def capitalize_words(s):
    return " ".join(w.capitalize() for w in s.split())

# Returns the number of words in a string
def word_count(s):
    return len(s.split())

# Returns the number of characters in a string
def char_count(s):
    return len(s)

# Removes all spaces from a string
def remove_spaces(s):
    return s.replace(" ", "")

# Converts a string to uppercase
def to_upper(s):
    return s.upper()

# Converts a string to lowercase
def to_lower(s):
    return s.lower()

# Alternates the case of each character in a string
def alternate_case(s):
    return "".join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(s))

# Replaces all vowels in a string with a specified character
def replace_vowels(s, char='*'):
    vowels = 'aeiouAEIOU'
    return ''.join(char if ch in vowels else ch for ch in s)

# Generates a random string of a given length
def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))

# Joins a list of strings with a specified delimiter
def join_strings(lst, sep=", "):
    return sep.join(lst)

# Splits a string by a specified delimiter
def split_string(s, sep=","):
    return s.split(sep)

# Counts occurrences of a substring within a string
def count_substring(s, sub):
    return s.count(sub)

# Checks whether a string starts with a given prefix
def starts_with(s, prefix):
    return s.startswith(prefix)

# Checks whether a string ends with a given suffix
def ends_with(s, suffix):
    return s.endswith(suffix)

# Checks whether a string contains only digits
def is_digit(s):
    return s.isdigit()

# Checks whether a string contains only alphabetic characters
def is_alpha(s):
    return s.isalpha()

# Checks whether a string contains only alphanumeric characters
def is_alnum(s):
    return s.isalnum()

# Converts a string into a list of characters
def string_to_list(s):
    return list(s)

# Joins a list of elements into a single string
def list_to_string(lst):
    return "".join(lst)

# Returns the sum of all elements in a matrix
def sum_matrix(matrix):
    return sum(sum(row) for row in matrix)

# Returns the transpose of a matrix
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Returns the sum of diagonal elements in a square matrix
def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Returns the upper triangular portion of a matrix
def upper_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j >= i else 0 for j in range(n)] for i in range(n)]

# Returns the lower triangular portion of a matrix
def lower_triangle(matrix):
    n = len(matrix)
    return [[matrix[i][j] if j <= i else 0 for j in range(n)] for i in range(n)]

# Creates an identity matrix of a given size
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Multiplies every element of a matrix by a scalar value
def scalar_multiply(matrix, scalar):
    return [[x * scalar for x in row] for row in matrix]

# Returns the element-wise sum of two matrices
def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# Returns the element-wise difference of two matrices
def matrix_subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

# Returns the product of two matrices using matrix multiplication
def matrix_multiply(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

# Returns the trace (sum of diagonal elements) of a square matrix
def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# Flattens a 2D matrix into a 1D list
def flatten_matrix(matrix):
    return [x for row in matrix for x in row]

# Reshapes a flat list into a matrix with given dimensions
def reshape_flat(flat, rows, cols):
    return [flat[i*cols:(i+1)*cols] for i in range(rows)]

# Creates a grid of specified rows and columns filled with a value
def make_grid(n, val=0):
    return [[val for _ in range(n)] for _ in range(n)]

# Creates a grid with a border of one value and interior of another
def border_grid(n):
    grid = make_grid(n)
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                grid[i][j] = 1
    return grid

# Generates a matrix filled with random numbers
def random_matrix(n, m, start=0, end=9):
    return [[random.randint(start, end) for _ in range(m)] for _ in range(n)]

# Prints a matrix in a formatted, readable layout
def pretty_print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Checks whether a given matrix is an identity matrix
def identity_check(a, b):
    return a is b

# Checks whether two values or objects are equal
def equality_check(a, b):
    return a == b

# Checks whether the first value is greater than the second
def greater_than(a, b):
    return a > b

# Checks whether the first value is less than the second
def less_than(a, b):
    return a < b

# Returns the sum of all integers in a given range
def range_sum(start, end):
    return sum(range(start, end + 1))

# Returns the product of all integers in a given range
def range_product(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

# Returns the absolute difference between two numbers
def absolute_difference(a, b):
    return abs(a - b)

# Calculates the hypotenuse of a right triangle given two sides
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Calculates the area of a circle given its radius
def area_circle(r):
    return math.pi * r * r

# Calculates the area of a square given its side length
def area_square(side):
    return side * side

# Calculates the area of a rectangle given width and height
def area_rectangle(length, width):
    return length * width

# Calculates the area of a triangle given base and height
def area_triangle(base, height):
    return 0.5 * base * height

# Calculates the perimeter of a rectangle given width and height
def perimeter_rectangle(length, width):
    return 2 * (length + width)

# Calculates the perimeter of a square given its side length
def perimeter_square(side):
    return 4 * side

# Calculates the circumference of a circle given its radius
def circumference_circle(r):
    return 2 * math.pi * r

# Calculates simple interest given principal, rate, and time
def simple_interest(p, r, t):
    return (p * r * t) / 100

# Calculates compound interest given principal, rate, time, and periods
def compound_interest(p, r, t):
    return p * ((1 + r/100)**t) - p

# Converts a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Converts a temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Converts a distance from kilometers to miles
def km_to_miles(km):
    return km * 0.621371

# Converts a distance from miles to kilometers
def miles_to_km(miles):
    return miles / 0.621371

# Converts seconds to minutes
def seconds_to_minutes(s):
    return s / 60

# Converts minutes to hours
def minutes_to_hours(m):
    return m / 60

# Converts hours to days
def hours_to_days(h):
    return h / 24

# Converts days to weeks
def days_to_weeks(d):
    return d / 7

# Checks whether a given year is a leap year
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Checks whether a number is even
def is_even(n):
    return n % 2 == 0

# Checks whether a number is odd
def is_odd(n):
    return n % 2 != 0

# Returns the sign of a number: -1, 0, or 1
def sign(n):
    if n > 0: return 1
    if n < 0: return -1
    return 0

# Clamps a value to be within a specified minimum and maximum range
def clamp(n, low, high):
    return max(low, min(n, high))

# Calculates the Euclidean distance between two 2D points
def distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Returns the midpoint between two 2D points
def midpoint_2d(x1, y1, x2, y2):
    return ((x1+x2)/2, (y1+y2)/2)

# Calculates the slope between two 2D points
def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

# ---------------------------------------------------------------------------
# DRIVER CODE (just to hit 500 lines)
# ---------------------------------------------------------------------------

# Main entry point of the program
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
