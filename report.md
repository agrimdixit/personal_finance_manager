# Project Report — Money Manager

## 1. Project Title
Money Manager — Command-Line Personal Finance Manager

## 2. Problem Statement
Managing daily income and expenses manually can make it difficult to understand spending patterns. This project provides a simple terminal application for recording transactions, calculating financial totals and monitoring a monthly budget.

## 3. Objectives
- Record income and expenses.
- Organize expenses by category.
- Calculate income, expenses and balance.
- Calculate spending for a selected month.
- Set and monitor a monthly budget.
- Preserve data after the program closes.

## 4. Features
1. Add income
2. Add expense
3. View transactions
4. Category-wise expense summary
5. Monthly spending
6. Current balance
7. Monthly budget
8. Budget status

## 5. Technologies
Python and the Python standard library. JSON is used for local storage. No third-party packages are required.

## 6. Python Concepts Used
- Variables and data types
- Arithmetic and comparison operators
- Input/output
- Type conversion
- Conditional statements and loops
- Functions
- Modules
- Lists and dictionaries
- File handling with JSON
- Object-oriented programming through the `FinanceManager` class

## 7. Program Flow
The application loads saved data, displays a menu, accepts an option, runs the selected operation, saves changes where needed and returns to the menu until the user exits.

## 8. Validation
Amounts must be numeric and greater than zero. Empty categories/sources receive a default value. Monthly spending accepts the `YYYY-MM` format.

## 9. Testing Plan
- Add income and verify the income total.
- Add expense and verify the expense total.
- Check that balance equals income minus expenses.
- Enter invalid amounts and verify validation.
- Set a budget and verify the budget status.
- Restart the program and verify that saved data is loaded.

## 10. Limitations
The application is designed for one local user and does not connect to real bank accounts. Data is stored locally in JSON.

## 11. Future Improvements
Possible extensions include editing/deleting transactions, CSV export, recurring transactions, password protection and optional graphical reports.

## 12. Conclusion
Money Manager combines Python fundamentals into a practical command-line application while keeping the program lightweight, portable and easy to execute.
