def clean_up():
    """
        f refers to text_to_clean.txt
        sf refers to student_names.txt
        use text to read in the appropriate file
        cleaned is used store the wanted characters
        :return: cleaned
        """
    allowed_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .\n")
    f = open("text_to_clean.txt", 'r')
    print(f)
    cleaned = ""
    text = f.read()
    for line in text:
        cleaned_line = ""
        for char in line:
            if char in allowed_characters:
                cleaned_line += char
        cleaned += cleaned_line
    sf = open("student_names.txt, w")
    print(cleaned, file=sf)

    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    return cleaned

    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    return cleaned
if __name__ == "__main__":
    clean_up()