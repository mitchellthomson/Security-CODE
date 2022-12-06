import psycopg2

def db_connection():
    connection = psycopg2.connect(dbname="pass", user="docker", password="docker") 

    cur = connection.cursor()

    cur.execute("SELECT password FROM manager")
    rows = cur.fetchall()

    if not len(rows):
        print("None")
    else:
        for row in rows:
            print(row)
            

    cur.close()
    connection.close()
    
    return connection