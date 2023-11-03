text = open("testtext.txt", "r")
trueText = text.readlines()
listText = []
for words in trueText:
    listText.append(words.strip())
print("there is", len(listText), "lines in your text file")
while True:
    lineNumber = (int(input("Which line number would you like to see?, press 0 to quit")))
    if lineNumber == 0:
        break
    if lineNumber > len(listText):
        print("The text does not have that many lines!")
    else:
        lineNumber = listText[lineNumber - 1]
    print(lineNumber)
