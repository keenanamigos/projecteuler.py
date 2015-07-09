x = 0 
for i in range (1,1000):
   if (i % 3 == 0 or i % 5 == 0):
      x += i
print x

#Set ending total variable (x) to 0
#For loop to run from 1-1000
#number (i) needs to be divisible either by 3 or by 5
#If this is true, add said number (i) to the running total variable (x)
#Print the ending total (x)

#Answer: 233168
'''Problem: If we list all the natural 
numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.'''
