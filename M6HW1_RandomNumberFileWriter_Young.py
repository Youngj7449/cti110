#Generates Random Numbers
#7/23/17
#CTI-110 M6HW1 - Random Number FIle Writer
#Jessica Young
#


import random

randfile = open("Randomnm.txt", "w" )

for i in range(int(input("How many number would you like to generate?: "))):
    line = str(random.randint(1, 500)) + "\n"
    randfile.write(line)
    print(line)

randfile.close()
