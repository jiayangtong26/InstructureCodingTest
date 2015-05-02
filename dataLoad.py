import pandas as pd
import sys

df = pd.read_csv("csvs/001.csv")
print df.columns
print df

while True:
    line = sys.stdin.readline()
    if not line:
        break
    files = line.split()
    #print files
    for f in files:
        print f
        df = pd.read_csv("csvs/"+f) # read the csv file according to its name, the file path is hard-coded for simplicity.
        if "user_id" in df.columns: # student data type
            table = "student"
            columns = [c for c in df.columns if c != "user_id"]
            columns.append("user_id")
            print columns

        # course data type
        elif "course_id" in df.columns:
            table = "course"
            columns = [c for c in df.columns if c != "course_id"]
            columns.append("course_id")
            print columns
