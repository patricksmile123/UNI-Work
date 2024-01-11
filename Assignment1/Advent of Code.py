codes = open("advent_of_code.txt", "r")
allowed_characters = "1234567890"
allowed_characters_2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
total_value = 0
for line in codes:
    cleaned_line = ""
    for character in line:
        if character in allowed_characters:
            cleaned_line += character
    cleaner_line = cleaned_line[0] + cleaned_line[-1]
    total_value += (int(cleaner_line))
print(total_value)
