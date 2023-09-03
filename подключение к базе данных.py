import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL)''')

cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('John Doe', 30))
cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ('Jane Smith', 25))

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()
