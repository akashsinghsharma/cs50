'''
user_input = input('Greetings')
user_input = user_input.strip().lower()
user_input = user_input.split()

if user_input[0] == 'hello':
    print('$0')

elif user_input[0][0] == 'h':
    print('$20')

else:
    print('$100')
'''
#Approach 2:

user_input = input('Greetings:')
user_input = user_input.strip().lower()

if user_input.startswith('hello'):
    print('$0')

elif user_input.startswith('h'):
    print('$20')

else:
    print('$100')