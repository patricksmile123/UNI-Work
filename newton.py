def newton(number):
    tolerance = 0.00000000001
    estimate = 1
    while True:
        estimate = (estimate + number / estimate) / 2
        difference = abs(number - estimate ** 2)
        if difference <= tolerance:
            break
    print(estimate)


def main():
    while True:
        number = (input("Enter the number you wish the square root to be estimated of, enter to quit"))
        print(number)
        if number == "":
            break
        else:
            newton(int(number))


main()

