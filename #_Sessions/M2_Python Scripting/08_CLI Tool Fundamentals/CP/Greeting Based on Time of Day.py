import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <hour_in_24_hour_format>")

else:
    hour = int(sys.argv[1])
    if 0 <= hour < 12:
        print("Good Morning!")
    elif 12 <= hour < 18:
        print("Good Afternoon!")
    elif 18 <= hour < 24:
        print("Good Evening!")

    else:
        print("Invalid hour! Please enter a value between 0 and 23.")