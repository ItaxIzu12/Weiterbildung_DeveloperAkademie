def sag_hallo(name):
    print("Hallo", name, "!")


sag_hallo("Alice")


def lotto_spielen(*zahlen):
    print("Die gezogenen Lottozahlen sind:", zahlen)


lotto_spielen(5, 12, 23, 34, 45, 49)


def hallo(name):
    print("Hallo,", name)


def addiere(x, y):
    return x + y


def subtrahiere(x, y):
    return x - y


def multipliziere(x, y):
    return x * y


def dividiere(x, y):
    return x / y


print(hallo("Max"))
print(addiere(5, 7))
print(subtrahiere(10, 3))
print(multipliziere(4, 6))
print(dividiere(8, 2))


#scoping
level = 0


def level_up():
    global level
    level += 1
    print(f"Dein Level ist: {level}")


level_up()