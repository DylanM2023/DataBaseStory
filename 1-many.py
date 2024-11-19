import sqlite3

table = sqlite3.connect('1-many.db')
c = table.cursor()

c.execute('''CREATE TABLE Authors (
            id INTEGER PRIMARY KEY, 
            name TEXT
            )''')
c.execute('''CREATE TABLE Books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES Authors(id)
        )''')

c.execute("INSERT INTO Authors (name) VALUES ('George Orwell')")
c.execute("INSERT INTO Books (title, author_id) VALUES ('1984', 1)")
c.execute("INSERT INTO Books (title,author_id) VALUES ('Animal Farm', 1)")

table.commit()
table.close()