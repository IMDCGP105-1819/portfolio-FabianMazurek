annual_salary =  int(input("Please enter you annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Please enter the price of your dream house: "))

current_savings = 0
months = 0
r = 0.04
monthly_salary = annual_salary / 12
portion_deposit = total_cost * .2
saving = portion_saved * monthly_salary


while current_savings <= portion_deposit:
    interest = current_savings * r / 12
    monthly_savings = interest + saving
    current_savings = current_savings + monthly_savings
    months = months + 1;

print("It will take you",  months,  "months to save up for your dream house!")
