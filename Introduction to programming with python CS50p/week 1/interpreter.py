user_input = input('What do you want to calculate')
user_input = user_input.split()

x = float(user_input[0])
y = user_input[1]
z = float(user_input[2])

if y == '+':
    output = x + z

elif y == '-':
    output = x - z

elif y == '*':
    output = x * z

else:
    output = x / z

print(f'{output:.1f}')