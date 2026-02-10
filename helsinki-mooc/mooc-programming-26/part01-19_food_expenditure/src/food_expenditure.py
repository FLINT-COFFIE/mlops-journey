# Write your solution here
#inputs
days = int(input("Number of days at the cafeteria: "))
price = float(input("Price of lunch: "))
groceries = float(input("Price of groceries: "))

#calculations
weekly = (price * days) + groceries
daily = weekly / 7

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")