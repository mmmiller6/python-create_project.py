# Name: Mayowa Miller
# Date: 2026-09-18
# Course: COMP 163
# Project 1: Paycheck Calculator

employee_name = input()
hours_worked = float(input())
hourly_rate = float(input())
tax_rate = float(input())

gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld

print(f"Employee: {employee_name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")
