# This program will calculate the amount of profit from a sale. The profit is set to 23 percent.
# 6/11/2017
#CTI-110 M2T1 - Sales Prediction
#Jessica Young
#

total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of the total sales.

profit = total_sales * 0.23

#Display the profit

print('The profit is $',format(profit, ',.2f'))
