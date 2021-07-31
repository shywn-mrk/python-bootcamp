# Deleing a variable
name = 'Shywn'
print(name)

del name
print(name)


# Lists
numbers = [2, 3, 4, 1, 5]
names = ['John', 'Jane']
ages = [25, 36, 95]

numbers.insert(2, 6)
numbers.extend(names)
print(numbers.index(6))
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(sorted(numbers))
print(numbers + names + ages)
print(numbers * 3)


# Sets
my_set = {1, 2, 3, '4', '5'}
new_set = {1, 2, 3, 6, 7, 8}
empty_set = {} # Creates a dict not a set
print(empty_set, type(empty_set))
new_set = set(numbers)
print(new_set, type(new_set))
new_set = set('Hello World!')
print(new_set, type(new_set))

print(len(my_set))
print(1 in my_set)
print(7 not in my_set)

my_set.add(5)
print(my_set)
my_set.add('5')
print(my_set)
my_set.remove(5)
print(my_set)
my_set.remove(5, '5') # Doesn't work
print(my_set)

frozen_set = frozenset(my_set)
print(frozen_set, type(frozen_set))

print(my_set.intersection(new_set))
print(my_set.difference(new_set))
print(my_set.union(new_set))
print(my_set.pop())
print(my_set)
my_set.clear()
print(my_set)
