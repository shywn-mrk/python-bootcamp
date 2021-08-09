my_tuple = (1, 2, 3)

print(my_tuple[1])

my_tuple[1] = 9

print(my_tuple, type(my_tuple))

file = open('doc.txt', 'r') # Read

print('File mode: ', file.mode)

print('File content:\n', file.read())
print('File content:\n', file.read(9))
file.seek(0)
print('File content:\n', file.read())
print('Cursor position: ', file.tell())
print('File content:\n', file.readline())
print('File content:\n', file.readlines())

file = open('doc.txt', 'w') # Write

file.write('Hi')
file.writelines(['hello\n', 'hi\n', 'how are you?\n'])

file = open('doc.txt', 'a') # Append

file.write('Hi')

file = open('doc.txt', 'r+') # Write and Read
file = open('doc.txt', 'w+') # Write and Read, For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.

print('file content: ', file.read())

file.write('Hi')

print(file.closed)

file.close()

print(file.closed)

with open('doc.txt', 'r+') as file:
    print(file.read())

# NOTE: Next session will be completed
import re

# message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# hex_value = 'ff55aa'

# result = re.match('Lorem', message)
# result = re.search(r'(.*) ipsum (.*?) .*', message)
# result = re.findall(pattern, string, flags)
# result = re.sub(pattern, string, string2)

# print(result.groups())
