import pandas as pd
import sys
import sqlite3


#conn = sqlite3.connect('school.db')
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
# create table "student" and "course". The relation is "Many-to-One"
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

while True:
    line = sys.stdin.readline()
    if not line:
        break
    files = line.split()
    print "**************************************************"
    print "Receiving and processing CSV files:",files
    for f in files:

        # read the csv file according to its name, the file path is hard-coded for simplicity.
        df = pd.read_csv("csvs/"+f) 
        
        # student data type
        if "user_id" in df.columns: 
            table = "student"
            new_rows = []
            # columns without "user_id", used in update
            u_columns = [c for c in df.columns if c != "user_id"]
            # all columns with "user_id" at the end
            columns = [c for c in df.columns if c != "user_id"]
            columns.append("user_id")
            #print columns
            # iterate all rows in the csv file
            for index,row in df.iterrows():
                # put the column values in a tuple
                r = tuple(row[col] for col in columns)
                #print r
                # check if the row exists in table "student" or not
                cur.execute("SELECT user_id FROM student WHERE user_id = ?", (row["user_id"],))
                data=cur.fetchone()
                if data is None:
                    # this is a new row
                    new_rows.append(r)
                else:
                    # update the row
                    # print "UPDATE student SET "+ "=?, ".join(u_columns) +"=? WHERE user_id=?",r
                    cur.execute("UPDATE student SET "+ "=?, ".join(u_columns) +"=? WHERE user_id=?", r)
            # insert all new rows in a batch
            conn.executemany("INSERT INTO student("+",".join(columns)+") VALUES (?, ?, ?)", new_rows)
            #for new_row in new_rows:
                #print "insert into student("+",".join(columns)+") values (?, ?, ?)",new_row


        # course data type
        elif "course_id" in df.columns:
            table = "course"
            new_rows = []
            # columns without "course_id", used in update
            u_columns = [c for c in df.columns if c != "course_id"]
            # all columns with "course_id" at the end
            columns = [c for c in df.columns if c != "course_id"]
            columns.append("course_id")
            #print columns
            # iterate all rows in the csv file
            for index,row in df.iterrows():
                # put the column values in a tuple
                r = tuple(row[col] for col in columns)
                #print r
                # check if the row exists in table "course" or not
                cur.execute("SELECT course_id FROM course WHERE course_id = ?", (row["course_id"],))
                data=cur.fetchone()
                if data is None:
                    # this is a new row
                    new_rows.append(r)
                else:
                    # update the row
                    # print "UPDATE course SET "+ "=?, ".join(u_columns) +"=? WHERE course_id=?",r
                    cur.execute("UPDATE course SET "+ "=?, ".join(u_columns) +"=? WHERE course_id=?", r)
            # insert all new rows in a batch
            conn.executemany("INSERT INTO course("+",".join(columns)+") VALUES (?, ?, ?)", new_rows)
            #for new_row in new_rows:
            #    print "insert into course("+",".join(columns)+") values (?, ?, ?)",new_row   

    # print all active courses and active students
    cur.execute("select course_id,course_name from course where state=\"active\" ")
    active_courses = cur.fetchall()
    for c in active_courses:
        print "Active Course:",c[1]
        cur.execute("select user_name from student where state=\"active\" and course_id=?", (c[0],))
        active_students = cur.fetchall()
        for s in active_students:
            print "\tActive Student:",s[0]
        print
    print "**************************************************"

