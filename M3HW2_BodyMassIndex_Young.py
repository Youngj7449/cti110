# A user will enter height and weight and then their BMI will be calculated along with telling them if they are over or underweight
#6/15/2017
#CTI-110 M3HW2 Body Mass Index
#Jessica Young
#
#
#

user_Weight = int(input('Enter your weight:'))
user_Height = int(input('Enter your height:'))

userBMI = (user_Weight * 703 / (user_Height * user_Height))


if userBMI < 18.5:
    print ('Yout BMI is: ' + str(userBMI) + ' and you are underweight.')
elif userBMI > 25:
     print ('Yout BMI is: ' + str(userBMI) + ' and you are overweight.')
else:
    print ('Yout BMI is: ' + str(userBMI) + ' and you are at optimal weight.')
