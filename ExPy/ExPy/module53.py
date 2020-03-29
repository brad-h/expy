"""Todo List"""

import sqlite3
   
def list_notes():
    """List Notes"""
    with sqlite3.connect("module53.db") as connection:
        cursor = connection.execute("select id, note from notes")
        notes = cursor.fetchall()
        for (id, note) in notes:
            print(id, ":", note)

def add_notes():
    """Add Notes"""
    notes = []
    while True:
        note = input("Add a note: ")
        if note == "":
            break
        notes.append(note)
    if len(notes) == 0:
        return
    notes = ["('" + x.replace("'", "''") + "')" for x in notes]
    with sqlite3.connect("module53.db") as connection:
        query = "insert into notes (note) values %s;\n" % " ".join(notes)
        connection.execute(query)
        connection.commit()

def remove_notes():
    """Remove Notes"""
    ids = []
    while True:
        id = input("Remove note by id: ")
        if id == "":
            break
        id = id.replace("'", "''")
        ids.append(id)
    with sqlite3.connect("module53.db") as connection:
        query = "delete from notes where id in (%s)\n" % ", ".join(ids)
        connection.execute(query)
        connection.commit()

if __name__ == "__main__":
    add_notes()
    list_notes()
    remove_notes()
