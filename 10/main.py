user = {
    'username': 'shywn_mrk',
    'email': 'shayankarimi0078@gmail.com',
    'password': '123456789'
}


# FOR loops and dictionaries

for key in user.keys():
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(key, value)


# FOR loop and 2 lists

list_1 = [1, 2, 3]
list_2 = [4, 5, 6, 7, 8]

for (item_1, item_2) in zip(list_1, list_2):
    print(item_1, item_2)


# REGEX
import re

pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|org|net|xyz)'

if re.search(pattern, user['email']):
    print(re.search(pattern, user['email']))
    print('User email is valid 🎉')
else:
    print('You shall not pass 🧙‍♂️')


# Classes and OOP

class User:

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print('Welcome 😜')
        else:
            print('You shall not pass 🧙‍♂️')


user = User('shywn_mrk', 'shayankarimi0078@gmail.com', '123456789')

user.login()
