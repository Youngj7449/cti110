#This project will calculate the total amount of a meal including tax and tip
#6/11/2017
#CTI-110 M2HW2- Tip Tax Total
#Jessica Young
#
#

CostofMeal = float( input ('Enter the cost of the meal: '))

tip = 0.18 * CostofMeal
tax = 0.07 * CostofMeal

total = CostofMeal + tip + tax

print ('The total cost of your meal is $' + format(total, ',.2f'))

