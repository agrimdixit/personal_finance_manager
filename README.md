# Money Manager

### Command-Line Personal Finance Manager built with Python

> A lightweight terminal-based application for recording income and expenses, organizing spending, calculating balances, and managing monthly budgets.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge)
![Interface](https://img.shields.io/badge/Interface-CLI-555555?style=for-the-badge)

---

## Overview

**Money Manager** is a Python command-line personal finance application designed to provide a simple and organized way to track everyday financial activity.

The application allows users to:

- Record income
- Record expenses
- Categorize spending
- View transaction history
- Calculate the current balance
- Generate category-wise expense summaries
- Calculate monthly spending
- Set and monitor a monthly budget
- Persist transactions and budget data locally using JSON
- Validate user input

The project is intentionally lightweight and uses Python's standard library without requiring a database, graphical interface, internet connection, or third-party packages.

> **Note:** This is an educational and personal-use application. It does not connect to bank accounts or perform real financial transactions.

---

## Features

### Income Management

Record income using an amount and source.

```text
Amount: ₹25000
Income source: Salary
```

### Expense Management

Record an expense using an amount, category, and note.

```text
Amount: ₹250
Category: Food
Note: Lunch
```

### Transaction History

View saved transactions containing:

- Date
- Transaction type
- Amount
- Category
- Note

The application also provides total income and total expense information.

### Category Summary

Calculate spending totals by category.

```text
Food              ₹3500
Travel            ₹1200
Shopping          ₹2000
Entertainment      ₹800
```

### Monthly Spending

Enter a month in `YYYY-MM` format to calculate expenses recorded during that month.

### Current Balance

```text
Balance = Total Income - Total Expenses
```

### Monthly Budget

Set a monthly spending limit and compare spending against the saved budget.

The budget status provides:

- Monthly budget
- Amount spent
- Amount remaining
- Amount exceeded when spending goes over the budget

### Local Data Persistence

Financial records are stored locally in `data.json`, allowing saved information to remain available after restarting the application.

---

## Main Menu

```text
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
```

---

## Project Structure

```text
personal_finance_manager/
├── main.py
├── finance_manager.py
├── utils.py
├── README.md
├── report.md
└── .gitignore
```

| File | Purpose |
|---|---|
| `main.py` | Main menu, prompts, navigation, and user interaction |
| `finance_manager.py` | `FinanceManager` class and core financial operations |
| `utils.py` | Reusable utility and validation functions |
| `data.json` | Persistent local transaction and budget storage |
| `README.md` | Project documentation |
| `report.md` | Detailed project report |
| `.gitignore` | Files excluded from version control |

---

## System Architecture

The project follows a simple modular local architecture.

| Component | Responsibility |
|---|---|
| **Terminal / Command Prompt** | Collects user input and displays results |
| **`main.py`** | Menu, prompts, navigation, and user interaction |
| **`finance_manager.py`** | `FinanceManager` class, transactions, income, expenses, balance, summaries, and budget |
| **`utils.py`** | Reusable utility and validation functions |
| **`data.json`** | Persistent local transaction and budget storage |

### Application Layers

```text
User
  |
  v
main.py
  |
  v
FinanceManager
  |
  v
utils.py
  |
  v
data.json
```

---

## Application Workflow

The application follows this workflow:

**Start → Load Saved Data → Display Main Menu → Read User Choice → Execute Selected Operation → Save Changes → Return to Menu / Exit**

Available operations:

1. Add Income
2. Add Expense
3. View Transactions
4. Category Summary
5. Monthly Spending
6. Current Balance
7. Set Budget
8. Budget Status
9. Exit

---

## Data Storage

Money Manager uses JSON rather than a relational database.

### Example Transaction

```json
{
  "date": "2026-09-25",
  "type": "Expense",
  "amount": 250.0,
  "category": "Food",
  "note": "Lunch"
}
```

### Stored Information

| Data | Fields |
|---|---|
| **Transaction** | Date, type, amount, category, note |
| **Budget** | Budget amount |

JSON keeps the project lightweight while allowing financial information to persist between program sessions.

---

## Python Concepts Demonstrated

The project applies concepts from the Python Essentials syllabus in a practical application.

| Concept | Application |
|---|---|
| Variables & Data Types | Amounts, dates, categories, notes, and budgets |
| Operators | Balance and financial calculations |
| Input / Output | Terminal menus and user interaction |
| Type Conversion | Numeric financial input |
| Control Flow | Menu navigation and validation |
| Functions | Separate financial operations |
| Lists | Transaction records |
| Dictionaries | Structured transaction data |
| Modules | `main.py`, `finance_manager.py`, `utils.py` |
| OOP | `FinanceManager` class |
| File Handling | Persistent local data |
| JSON | Structured financial storage |

### Core Functions

```python
add_income()
add_expense()
view_transactions()
category_summary()
monthly_spending()
current_balance()
set_budget()
budget_status()
```

---

## Input Validation

The application validates important user input:

- Amounts must be numeric.
- Amounts must be greater than zero.
- Invalid menu choices are rejected.
- Monthly spending expects the `YYYY-MM` format.
- Invalid monetary data is prevented from entering stored records.

---

## Testing

The project defines **12 test scenarios** covering its major operations.

| ID | Scenario | Expected Result |
|---|---|---|
| TC-01 | Add valid income | Income is stored |
| TC-02 | Add valid expense | Expense is stored |
| TC-03 | Invalid amount | Error message; amount rejected |
| TC-04 | Negative amount | Amount rejected |
| TC-05 | View transactions | Saved records displayed |
| TC-06 | Category summary | Category totals displayed |
| TC-07 | Current balance | Income minus expenses displayed |
| TC-08 | Monthly spending | Monthly expenses displayed |
| TC-09 | Invalid month | Validation message displayed |
| TC-10 | Set budget | Budget saved |
| TC-11 | Budget status | Spending compared with budget |
| TC-12 | Restart application | Saved data loaded |

---

## Requirements

- **Python 3.9 or newer**
- Terminal / Command Prompt
- No third-party Python packages

The project uses the Python standard library only.

---

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/personal_finance_manager.git
```

### 2. Enter the Project Directory

```bash
cd personal_finance_manager
```

### 3. Run the Application

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

No database, GUI setup, or external package installation is required.

---

## Example Execution

### Add Expense

```text
ADD EXPENSE

Amount: ₹250
Category: Food
Note: Lunch

Expense of ₹250.00 added.
```

### Category Summary

```text
Food              ₹3500
Travel            ₹1200
Shopping          ₹2000
Entertainment      ₹800
```

---

## Non-Functional Characteristics

| Quality | Implementation |
|---|---|
| **Usability** | Clear terminal menu and prompts |
| **Reliability** | Saved data remains available after restart |
| **Portability** | Runs on systems supporting Python 3.9+ |
| **Maintainability** | UI, financial logic, and utilities are separated |
| **Dependencies** | No third-party Python packages |
| **Performance** | Lightweight local calculations and file operations |
| **Data Integrity** | Invalid or non-positive amounts are rejected |
| **Privacy** | Financial records remain in local storage |

---

## Advantages

- Simple command-line interface
- Easy transaction recording
- Local data persistence
- No external dependencies
- No database configuration
- Portable Python implementation
- Modular project structure
- Category-wise financial summaries
- Monthly spending analysis
- Budget tracking
- Demonstrates multiple Python concepts

---

## Current Limitations

The current version:

- Is designed for a single local user
- Does not connect to real bank accounts
- Does not perform real financial transactions
- Uses local JSON storage instead of a database
- Does not currently provide graphical charts
- Uses Indian Rupees (₹)
- Does not currently provide user authentication

---

## Future Enhancements

- [ ] Transaction editing and deletion
- [ ] Transaction search and filtering
- [ ] CSV export
- [ ] Recurring expenses
- [ ] Multiple user profiles
- [ ] Password protection
- [ ] Graphical spending charts
- [ ] Detailed financial reports
- [ ] Database support
- [ ] Multiple currency support
- [ ] Monthly and yearly financial summaries

---

## Educational Purpose

Money Manager was developed as a Python Essentials project to demonstrate how Python fundamentals can be combined into a practical personal-finance application.

The project brings together variables, operators, input/output, type conversion, control flow, data structures, functions, modules, object-oriented programming, file handling, and JSON persistence in one workflow.

---

## License

This project is intended for educational and personal-use purposes.
