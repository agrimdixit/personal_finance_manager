# Money Manager

A command-line personal finance manager written in Python.

## Features

- Add income and expenses
- Categorize expenses and add notes
- View transaction history
- Calculate income, expenses and balance
- View category-wise spending
- Check spending for a selected month
- Set a monthly budget
- Check current-month budget status
- Save data locally in JSON

## Requirements

- Python 3.9 or newer
- No external packages

## Run

Open a terminal in the project folder and run:

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

The program creates `data.json` automatically when data is first saved.

## Project Structure

```text
personal-finance-manager/
├── main.py
├── finance_manager.py
├── utils.py
├── README.md
├── report.md
└── .gitignore
```

## Notes

This project is intentionally terminal-only and uses only Python's standard library, so there is no dependency installation step or GUI requirement.
