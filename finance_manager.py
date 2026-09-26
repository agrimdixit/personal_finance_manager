import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("data.json")


class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.budget = None
        self.load_data()

    def load_data(self):
        if not DATA_FILE.exists():
            return
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            self.transactions = data.get("transactions", [])
            self.budget = data.get("budget")
        except (json.JSONDecodeError, OSError):
            print("Could not read saved data. Starting with empty data.")

    def save_data(self):
        DATA_FILE.write_text(json.dumps({"transactions": self.transactions, "budget": self.budget}, indent=4), encoding="utf-8")

    def add_transaction(self, transaction_type, amount, category, note=""):
        self.transactions.append({"date": date.today().isoformat(), "type": transaction_type,
                                  "amount": round(amount, 2), "category": category, "note": note})
        self.save_data()

    def total_income(self):
        return round(sum(t["amount"] for t in self.transactions if t["type"] == "Income"), 2)

    def total_expense(self):
        return round(sum(t["amount"] for t in self.transactions if t["type"] == "Expense"), 2)

    def balance(self):
        return round(self.total_income() - self.total_expense(), 2)

    def category_summary(self):
        summary = {}
        for t in self.transactions:
            if t["type"] == "Expense":
                summary[t["category"]] = summary.get(t["category"], 0) + t["amount"]
        return {k: round(v, 2) for k, v in summary.items()}

    def monthly_expense(self, month):
        if len(month) != 7 or month[4] != "-":
            raise ValueError("Invalid month")
        try:
            year, month_number = int(month[:4]), int(month[5:])
            if year < 1 or not 1 <= month_number <= 12:
                raise ValueError
        except ValueError:
            raise ValueError("Invalid month")
        return round(sum(t["amount"] for t in self.transactions
                         if t["type"] == "Expense" and t["date"][:7] == month), 2)

    def set_budget(self, amount):
        self.budget = round(amount, 2)
        self.save_data()

    def current_month(self):
        return date.today().strftime("%Y-%m")
