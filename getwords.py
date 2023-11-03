import random

# articles = ("A", "THE")
# nouns = ("BOY", "GIRL", "BAT", "BALL")
# verbs = ("HIT", "SAW", "LIKED")
# prepositions = ("WITH", "BY")


def getWords(x):
    file = open(x, "r")
    content = file.read()
    file.close()
    lst = []
    for words in content.split():
        lst.append(words)
    tuple(lst)
    return lst

def sentence():
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    verbs = getWords("verbs.txt")
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()


def prepositionalPhrase():
    prepositions = getWords("prepositions.txt")
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    number = int(input("Enter the number of sentences"))
    for count in range(number):
        print(sentence())


main()