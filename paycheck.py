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
