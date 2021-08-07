# While loop
n = 0
while n <= 10:
    print(n)
    n += 1
print(n)

# TRY / EXCEPT / ELSE / FINALLY next session

# Functions
def add(a, b=0):
    return a + b

def add(a, b, c):
    return a + b + c

def multiply(a, b):
    return a * b

result = add(2, 3)
print(result)

result = add(2, 3, 4)
print(result)

result = multiply(4, 3)
print(result)

# TODO: ...
def my_function():
    pass
my_function()

def my_function(*args):
    print(args)

my_function(1, 2, 3, 4)

def my_function(**kwargs):
    print(kwargs['name'])

my_function(name='Shayan', surname='Karimi', age=21)
