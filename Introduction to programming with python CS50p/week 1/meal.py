def main():
    user_input = input("What's the time now, o good sir?").strip()
    time = convert(user_input)
    if time >= 7 and time <= 8:
        print('breakfast time')

    elif time >= 12 and time <= 13:
        print('lunch time')

    elif time >= 18 and time <= 19:
        print('dinner time')

    else:
        print()

def convert(time):
    time = time.split(':')
    hrs = float(time[0])
    min = float(time[1]) / 60
    time_converted = hrs + min
    return time_converted

if __name__ == "__main__":
    main()