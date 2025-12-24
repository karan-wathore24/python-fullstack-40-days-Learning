from db_conncetion import connect_db
con = connect_db()
cur=con.cursor()

cur.execute("UPDATE student SET marks=90 WHERE name='KARAN'")
con.commit()
con.close()


print("data updated successfully")