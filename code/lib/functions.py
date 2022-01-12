def menu(choices, choice):
    i = 0
    print("\n" * 12)
    for e in choices:
        i += 1
        if i == choice:
            print("--->", end="")
        print(e)
    
    key = input()
    if key == "d":
        if len(choices) <= choice:
            return menu(choices, choice)
        else:
            return menu(choices, choice+1)
    if key == "u":
        if 1 >= choice:
            return menu(choices, choice)
        else:
            return menu(choices, choice-1)
    if key == "":
        return choice
    if key == "stop":
        return None

    else:
        return menu(choices, choice)