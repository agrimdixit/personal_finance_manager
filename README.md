Money Manager

Command-Line Personal Finance Manager built with Python

A lightweight terminal-based application for recording income and expenses, organizing spending, calculating balances, and managing monthly budgets.






Overview

Money Manager is a Python command-line personal finance application designed to provide a simple and organized way to track everyday financial activity.

Core capabilities

Record income and expenses

Categorize spending

View transaction history

Calculate current balance

Generate category-wise expense summaries

Calculate monthly spending

Set and monitor a monthly budget

Persist transactions and budget data locally using JSON

Validate user input

Note: This is an educational/personal-use application. It does not connect to bank accounts or perform real financial transactions.

Features

Income Management

Record income using an amount and source.

Amount: ₹25000
Income source: Salary

Expense Management

Record an expense using an amount, category, and note.

Amount: ₹250
Category: Food
Note: Lunch

Transaction History

View saved transactions containing date, type, amount, category, and note.

Category Summary

Calculate spending totals by category.

Food             ₹3500
Travel           ₹1200
Shopping         ₹2000
Entertainment     ₹800

Monthly Spending

Enter a month in YYYY-MM format to calculate expenses for that month.

Current Balance

Balance = Total Income - Total Expenses

Monthly Budget

Set a monthly spending limit and compare spending against the saved budget.

Local Persistence

Financial records are stored locally in data.json, allowing them to remain available after restarting the application.

Main Menu

==================================================
              MONEY MANAGER
==================================================
1. Add income
2. Add expense
3. View transactions
4. Category summary
5. Monthly spending
6. Current balance
7. Set monthly budget
8. Budget status
9. Exit
==================================================
Enter your choice:

Project Structure

personal_finance_manager/
│
├── main.py
├── finance_manager.py
├── utils.py
├── README.md
├── report.md
└── .gitignore

File

Purpose

main.py

Menu, prompts, navigation, and user interaction

finance_manager.py

FinanceManager class and financial operations

utils.py

Utility and validation functions

data.json

Persistent transaction and budget storage

README.md

Project documentation

report.md

Detailed project report

.gitignore

Files excluded from version control

System Architecture

Terminal / Command Prompt
          │
          ▼
       main.py
          │
          ▼
finance_manager.py
  FinanceManager class
          │
          ▼
       utils.py
          │
          ▼
       data.json

The terminal interface collects user input, FinanceManager handles financial operations, utility functions support reusable tasks, and JSON provides local persistence.

Application Workflow

Start
  │
  ▼
Load saved data
  │
  ▼
Display Main Menu
  │
  ▼
Read User Choice
  │
  ├── Add Income
  ├── Add Expense
  ├── View Transactions
  ├── Category Summary
  ├── Monthly Spending
  ├── Current Balance
  ├── Set Budget
  ├── Budget Status
  └── Exit
  │
  ▼
Save Changes
  │
  ▼
Return to Menu / Exit

Data Storage

The project uses JSON rather than a relational database.

Example transaction:

{
  "date": "2026-09-25",
  "type": "Expense",
  "amount": 250.0,
  "category": "Food",
  "note": "Lunch"
}

Stored information includes:

Transactions
├── Date
├── Type
├── Amount
├── Category
└── Note

Budget
└── Amount

Python Concepts Demonstrated

Concept

Application

Variables & Data Types

Amounts, dates, categories, notes, budgets

Operators

Balance and financial calculations

Input / Output

Terminal menus and interaction

Type Conversion

Numeric financial input

Control Flow

Menu navigation and validation

Functions

Separate financial operations

Lists

Transaction records

Dictionaries

Structured transaction data

Modules

main.py, finance_manager.py, utils.py

OOP

FinanceManager class

File Handling

Persistent local data

JSON

Structured financial storage

Core Functions

add_income()
add_expense()
view_transactions()
category_summary()
monthly_spending()
current_balance()
set_budget()
budget_status()

Input Validation

The application validates important user input:

Amounts must be numeric.

Amounts must be greater than zero.

Invalid menu choices are rejected.

Monthly spending expects YYYY-MM.

Invalid monetary data is prevented from entering records.

Testing

The project defines 12 test scenarios covering its major operations:

ID

Scenario

Expected Result

TC-01

Add valid income

Income is stored

TC-02

Add valid expense

Expense is stored

TC-03

Invalid amount

Error message; amount rejected

TC-04

Negative amount

Amount rejected

TC-05

View transactions

Saved records displayed

TC-06

Category summary

Category totals displayed

TC-07

Current balance

Income minus expenses displayed

TC-08

Monthly spending

Monthly expenses displayed

TC-09

Invalid month

Validation message displayed

TC-10

Set budget

Budget saved

TC-11

Budget status

Spending compared with budget

TC-12

Restart application

Saved data loaded

Requirements

Python 3.9 or newer

Terminal / Command Prompt

No third-party Python packages

The project uses the Python standard library only.

Installation & Usage

Clone

git clone https://github.com/YOUR_USERNAME/personal_finance_manager.git
cd personal_finance_manager

Run

python main.py

Or:

python3 main.py

No database, GUI setup, or external package installation is required.

Example Execution

ADD EXPENSE

Amount: ₹250
Category: Food
Note: Lunch

Expense of ₹250.00 added.

Category summary:

Food             ₹3500
Travel           ₹1200
Shopping         ₹2000
Entertainment     ₹800

Non-Functional Characteristics

Quality

Implementation

Usability

Clear terminal menu and prompts

Reliability

Saved data remains available after restart

Portability

Runs on Python 3.9+

Maintainability

UI, financial logic, and utilities are separated

Dependencies

No third-party packages

Performance

Lightweight local calculations and file operations

Data Integrity

Invalid/non-positive amounts are rejected

Privacy

Financial records remain in local storage

Advantages

Simple command-line interface

Local data persistence

No external dependencies

No database configuration

Portable Python implementation

Modular project structure

Category-wise summaries

Monthly spending analysis

Budget tracking

Demonstrates multiple Python concepts

Current Limitations

Designed for a single local user

No real bank integration

No actual financial transactions

Local JSON storage instead of a database

No graphical charts

Uses Indian Rupees (₹)

No user authentication in the current version

Future Enhancements

Transaction editing and deletion

Transaction search and filtering

CSV export

Recurring expenses

Multiple user profiles

Password protection

Graphical spending charts

Detailed financial reports

Database support

Multiple currency support

Monthly and yearly summaries

Educational Purpose

Money Manager was developed as a Python Essentials project to demonstrate how Python fundamentals can be combined into a practical personal-finance application.

The project brings together variables, operators, input/output, type conversion, control flow, data structures, functions, modules, object-oriented programming, file handling, and JSON persistence in one workflow.
