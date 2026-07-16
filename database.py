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
def income_summary():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = "Income"
    """)
    income = cursor.fetchone()[0]
    if income is None:
        income = 0
    connection.close()
    return income
def expense_summary():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type = "Expense"
    """)
    expense = cursor.fetchone()[0]
    if expense is None:
        expense = 0
    connection.close()
    return expense
def delete_transaction(transaction_id):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """,(transaction_id,))
    connection.commit()
    connection.close()
def update_transaction(transaction_id , category,amount):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE transactions
        SET category = ? , amount = ?
        WHERE id = ?
    """,(category, amount, transaction_id))
    connection.commit()
    connection.close()