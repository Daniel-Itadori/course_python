"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""

def suma_args(*numbers):
    return sum(numbers)

print(suma_args(1, 2, 3, 4, 5))

"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""



"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""
def calculate_expenses (name, monthly_income, *var_exp, **fix_exp):
    # s = 0
    # su = 0
    # for _ in fix_exp:
    #     s += fix_exp[_]
    # for _ in var_exp:
    #     su += _

    income = monthly_income-sum(var_exp)-sum(fix_exp.values()) #con el sum(expenses) y el .values nos ahorramos los for
    print(f'Hi {name}, your actually income is: {income}')

calculate_expenses('Daniel', 10000, 45, 100, 1500, 45, internet=500, food=1000, coffe=2000)

print(*range(7))