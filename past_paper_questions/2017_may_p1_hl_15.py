# The collection WEATHER contains the temperatures that have been measured for one city
# over the course of one week, starting on Monday and ending on Sunday.  Each day,
# 24 readings were taken, one each hour, the first being at 00:00, the second at 01:00 and so 
# on. The data is stored in chronological order with the data for Monday stored in the collection 
# first, followed by Tuesday and so on.

import random

WEATHER = []
for i in range (24 * 7):
    WEATHER.append(round(random.uniform(-2, 7),2))


# (a) ...total number of readings that were taken during this week.
print(f"Total number of readings taken was {24 * 7}")


# (b) ...read data into a 2D array, A, that would allow the temperature on a specific day at a specific time to be accessed directly.
A = []
index = 0
for row in range(7):
    readings = []
    for col in range(24):
        readings.append(WEATHER[index])
        index += 1
    A.append(readings)
# print(*A, sep='\n')


# (c) ...output the day, as a word (for example Tuesday), on which the highest temperature was recorded.
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
HIGHEST = A[0][0]
HIGH_DAY = ''
for day_index in range(7):
    for reading_index in range(24):
        if A[day_index][reading_index] > HIGHEST:
            HIGHEST = A[day_index][reading_index]
            HIGH_DAY = WEEKDAYS[day_index]

print(f"Higest temperature was {HIGHEST}, taken on {HIGH_DAY}")
