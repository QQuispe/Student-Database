import sqlite3

db = 'students.db'

con = sqlite3.connect(db)
c = con.cursor()

# Create table
c.execute("""
CREATE TABLE student_info
(id INTERGER PRIMARY KEY,
name TEXT,
points INTERGER
)
""")

con.commit()
con.close()