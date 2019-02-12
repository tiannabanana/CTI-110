#Calculating the total amount for meals including tips.
#February 12,2019.
#CTI-110 P2HW2 - Meal Tip Calculator.
#Tianna Scott
#
# Get meal cost.
MealCost = float(input("Enter total cost of meal:"))

# Calculate tip as 15 percent of total cost.
Tip15 = MealCost * 0.15

#Display tip amount.
print("15 percent = $", format(Tip15,".2f"))

# Calculate total cost
Total15 = MealCost + Tip15

#Display total cost of meal.
print ("Total cost = $", Total15)

# Calculate tip as 18 percent of total cost.
Tip18 = MealCost * 0.18

#Display tip amount.
print("18 percent = $", format(Tip18,".2f"))

# Calculate total cost
Total18 = float(MealCost + Tip18)

#Display total cost of meal.
print ("Total cost = $", Total18)

# Calculate tip as 20 percent of total cost.
Tip20 = MealCost * 0.2

#Display tip amount.
print("20 percent = $", format(Tip20,".2f"))

# Calculate total cost
Total20 = float(MealCost + Tip20)

#Display total cost of meal.
print ("Total cost = $", Total20)

