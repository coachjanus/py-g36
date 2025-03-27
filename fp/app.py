# 

def foo():
    print('I am foo function')
    
foo()

bar = foo

bar()

print(lambda s: s[::-1])

print(callable(lambda s: s[::-1]))

revers = lambda s: s[::-1]

print(revers("I'm a string"))

print((lambda x1, x2, x3:(x1 + x2 + x3) / 3)(8, 7, 6))

def fn(x):
    return x, x**2, x**3

print(fn(4))

print((lambda x: (x, x**2, x**3))(4))

print((lambda x: [x, x**2, x**3])(4))
print((lambda x: {1:x, 2:x**2, 3:x**3})(4))

def inner():
    print("I'm inner function")
    
def outer(fn):
    print("I'm oter function")
    fn()

outer(inner)


animals = ['ferret', 'vole', 'dog', 'cat', 'gecko']

print(sorted(animals))

print(sorted(animals, key=len))

print(sorted(animals, key=len, reverse=True))


def revers_len(s):
    return -len(s)

print(sorted(animals, key=revers_len))

a = [10, 3, 4, 1, 9]
a.sort()
print(a)

b = [
    [12, 101],
    [2, 200],
    [8, 99]
]
b.sort()
print(b)

def sort_col(i):
    return i[1]

b.sort(key=sort_col)
print(b)

b.sort(key=lambda x: x[0])
print(b)

b.sort(key=lambda x: x[1])
print(b)