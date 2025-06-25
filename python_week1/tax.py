name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic monthly salary (₹): "))
special_allowance = float(input("Enter monthly special allowance (₹): "))
bonus_percent = float(input("Enter annual bonus percentage: "))

gross_monthly = basic_salary + special_allowance
annual_gross = gross_monthly * 12
bonus = annual_gross * (bonus_percent / 100)
annual_gross += bonus

standard_deduction = 50000
taxable_income = annual_gross - standard_deduction

tax = 0
if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = 15000 + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = 45000 + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = 90000 + (taxable_income - 1200000) * 0.20
else:
    tax = 150000 + (taxable_income - 1500000) * 0.30

if taxable_income <= 700000:
    tax = 0

cess = tax * 0.04
total_tax = tax + cess

net_salary = annual_gross - total_tax

print("\n----- Salary and Tax Report -----")
print("Employee Name       :", name)
print("Employee ID         :", emp_id)
print("Gross Monthly Salary: ₹", round(gross_monthly, 2))
print("Annual Gross Salary : ₹", round(annual_gross, 2))
print("Taxable Income      : ₹", round(taxable_income, 2))
print("Tax Payable         : ₹", round(tax, 2))
print("Cess (4%)           : ₹", round(cess, 2))
print("Total Tax Payable   : ₹", round(total_tax, 2))
print("Annual Net Salary   : ₹", round(net_salary, 2))
