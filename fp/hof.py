# filter(function, iterable)
# 
numbers = [-2, -1, 0, 1, 2]

positive = filter(lambda n: n > 0, numbers)

print(positive)

print(list(positive))

def is_positive(n):
    return n > 0

print(list(filter(is_positive, numbers)))

def extract_even(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)  
    return even_numbers

print(extract_even(numbers))

def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, numbers)))

print(list(filter(is_even, range(100))))

print(list(filter(lambda x: x > 50 , range(100))))

animals = ['ferret', 'vole', 'dog', 'cat', 'gecko']

print(list(filter(lambda x: 'o' in x, animals)))

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(is_prime, range(1, 51))))

import statistics as st

data = [10, 8, 10, 8, 2, 7, 9, 1, 45, 9, 6, 9, 100]

mean = st.mean(data)

print(mean)

stdev = st.stdev(data)
low = mean - 2*stdev
high = mean + 2*stdev

real_data = list(filter(lambda x: low <= x <= high, data))
print(real_data)
print(st.mean(real_data))

print(list(map(lambda x: x.upper(), animals)))

txns = [1.09, 23.56, 57.66, 4.66, 6.78]

TAX_RATE = .08

def price_with_tax(tx):
    return tx * (1 + TAX_RATE)

final_prices = map(price_with_tax, txns)

print(list(final_prices))


from functools import reduce

print(reduce(lambda x, y: x + y, data))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n +1))

print(factorial(4))

print(factorial(6))
