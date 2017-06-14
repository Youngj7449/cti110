#calculates if you grade will  be an A,B,C,D or F based on score
#6/14/2017
#CTI-110 M3T2 - Debugging
#Jessica Young
#
#
#

A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 59

score = int(input('Enter your score: '))


if score >= A_score:
    print('Your grade is A!')
else:
    if score >= B_score:
        print ('Your grade is B!')
    else:
        if score >= C_score:
            print ('Your grade is C.')
        else:
            if score >= D_score:
                print ('Your grade is D.')
            else:
                print ('Your grade is F.')
