age = 21 
print(age, type(age))

age = '22'
print(age, type(age))

# Strings
name = 'Shayan'
names = 'Shayan, Ali, Hassan'

print(name.find('a'))
print(name.lower())
print(name.upper())
print(name.startswith('Sha'))
print(name.endswith('b'))
print(name.strip('$'))
print(name.replace('a', 'b'))
print(names.split(', ')) # Returns an list
splited_names = names.split(', ')
print(', '.join(splited_names)) # Works on lists

message = 'Welcome ' + name + '!'
print(name + ' is ' + str(21))
print(name * 3)
