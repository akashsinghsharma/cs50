user_input = input('what is the answer to the great question of life, the universe and everything')
user_input = user_input.lower().strip()

if user_input=="42" or user_input == 'forty-two' or user_input == 'forty two':
    print('Yes')

else:
    print('No')