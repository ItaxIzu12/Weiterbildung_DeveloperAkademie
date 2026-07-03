notes = [
    {"title": "Einkauf", "text": "Milch, Brot, Eier"},
    {"title": "Arbeit", "text": "Backendcall um 11"},
]


def show_notes():
    for note in notes:
        print(f"Title: {note['title']}, Text: {note['text']}")


def add_note():
    notes.append({"title": "Neue Notiz", "text": "Hier ist der Text der neuen Notiz."})


def delete_note():
    notes.pop(1)  # Löscht die erste Notiz in der Liste


def update_note():
    notes[0]["test"] = "Ich habe heute Milch, Eier gekauft"


add_note()
delete_note()
update_note()
show_notes()
