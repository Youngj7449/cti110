#This program will add all the numbers a user inputs until a negative numbers is input. Then it will display the sum
#6/23/2017
#CTI-110 M4HW1 -Sum of Numbers
#Jessica Young
#




total = 0
userNumber = float( input( "Enter the first number or a negative " + "number to quit: "))
while userNumber > -1:
    total = total + userNumber
    userNumber = float( input( "Enter the next number or a "+ "negative number to quit: "))                          


print( "The sum of all the numbers you entered is:",total)
                           
