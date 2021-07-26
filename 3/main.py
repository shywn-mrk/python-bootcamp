name = 'Shayan'
age = 21

print('yan' in name)
print('z' not in name)

# # String formatting

# # V1
print('My name is %s and I\'m %d. %.8f'%(name, age, 36.24))
# # V2
print('My name is {} and I\'m {}. {}'.format(name, age, 36.24))
# # V3
print(f'My name is {name} and I\'m {age}.')

message = f'My name is {name} and I\'m {age}'

# Slicing
print(message[5])
print(message[0:5])
print(message[:5])
print(message[2:5])
print(message[:10:5])
print(message[::-1])

# Numbers
age = 21
avg = 15.46

print(age, type(age))
print(avg, type(avg))

# Math Operators
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 // 2)
print(1 % 2)
print(2 ** 3)
print(2 + 3 * 2)

print(abs(-256))

print(float(2))
print(int(2.56))
print(type(int('546848465')))

numbers = [1, 5, 2, 6, 8]
print(max(numbers))
print(max(1, 5, 2, 6, 8))
print(min(numbers))
print(pow(2, 3))

print(1 == 2)
print(1 != 2)
print(1 >= 2)
print(1 <= 2)
print(1 > 2)
print(not(1 < 2))
print(bool(True))
print(bool(False))
print(bool(0))
print(bool(-1))
print(bool(-1.69))
print(bool('bool'))
print(bool(''))
print(bool(' '))

# Lists
numbers = [1, 2, 3, 4, 5, 5, 5]
print(numbers, type(numbers))
print(numbers[4])
print(numbers[:4])
print(numbers[::-1])

my_list = ['string', 21, 36.25, True, numbers]
print(my_list)

print(len(numbers))
print(len('string'))

numbers.append(6) # Exactly one argument
print(numbers)

del numbers[0]
numbers.pop(0)
numbers.remove(5)
print(numbers)
