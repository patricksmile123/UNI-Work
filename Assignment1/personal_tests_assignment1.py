def create_short_address():
    """
    Open the addresses.txt file correctly where f = the file to be opened
    split the address up so that only the first part and the postcode make up the shorter address
    :return: split_addrs is returned where the address1, postcode make up the list - this list is used for validate_pcode()
    """
    f = open("addresses.txt", 'r')
    text = f.read()
    # lines = text.split('\n')
    # split_addrs = []
    # for line in lines:
    #     if line:
    #         parts = line.split(',')
    #         print(parts)
    #         address_part = parts[0]
    #         postcode = parts[-1][1:]
    #         short_address = [address_part, postcode]
    #         split_addrs.append(short_address)
    # print(split_addrs)
    # return split_addrs
    addresses = []
    split_addrs = []
    for addresses in text:
        addresses = text.split('\n')
    for i in addresses:
        test = i.split(',')
    for answer in addresses:
        split_addrs.append(answer.split(",")[0])

    # insert code here to create the shorter address
    return split_addrs


if __name__ == "__main__":
    create_short_address()