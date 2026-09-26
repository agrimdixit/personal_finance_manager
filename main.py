from finance_manager import FinanceManager
from utils import clear_screen, pause, money


def show_menu():
    print("\n" + "=" * 50)
    print("              MONEY MANAGER")
    print("=" * 50)
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. Category summary")
    print("5. Monthly spending")
    print("6. Current balance")
    print("7. Set monthly budget")
    print("8. Budget status")
    print("9. Exit")
    print("=" * 50)


def read_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Enter an amount greater than 0.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number.")


def add_income(manager):
    clear_screen(); print("ADD INCOME")
    amount = read_amount("Amount: ₹")
    source = input("Income source: ").strip() or "Other"
    manager.add_transaction("Income", amount, source)
    print(f"Income of {money(amount)} added."); pause()


def add_expense(manager):
    clear_screen(); print("ADD EXPENSE")
    amount = read_amount("Amount: ₹")
    category = input("Category: ").strip().title() or "Other"
    note = input("Note: ").strip()
    manager.add_transaction("Expense", amount, category, note)
    print(f"Expense of {money(amount)} added."); pause()


def view_transactions(manager):
    clear_screen(); print("TRANSACTION HISTORY"); print("-" * 75)
    if not manager.transactions:
        print("No transactions recorded yet."); pause(); return
    for i, t in enumerate(manager.transactions, 1):
        extra = f" | {t['note']}" if t['note'] else ""
        print(f"{i:>3}. {t['date']} | {t['type']:<7} | {t['category']:<15} | {money(t['amount']):>12}{extra}")
    print("-" * 75)
    print(f"Total income : {money(manager.total_income())}")
    print(f"Total expense: {money(manager.total_expense())}"); pause()


def category_summary(manager):
    clear_screen(); print("EXPENSE BY CATEGORY"); print("-" * 45)
    summary = manager.category_summary()
    if not summary:
        print("No expenses recorded yet.")
    else:
        for category, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{category:<25} {money(amount):>15}")
    pause()


def monthly_spending(manager):
    clear_screen(); month = input("Enter month (YYYY-MM): ").strip()
    try:
        print(f"\nExpense for {month}: {money(manager.monthly_expense(month))}")
    except ValueError:
        print("Use the format YYYY-MM.")
    pause()


def current_balance(manager):
    clear_screen(); print("CURRENT FINANCIAL STATUS"); print("-" * 40)
    print(f"Total income : {money(manager.total_income())}")
    print(f"Total expense: {money(manager.total_expense())}")
    print(f"Balance      : {money(manager.balance())}"); pause()


def set_budget(manager):
    clear_screen(); print("MONTHLY BUDGET")
    amount = read_amount("Budget amount: ₹")
    manager.set_budget(amount)
    print(f"Monthly budget set to {money(amount)}."); pause()


def budget_status(manager):
    clear_screen(); print("BUDGET STATUS"); print("-" * 40)
    if manager.budget is None:
        print("No monthly budget has been set.")
    else:
        spent = manager.monthly_expense(manager.current_month())
        remaining = manager.budget - spent
        print(f"Budget    : {money(manager.budget)}")
        print(f"Spent     : {money(spent)}")
        print(f"Remaining : {money(remaining)}")
        print((f"Over budget by {money(abs(remaining))}." if remaining < 0
               else f"You have {money(remaining)} left."))
    pause()


def main():
    manager = FinanceManager()
    actions = {"1": add_income, "2": add_expense, "3": view_transactions,
               "4": category_summary, "5": monthly_spending, "6": current_balance,
               "7": set_budget, "8": budget_status}
    while True:
        clear_screen(); show_menu(); choice = input("Choose an option: ").strip()
        if choice == "9":
            print("\nThanks for using Money Manager."); break
        action = actions.get(choice)
        if action: action(manager)
        else: print("Invalid option."); pause()


if __name__ == "__main__":
    main()
