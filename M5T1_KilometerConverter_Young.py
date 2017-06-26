#Converts kilmeters to miles
#6/26/2017
#CTI-110 M5T1_KilometerConverter
#Jessica Young
#
#



Conversion_Factor = 0.6214

def main ():
    kilometers = float(input('Enter a distance in kilometers: '))
    show_miles(kilometers)
                             

def show_miles(km):
    miles = km * Conversion_Factor

    print(km, 'kilometers equals', miles, 'miles.')


main()
