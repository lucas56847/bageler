import os
print('enter: ', end ='')
lines = []

while True:
    line = input("Enter a line (or 'q' to quit): ")
    if line == 'q':
        break
    lines.append(line)

user_input = '\n'.join(lines)

print(user_input.count(',')+1)