enteredNumber = input("Enter a number: ")
remainder = int(enteredNumber) % 2
if (remainder > 0):
    print("odd")
else:
    if (int(enteredNumber) % 4 == 0):
        print("div by 4")
    else:
        print("Even")