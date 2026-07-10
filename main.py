import database
from datetime import date
today = date.today()
database.create_table()
while True:
    try:
        choice = int(input("Enter Your Choice:\n1)Add Transaction\n2)View Transaction\n3)Monthly Summary\n4)Exit\n"))
        if choice == 1:
            transaction_type = input("Expense: ")
            Category = input("Category: ")
            Amount = float(input("Amount: "))
            Date = str(today)
            database.add_transaction(transaction_type,Category,Amount,Date)
        if choice == 2:
            rows = database.view_transactions()
            print("-" * 60)
            print("ID  TYPE      CATEGORY      AMOUNT      DATE")
            print("-" * 60)

            for row in rows:
                print(f"{row[0]:<3} {row[1]:<10} {row[2]:<12} ₹{row[3]:<10.2f} {row[4]}")
        if choice == 3:
            pass
        if choice == 4:
            print("Thanks For Visiting!")
            break
    except ValueError:
        print("Enter Given Choices!")
