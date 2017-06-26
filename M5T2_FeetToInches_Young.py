#Converts feet to inches
#6/26/2017
#CTI-110 M5T2_FeetToInches
#Jessica Young
#
#
Inches_per_foot = 12

def main():

    feet = int(input('Enter a number of feet: '))
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')
    
def feet_to_inches (feet):
    return feet * Inches_per_foot

main()
