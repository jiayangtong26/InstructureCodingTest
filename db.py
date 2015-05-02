import sqlite3


#conn = sqlite3.connect('school.db')
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS course
                (course_id TEXT PRIMARY KEY,
                 course_name TEXT, 
                 state TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS student 
                (user_id TEXT PRIMARY KEY, 
                 user_name TEXT, 
                 course_id TEXT, 
                 state TEXT, 
                 FOREIGN KEY(course_id) REFERENCES course(course_id))''')

courses = [("C628944","Suicide","active"),("C696253","Substance abuse","deleted")]
conn.executemany("insert into course(course_id, course_name, state) values (?, ?, ?)", courses)

cur.execute("select * from course")
data = cur.fetchall()
for row in data:
	print row