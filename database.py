import sqlite3
def connect_database():  
    connection = sqlite3.connect("finance.db")
    return connection
def create_table():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)   
    connection.commit()   
    connection.close()     
def add_transaction(transaction_type, category, amount, date):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions(type, category, amount, date)
        VALUES (?, ?, ?, ?)
    """, (transaction_type, category, amount, date))
    connection.commit()
    connection.close()
def view_transactions():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    connection.close()
    return rows
