#Totals how many bugs you have collected over the course of 5 days.
#6/15/2017
#CTI-110 M4T1 - Bug Collector
#Jessica Young


total = 0

for day in range(1, 6):
    print ('Enter the bugs collected on day', day)
    bugs = int(input())
    total += bugs


print('You collected a total of', total, 'bugs.')
