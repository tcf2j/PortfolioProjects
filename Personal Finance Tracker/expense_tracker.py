#Developer: Tyler Fisher
#1/7/2025
#Personal Finance Tracker
from expense import Expense
import pandas as pd
import csv 

def main():
    print("📊 Finance Tracker Running! 📊 ")
    expense_file_path = "expenses.csv"
    budget_file_path = "budget.csv"
    #Getting Budget
    budget = getting_budget(budget_file_path)
    #User enters expense 
    expense = user_entry()
    #Save expense to CSV file
    save_expense(expense, expense_file_path)
    #Summarize expense totals
    total_summary(expense_file_path, budget)
    

def user_entry():
    expense_name = input("What is the expense? ")

    expense_categories = [
        "📑 Bills",
        "🍔 Food",
        "🚕 Travel",
        "🎉 Entertainment",
        "👾 Misc"
    ]
    for i,category_name in enumerate(expense_categories):
        print(f"{i+1}. {category_name}")
    
    while True:
        while True: 
            category_index = (input("What is the category [1-5] "))
            try: 
                int(category_index)
                break
            except ValueError:
                print("Invalid Input")   
        category_index = int(category_index)
        if category_index > 0 and category_index < 6:
            category_index -= 1
            break
        else:
            print("Invalid Input")
   
    while True:
        expense_amount = input("How much was the expense? ")
        try: 
            float(expense_amount)
            break
        except:
            print("Invalid Input")
    expense_amount = f"{float(expense_amount):.2f}"
    
    expense = Expense(expense_name, expense_categories[category_index], expense_amount)
    return expense


def save_expense(expense: Expense, filepath): 
    with open(filepath, "a",encoding='utf-8') as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")
    

def total_summary(filepath, budget):
    print("📊 Your Summary!")
    expenses: list[Expense]=[]
    with open(filepath, "r",encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense (
                name=expense_name,category=expense_category,amount=float(expense_amount))
            expenses.append(line_expense)
    
    category_amount = {}
    for expense in expenses:
        key = expense.category
        if key in category_amount:
            category_amount[key] += expense.amount
        else:
            category_amount[key] = expense.amount
    
    print("Each Category Expense: ")
    for key, amount in category_amount.items():
        print(f"  {key}: ${amount:.2f}")

    total_amount = sum([x.amount for x in expenses])
    print(f"You've Spent ${total_amount:.2f}!")

    remaining_budget = budget - total_amount
    print(green(f"Your Remaining Budget {remaining_budget:.2f}!"))

def getting_budget(file_path):
    with open(file_path, "r", encoding='utf-8' ) as f:
        budget = f.readline()
    budget = float(budget)

    if budget == 0:
        while True:
            user_input = input("Please enter your budget: ")
            try:
                float(user_input)
                break
            except:
                print("Invalid entry")
        budget = float(user_input)
        print(f"Thank you!👍 Budget: ${budget:.2f}")

        with open(file_path,"w", encoding='utf-8') as f:
            f.write(f"{budget}\n")


        return budget
    else:
        return budget



def green(text):
    return f"\033[92m{text}\033[0m"    

if __name__ =="__main__":
    main()