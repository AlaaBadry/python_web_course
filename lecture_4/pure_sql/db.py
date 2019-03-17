import sqlite3


conn = sqlite3.connect("./test.sqlite")

name = input("Enter a student name: ")
sql = f"SELECT * FROM students WHERE name=?"

print(sql)

cur = conn.cursor()
cur.execute(sql, (name,))

rows = cur.fetchall()
for row in rows:
    print(row)

sql = "INSERT INTO students(name,address) " \
      "VALUES(?,?)"
cur.execute(sql, ("Akram", "Maadi"))
conn.commit()

sql = "INSERT INTO students(name,address) " \
      "VALUES(?,?)"
cur.execute(sql, ("Mona", "Alex"))
conn.rollback()

print("#################")

cur.execute("SELECT * FROM students")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
