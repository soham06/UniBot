import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('users.db')

# Create Users Database
c = conn.cursor()
c.execute("""CREATE TABLE hs_user 
(first text, last text, email text, username text,  password text, school text, grade text)
""")
c.execute("""CREATE TABLE uni_user 
(first text, last text, email text, university text, program text, study_level text 
,password text, username text)
""")
conn.commit()
conn.close

# Create Reviews Database
conn2 = sqlite3.connect('reviews.db')
c2 = conn2.cursor()
c2.execute("""CREATE TABLE reviews\
    (name text, university text, program text, message text, rating real)""")
conn2.commit()
conn2.close()

