from db_conncetion import connect_db
con = connect_db()
cur=con.cursor()

cur.execute("DELETE FROM student WHERE name='KARAN'")
con.commit()
con.close()

print("delete data succesfully")