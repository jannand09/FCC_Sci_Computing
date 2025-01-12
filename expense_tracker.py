# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:33:52 2024

@author: janna
"""

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))


def filter_expenses_by_category(expenses, category):
    lambda expense: expense['category'] == category
    
expenses = []