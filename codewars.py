def are_you_playing_banjo(name):
    if name[0] == "R":
        name = print(name + " plays banjo")
    elif name[0] == "r":
        name = print(name + " plays banjo")
    else:
        name = print(name + " does not play banjo")
    str(name)
    return name

name = "adam"
are_you_playing_banjo(name)