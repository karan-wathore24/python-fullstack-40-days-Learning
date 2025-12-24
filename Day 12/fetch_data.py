from db_conncetion import connect_db

con = connect_db()
cur=con.cursor()
cur.execute("SELECT * FROM student")
data=cur.fetchall()

for i in data:
    print(i)


con.commit()
con.close()