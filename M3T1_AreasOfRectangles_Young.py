# Calculate the area of two rectangles and determine which one is greater
#6/14/2017
#CTI-110 M3T1 - Areas of Rectangles
#Jessica Young
#
#

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))


length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2


if area1 > area2:
    print ('Rectangle 1 has a greater area.')
else:
    if area2 > area1:
        print('Rectangle 2 has a greater area.')
    else:
        print('Both rectangles have the same area.')
        
