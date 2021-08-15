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

    def print_user(self):
        print('username:', self.username)
        print('email:', self.email)

    def del_pass(self):
        delattr(self, 'password')

    def __str__(self):
        return self.username

