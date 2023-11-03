def mode(numbers):
    # fileName = "testnumbers.txt"
    # f = open(fileName, 'r')
    # x = f.read()
    # x = x.split(',')

    theDictionary = {}
    for key in numbers:
        number = theDictionary.get(key, None)
        if number is None:
            theDictionary[key] = 1
        else:
            theDictionary[key] = number + 1
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            print("the mode is", key)


def median(numbers):
    # fileName = "testnumbers.txt"
    # f = open(fileName, 'r')

    # numbers = []
    # for line in numbers:
    #     for word in words:
    # for line in numbers:
    #     numbers.append(float(word))
    numbers.sort()
    midpoint = len(numbers) // 2
    print("the median is", end=" ")
    if len(numbers) % 2 == 1:
        print(numbers[midpoint])
    else:
        print((numbers[midpoint] + numbers[midpoint - 1]) / 2)


def mean(numbers):
    #
    #
    # for line in numbers:
    #     for word in words:
    answer = 0.0
    for calculation in numbers:
        answer += calculation
    trueAnswer = (answer/len(numbers))
    print("The mean of your numbers is", trueAnswer)


def main():
    function = input("Which function would you like to call? mean, median or mode ")
    numbers = []
    while True:
        numbers_input = input("What are your numbers that need to be tested, type quit to break: ")
        if numbers_input.lower() == "quit":
            break
        numbers.append(float(numbers_input))

    if function == "median":
        median(numbers)
    elif function == "mode":
        mode(numbers)
    elif function == "mean":
        mean(numbers)
# def main():
#     function = (input("Which function would you like to call? mean, median or mode "))
#     numbers = []
#     while True:
#        numbers = (input("What are your numbers that need to be tested, type quit to break"))
#         if numbers == ("quit"):
#             break
#     if function == "median":
#         median(numbers)
#     elif function == "mode":
#         mode(numbers)
#     elif function == "mean":
#         mean()

# main()
# if __name__ == "__main:__":
main()

