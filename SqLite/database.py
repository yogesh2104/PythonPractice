import sqlite3

# create a database
connetion = sqlite3.connect('customer.db')
#this line make customer.db file if file is not present 
# if you want to make db in memory then
# connetion = sqlite3.connect(':memory:')
# than we have to make cursor to in which you can invoke methodes that executes SQLite s
# statements , fetch data from the result set of queries.
# create a cursor
cur = connetion.cursor()

# create table
# cur.execute("""CREATE TABLE yogeshDB(first_name text,lastname text, email text)""")


# cur.execute("INSERT INTO yogeshDB values('yogesh','singh','singh@gmail.com')")
# cur.execute("INSERT INTO yogeshDB values('mahesh','yadav','mahesh@gmail.com')")
# cur.execute("INSERT INTO yogeshDB values('visahl','varma','vishal@gmail.com')")
# cur.execute("INSERT INTO yogeshDB values('manish','khatri','manish@gmail.com')")


my_list = [('dsfsd','dff','reg@gmail.com'),
           ('gre','gdb','dfsg@gmail.com'),
           ('dsgh','gss','njr@gmail.com'),
           ('ggre','ge','mgdb@gmail.com'),
           ('fsere','hffgnb','dfh@gmail.com'),
           ('hkg','koth','gjs@gmail.com'),
]
cur.executemany("INSERT INTO yogeshDB values(?,?,?)",my_list)
print("Database created...")

# close database
# it is must
cur.close()
