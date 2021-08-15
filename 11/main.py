from utils.models import User

user = User('shywn_mrk', 'shayankarimi0078@gmail.com', '123456789')

user.login('shywn_mrk', '123456789')

user.username = 'shayan.karimi'
print(user.username)

user.print_user()
print(user)

setattr(user, 'username', 'shayan.karimi')
print('username:', getattr(user, 'username'))
print(hasattr(user, 'email'))
print(delattr(user, 'password'))
print('password:', getattr(user, 'password'))
print(isinstance(user, User))

user.del_pass()
print(user.password)

class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Student(Person):

    def __init__(self, name, surname, id, field):
        super().__init__(name, surname)
        self.id = id
        self.field = field

    def __str__(self):
        return f'{self.id} - {self.name} {self.surname} | {self.field}'


person = Person('Shayan', 'Karimi')
print(person)

student = Student('Ali', 'Nasseri', 256314, 'CS')
print(student)

print(issubclass(Student, Person))
print(issubclass(Person, Student))


# Comprehensions

my_list = [x ** 2 for x in range(1,6)]
print(my_list, type(my_list))

my_dict = {x: x ** 2 for x in range(1,6)}
print(my_dict, type(my_dict))


# Lambda

def add_two(x):
    return x + 2

my_first_lambda = lambda x, y : x + y

print(my_first_lambda(2, 3), type(my_first_lambda))


# Map and filter

numbers = [1, 2, 3, 4, 5, 6]

print(list(map(add_two, numbers)))

def filter_func(x):
    return not x % 2 == 0

print(list(filter(filter_func, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))

def my_gen(*args):
    for arg in args:
        yield arg + 2

my_gen_obj = my_gen(1, 2, 3, 4)

next(my_gen_obj)
next(my_gen_obj)
next(my_gen_obj)
next(my_gen_obj)

print(list(my_gen_obj))


# Decorators

def my_decorator(target_function):
    def function_wrapper():
        return f'Python is the {target_function()} programming language! 😎'

    return function_wrapper

@my_decorator
def target_function():
    return 'best'

print(target_function())
