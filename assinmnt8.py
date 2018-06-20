       #assinmnt-8
#1.  what is time tuple	


#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

# Index	Field	Values
# 0	4-digit year	2008
# 1	Month	1 to 12
# 2	Day	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	0 to 6 (0 is Monday)
# 7	Day of year	1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST
# The above tuple is equivalent to struct_time structure. T


#2.write a program to get formatted time.

import time 
print(time.asctime(time.localtime(time.time())))
 
 
   
#3.extract month from he time
#4.exract day from the time   