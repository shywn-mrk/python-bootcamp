def my_func(arg):
    print(arg, type(arg))

user = {'username': 'Shayan', 'age': 21}
my_func(user)

# TRY / EXCEPT / ELSE / FINALLY | Error handling

try:
    number = int(input('Please enter a number: '))

    # Alternate
    # if number == 0:
    #     raise ValueError

    print('Your input divided by 2 is: ', 2 / number)
except ValueError:
    print('Something went wrong!')
except ZeroDivisionError:
    print('Can\'t divide by zero!')
else:
    print('You are doing great :)')
finally:
    print('We are done :)')

print('Can\'t divide by zero!') # Character escaping
print('1\t2') # Tab
print('1\n2') # Next line


