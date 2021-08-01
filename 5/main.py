# Tuples
my_tuple = (1, 2, True)
# my_tuple[0] = 4 # This does not work
print(my_tuple[2])
new_tuple = (4, 5, 6)
print(my_tuple + new_tuple)

a = 2
b = 4
a, b = b, a
print(a)
print(b)

a, b, c = new_tuple
print(a, b, c)

print(min(my_tuple))
print(max(my_tuple))
print(my_tuple * 3)
print(1 in my_tuple)
print(4 not in my_tuple)


# Ranges
my_range = range(1, 20, 3)
print(list(my_range), type(my_range))


# Dicts
user = {'username': 'shywn_mrk', 'age': 21, 'email': 'shayankarimi0078@gmail.com'}
print(user, type(user))
# print(user.username) # This does not work
# print(user[0]) # This does not work
print(user['username'])
print(user.get('username'))

user.pop('age')
del user['age']
print(user)

print(len(user))
print('username' in user)
print('shywn_mrk' not in user)
keys = user.keys()
print(keys, type(keys))
print(user.values())
print(user.items())


# Type casting
str()
int()
float()
list()
tuple()
set()
dict()

print(bin(2))
print(hex(15))
print(int('0b10', 2))
print(int('0xf', 16))
