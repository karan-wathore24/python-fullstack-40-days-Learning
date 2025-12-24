from db_conncetion import connect_db

con = connect_db()
cur=con.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS student(name VARCHAR(50), marks INT)")
cur.execute("INSERT INTO student( name, marks)VALUES (?,?)",('KARAN',95))


con.commit()
con.close()

print("data inserted Successfully")