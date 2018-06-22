import sqlite3

def createTable():
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products (ID INTEGER, Name Text, qty INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insertData(id, name, qty, price):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO products VALUES(?, ?, ?, ?)", (id, name, qty, price))
    conn.commit()
    conn.close()

def viewData():
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()

    return rows

def deleteData(id):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE ID=?", (id,))
    conn.commit()
    conn.close()

def updateData(price, id):
    conn = sqlite3.connect("demo.db")
    cur = conn.cursor()
    cur.execute("UPDATE products SET price=? WHERE ID=?", (price, id))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createTable()
    insertData(4, "Product4", 15, 35)

    print("\nData before updation")
    print(viewData())

    updateData(50, 2)
    #deleteData(1)

    print("\nData after updation")
    print(viewData())