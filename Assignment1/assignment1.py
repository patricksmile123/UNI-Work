def clean_up():
    """
        f refers to text_to_clean.txt
        sf refers to student_names.txt
        use text to read in the appropriate file
        cleaned is used store the wanted characters
        :return: cleaned
        """
    allowed_characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. \n")
    f = open("text_to_clean.txt", 'r')
    cleaned = ""
    text = f.read()
    for line in text:
        cleaned_line = ""
        for char in line:
            if char in allowed_characters:
                cleaned_line += char
        cleaned += cleaned_line
    cleaned += "\n"
    sf = open("student_names.txt", 'w')
    sf.write(cleaned)
    sf.close()

    # lower case char, upper case char, blank, full stop - valid characters
    # insert code here to clean the file as per question 1
    return cleaned


def build_id():
    f = open('student_names.txt', 'r')
    id_list = []

    lines = f.read()
    lines = lines.split("\n")

    for line in lines:
        name_parts = line.split()
        num_parts = len(name_parts)

        if num_parts == 3:
            initials = [part[0].lower() for part in name_parts if part]
            id_str = initials[0]+initials[1]+initials[2]
        elif num_parts == 2:
            id_str = name_parts[0][0].lower() + 'x' + name_parts[1][0].lower()

        if id_str and len(line) > 0:
            id_list.append(id_str)

    f.close()
    return id_list


def validate_password(password):
    illegal_password = []

    # Check password length
    if len(password) < 8:
        illegal_password.append("TOO SHORT")
    if len(password) > 12:
        illegal_password.append("TOO LONG")

    has_upper = False
    has_lower = False

    for char in password:
        if char.isdigit():
            continue
        elif 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif char == '_':
            continue
        else:
            illegal_password.append("WRONG CHARACTERS")

    if not has_upper or not has_lower:
        illegal_password.append("NOT MIXED CASE")

    if password[0].isdigit():
        illegal_password.append("LEADING DIGIT")

    common_passwords = open("password.txt", 'r').read().split("\n")

    if password in common_passwords:
        illegal_password.append("CANNOT MAKE USE OF THIS PASSWORD")

    return illegal_password


def create_unique(id_list):
    """
    Adhere to the instructions in question 4 to determine a unique id for each student
    Write the content of the unique ids to the file unique_ids.txt - open / close the file correctly
    Write the content of the emails created to the file create_emails.txt - - open / close the file correctly
    :param id_list: the id_list that was returned in build_id() is used here to create the unique ids
    :return: final_list is returned and this list contains all of the unique student ids
    """
    # id_list = ["mas", "axj", "drs", "axt", "mas", "mas", "jxs", "hxc", "axg"]
    final_list = []
    unique_ids_str = ""
    emails_str = ""
    for id in id_list:
        id_suffix = 0
        current_id = id + "0000"
        while current_id in final_list:
            current_id = id
            id_suffix += 1
            for x in range(4-len(str(id_suffix))):
                current_id += "0"
            current_id += str(id_suffix)
        final_list.append(current_id)
    for final_id in final_list:
        unique_ids_str += final_id + "\n"
        emails_str += final_id + "@student.bham.ac.uk\n"

    i = open("unique_ids.txt", 'w')
    i.write(unique_ids_str)
    i.close()
    f = open("create_emails.txt", 'w')
    f.write(emails_str)
    f.close()

    # insert code here to create unique ids
    return final_list
def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = open("addresses.txt", 'r')
    text = f.read()
    lines = text.split('\n')
    split_addrs = []
    for line in lines:
        if line:
            parts = line.split(',')
            address_part = parts[0]
            postcode = parts[-1][1:]
            short_address = [address_part, postcode]
            split_addrs.append(short_address)
    return split_addrs

def validate_pcode(split_addrs):
    """
    This function validates each character of the postcode
    :param split_addrs: this is passed from main(), obtained from the function create_short_address()
    :return: validate_pcode is a list that contains True False values for each postcode that is validated - see question 6
    """
    validate_pcode = []
    for index in range(len(split_addrs)):
        _, postcode = split_addrs[index]
        cleaned_postcode = ''
        for char in postcode:
            if char not in " \n\t\r":
                cleaned_postcode += char
        postcode = cleaned_postcode

        is_length_six = len(postcode) == 6
        if not is_length_six:
            postcode = "$$$$$$"
        is_length_six = str(is_length_six)

        is_first_uppercase_alpha = str('A' <= postcode[0] <= 'Z')

        are_middle_chars_digits = "True"
        for char in postcode[1:4]:
            if not ('0' <= char <= '9'):
                are_middle_chars_digits = "False"
                break

        are_last_two_uppercase_alpha = "True"
        for char in postcode[4:]:
            if not ('A' <= char <= 'Z'):
                are_last_two_uppercase_alpha = "False"
                break

        validate_pcode.append(index)
        validate_pcode.append(is_length_six)
        validate_pcode.append(is_first_uppercase_alpha)
        validate_pcode.append(are_middle_chars_digits)
        validate_pcode.append(are_last_two_uppercase_alpha)

    return validate_pcode


def ids_addrs(short_addr):
    """
    This function reads in the unique_ids.txt file as f and creates a dictionary based on the id and the short address
    :param short_addr: passed in from main() - generated from create_short_address()
    :return: combo is the key / value pair, i.e. unique id and the short addr for each student
    """
    f = open("unique_ids.txt", 'r')
    short_addr = split_addrs
    ids = f.read()

    for list in ids:
        combo = {list: short_addr}

    return combo
    # insert code here to create combo

def main():
    id_list = []
    while True:
        print("\nStudent File Menu:")
        print("1. Perform clean up operation")
        print("2. Create ID's")
        print("3. Validate a Password")
        print("4. Create unique ID's")
        print("5. Reduce addresses")
        print("6. Validate postcode")
        print("7. Create ID with short address")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clean_up()
        elif choice == '2':
            id_list = build_id()
        elif choice == '3':
            validate_password("1abcDE%")
        elif choice == '4':
            create_unique(id_list)
        elif choice == '5':
            short_addr = create_short_address()
        elif choice == '6':
            validate_pcode(short_addr)
        elif choice == '7':
            ids_addrs(short_addr)
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()



