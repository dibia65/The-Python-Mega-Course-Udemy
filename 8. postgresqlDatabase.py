import psycopg2

def createTable():
    conn = psycopg2.connect("dbname = 'testDB' user = 'postgres' password = 'subham@1996' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products (ID INTEGER, Name Text, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertData(id, name, qty, price):
    conn = psycopg2.connect("dbname = 'testDB' user = 'postgres' password = 'subham@1996' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO products VALUES('%s', '%s', '%s', '%s')" %(id, name, qty, price))         #this sis prone to SQL injections
    cur.execute("INSERT INTO products VALUES(%s, %s, %s, %s)", (id, name, qty, price))
    conn.commit()
    conn.close()

def viewData():
    conn = psycopg2.connect("dbname = 'testDB' user = 'postgres' password = 'subham@1996' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()

    return rows

def deleteData(id):
    conn = psycopg2.connect("dbname = 'testDB' user = 'postgres' password = 'subham@1996' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE ID = %s", (id,))
    conn.commit()
    conn.close()

def updateData(newID, oldID):
    conn = psycopg2.connect("dbname = 'testDB' user = 'postgres' password = 'subham@1996' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE products SET ID=%s WHERE ID=%s", (newID, oldID))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createTable()
    insertData(3, "Product3", 10, 25)

    print("\nData before updation")
    print(viewData())

    updateData(1, 5)
    #deleteData(4)

    print("\nData after updation")
    print(viewData())