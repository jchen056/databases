import mysql.connector as mysql

def connect(db_name):
    try:
        db=mysql.connect(
            host='localhost',
            user='root',
            password='',
            database=db_name;
        )
    except Error as e:
        print(e)

if __name__=='__main__':
    db=connect("projects")
    cursor=db.cursor()
    cursor.execute("SELECT * FROM projects")
    project_records=cursor.fetchall()
    print(project_records)
    db.close()