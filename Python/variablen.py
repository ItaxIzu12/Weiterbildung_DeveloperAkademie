name = 'Richard'
alter = 28
beruf = 'Softwareentwickler'

print('Name:', name)
print('Alter:', alter)
print('Beruf:', beruf)

name, alter, beruf = beruf, name, alter

print('Hallo, mein Name ist', name, 'und ich bin', alter, 'Jahre alt. Ich arbeite als', beruf, '.')

name = "Richard    test"
obst = "Apfel"
haus = "Villa"

print(name[0:6], len(obst), len(haus))

print(name.strip())

print(name.replace("ard", "affe"))

zahlen = "0123456789"

print(16**0.5)

note = input("Bitte geben Sie Ihre Note ein: ")
if note == "1":
    print("Sehr gut!")
elif note == "2":
    print("Gut!")
else:
    print("Nicht bestanden!")


skills = ['Python', 'Java', 'C++', 'JavaScript']

for skill in skills:
    print('Ich kann', skill)


zahlen = [1, 2, 3, 4, 5]

zahlen.append(6)
print(zahlen)

test = (1, 2, 3, 4, 5, 6, 76, 98, 10, 11)

print(test[4])
