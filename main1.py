#1. create a list of dictionaries with name and age of 5 people. use lambda function to filter out people under 18 and map the remaining people names to a new list.

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30},
    {"name": "David", "age": 15},
    {"name": "Eve", "age": 22}
]
adults = list(filter(lambda a: a['age'] >= 18, people))
adult_names = list(map(lambda a: a['name'], adults))
print(adult_names)

#2.Use reduce function and lambda expression to calculate the product of all numbers in a list.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)


# 3. Square of even numbers in a list using lambda function and list comprehension
n = list(map(int, input().split()))          # Read integers
is_even = lambda x: x % 2 == 0               # Lambda to check even
q = [x**2 for x in n if is_even(x)]          # Squares of evens
print(q)

#4. write a lambda function to check if the given string is a number
n = input()
is_number = lambda s: s.isdigit()
print(is_number(n)) 

#5. Use lambda funtion to extract year, month and day from datetime object
import datetime
now = datetime.datetime.now()
extract_date = lambda dt: (dt.year, dt.month, dt.day)
print(extract_date(now)) 

#6. create a lambda function to generate fibonacci series up to n terms

n = int(input("Enter the number of terms: "))
# Recursive lambda for Fibonacci series
fibonacci = lambda n: [0, 1][:n] if n <= 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-2)[-1]]
print(*fibonacci(n))
