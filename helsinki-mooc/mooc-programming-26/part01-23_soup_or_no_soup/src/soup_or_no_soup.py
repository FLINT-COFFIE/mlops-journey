# Write your solution here
name = input("Enter your name: ")

#conditionals
if name == "Jerry":
    print("Next please!")
    
if name != "Jerry":
    portion = int(input("How many portions: "))
    price = 5.90 * portion
    print(f"The total cost is {price} Next please!")