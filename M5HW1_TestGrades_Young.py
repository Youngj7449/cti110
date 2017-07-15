#Calculates letter grade and average test score
#7/9/2017
#CTI-110 M5HW1 - Test Average and Grade
#Jessica Young
#
#

def main():
    total = 0; avg = 0; letter_grade = 0
def calc_average(total):
    return total / 5

    def determine_grade( user_score):
        if( user_score < 60 ):
            return "F"
        elif( user_score < 70):
            return "D"
        elif ( user_score < 80):
            return "C"
        elif ( user_score < 90):
            return "B"
        elif ( user_scrore <= 100):
            return "A"



while(True):
    grade = int(input("Enter grade: "))
    total += grade
    avg = calc_average(total)
    letter_grade = determine_grade(grade)

    print("The average grade is: " + str(avg))
    print("The letter grades are: " + str(letter_grade))


main()
                   
                          

