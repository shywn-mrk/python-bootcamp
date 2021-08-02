# IF / ELSE / ELIF
age = int(input('Please enter you age: '))

if age >= 18:
    print('You are an adult!')

    if age <= 45:
        print('You are still young.')
elif age > 12:
    print('You are a teenager.')
else:
    print('You are a baby.')

print('Keep going!')


# FOR Loops
brands = ['Asus', 'HP', 'Dell', 'Apple', True, 125, [1, 2, 3], {1, 2, 3}, {'age': 21}]

#  V1
for brand in brands:
    if brand == 'Asus':
        print(brand)
        break
print(brand)

# V2
for i in range(len(brands)):
    print(brands[i])

print('End of the loop!')
