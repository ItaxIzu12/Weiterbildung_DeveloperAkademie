zahlen = [1, 2, 3, 4, 5]

zahlen.insert(5, 10)

print(zahlen)


zahlen = ["Test", "Hallo", "Welt", "4", "5"]
print(';'.join(zahlen))


tupel = (1, 2, 3, 4, 5)

print(tupel.index(3))


telefonbuch = {
    "Richard": 123456789,
    "Max": 987654321,
    "Anna": 555555555
}

telefonbuch["Max"] = 111111111

print(telefonbuch.get("Test"))