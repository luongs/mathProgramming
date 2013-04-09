# Largest prime factor; find the largest prime factor 
#( primenumber that will divide given number)
# Author: Sebastien Luong

# Steps: determine if number divides the given number
# Determine if the number is a prime number
# Return the max prime number

# Test run with number 33

max=0
divisorArr=[]
num=long(600851475143)

div=num
initPrime=2
while (div > 1): 
	while (div%initPrime==0):
		divisorArr.append(initPrime)
		div /= initPrime
	initPrime += 1

for i in divisorArr:
	print i
'''
while i<num:
	print i
	if (num%i==0):
		# Append i if it is prime and divides num
		if (isPrime(i)):
			max=i
			divisorArr.append(i)
	
	i=2*i+1


for x in divisorArr:
	print x
print "Max prime number is: "+ str(max)

'''

