# A persons age is entered and then they're classified as infant, child, teenager or adult
#6/15/2017
#CTI-110 M#HW1 - Age Classifier
#Jessica Young
#
#


user_age = int(input('Enter individuals age: '))

if user_age <= 1:
    Print ('They are an infant.')
elif user_age > 1 and user_age < 13:
    print ('They are a child.')
elif user_age >= 13 and user_age < 20:
    print ('They are a teenager.')
elif user_age >= 20:
    print ('They are an adult.')
else:
    print ('You are an alien.')
