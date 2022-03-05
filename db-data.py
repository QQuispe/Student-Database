# This file can be used to reset database to original data
import sqlite3

db = 'students.db'

con = sqlite3.connect(db)
c = con.cursor()

# Clear table
c.execute("DELETE from student_info")

# Create new table
c.execute("""
INSERT INTO student_info (id, name, points) VALUES
('122','Jian Wong','92'),
('211','Steve Smith','80'),
('213','Chris Peterson','91'),
('287','Robert Sanders','75'),
('425','Andrew Whitehead','99'),
('524','Sai Patel','94'),
('626','Lynn Roberts','90')
""")

con.commit()
con.close()