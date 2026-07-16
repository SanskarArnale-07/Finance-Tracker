import database
from datetime import date
today = date.today()
database.create_table()
while True:
    try:
        choice = int(input("Enter Your Choice:\n1)Add Transaction\n2)View Transaction\n3)Monthly Summary\n4)Update Transaction\n5)Delete Transaction\n6)Exit\n"))
        if choice == 1:
            transaction_type = input("Type(Income or Expense): ").capitalize()
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
            income = database.income_summary()
            expense = database.expense_summary()
            balance = income-expense
            print("-" * 60)
            print("       MONTHLY SUMMARY")
            print("-" * 60)
            print(f"Income  : ₹{income:.2f}")
            print(f"Expense : ₹{expense:.2f}")
            print(f"Balance : ₹{balance:.2f}")
            print("Press Enter to Continue...")
            print("=" * 60)
        if choice == 4:
            print("-" * 60)
            transaction_id = int(input("Transaction ID to Update: "))
            Category = input("Enter the Category: ")
            Amount = int(input("Enter the Amount: "))
            database.update_transaction(transaction_id, Category , Amount)
            print("Updated Successfully")
            print("Press Enter to Continue...")
            print("-" * 60)
        if choice == 5:
            print("=" * 60)
            transaction_id = int(input("Transaction ID to Delete: "))
            database.delete_transaction(transaction_id)
            print("Transaction Deleted Successfully")
            print("Press Enter to Continue...")
            print("=" * 60)

            

        if choice == 6:
            print("Thanks For Visiting!")
            break
    except ValueError:
        print("Enter Given Choices!")
