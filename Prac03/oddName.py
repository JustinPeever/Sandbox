"""Justin"""
def main():
    name = get_name()
    numberfeq = int(input("Frq Number Please "))
    method_name(name, numberfeq)


def method_name(name, numberfeq):
    for i in range(0, len(name), numberfeq):
        print(name[i])


def get_name():
    finish = False
    while finish == False:
        name = str(input("Name Please "))
        if name == "":
            finish = False
        else:
            finish = True
    return name


main()