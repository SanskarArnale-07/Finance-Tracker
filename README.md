# 💰 Finance Tracker

A simple command-line Finance Tracker built with Python and SQLite to manage personal income and expenses.

## Features

- ➕ Add Income and Expense transactions
- 📋 View all transactions
- ✏️ Update existing transactions
- ❌ Delete transactions
- 📊 Monthly Summary
  - Total Income
  - Total Expenses
  - Current Balance
- 💾 SQLite database for persistent storage

## Technologies Used

- Python 3
- SQLite3

## Project Structure

```
Finance-Tracker/
│── main.py
│── database.py
│── finance.db
│── README.md
│── .gitignore

```

## Database Schema

| Column | Type |
|---------|------|
| id | INTEGER (Primary Key) |
| type | TEXT |
| category | TEXT |
| amount | REAL |
| date | TEXT |

## SQL Concepts Used

- CREATE TABLE
- INSERT INTO
- SELECT
- UPDATE
- DELETE
- Aggregate Functions (SUM)

## What I Learned

While building this project, I learned:

- SQLite database integration with Python
- Implementing CRUD(Create, Read, Update, Delete) operations
- SQL queries
- Parameterized queries using `?`
- Database connections and cursors
- Organizing code into multiple modules

## Future Improvements

- Category-wise reports
- CSV export
- Search by category/date
- Budget tracking
- Graphical interface (Tkinter)

## How to Run

```bash
git clone <https://github.com/SanskarArnale-07/Finance-Tracker>

cd Finance-Tracker

python main.py

**Note:** `finance.db` is created automatically when you run the application for the first time.
```

---

Made with ❤️ using Python.