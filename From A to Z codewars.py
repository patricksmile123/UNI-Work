def gimme_the_letters(sp):
    out = ""
    for c in range(ord(sp[0]), ord(sp[2]) + 1):
        out += chr(c)
    return out
