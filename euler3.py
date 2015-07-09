n = 600851475143
factors = []
i = 2

while i * i <= n: 
   while n % i == 0:
      n /= i
      factors.append(i)
   i += 1
   

print(factors)
print(n) #this is the highest prime factor 


#n here is the limit
#factors is an empty list meant to eventually contain the prime factors of the limti 
#start at 2 (i)
#while i * i <= n (don't want to go above the prime factor)
#while n / i == 0 (prime factor needs to be evenly divisible
#Divide the limit by i and store it (n = n / i)
#Append this factor to the factors list
#Increase the start by 1
#Print the ending factors list and print the highest prime factor 


#: Start with i = 2 because 2 is the smallest prime number 
#: i*i is less than/equal to n because the largest prime factor will never be larger than the square root of n
#: The inner loop stops when n is no longer divisible by i 
#: The outer loop eventually makes the while statement untrue; i squared will eventually be greater than n 

'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
