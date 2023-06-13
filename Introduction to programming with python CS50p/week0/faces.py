def convert(user_input):
    print(user_input.replace(':)', '🙂').replace(':(', '🙁'))

def main():
    ask_input = input("Please enter an input")
    convert(ask_input)

main()