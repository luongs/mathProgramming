# find 10,001st prime num using a modified Sieve of Eratosthenes
# Author Sebastien Luong

TARGET_PRIME=10001
MIN_NUMBER=2 
primeCounter=0
counter=1; 

#MAXNUMBER=500000
#normalList=[]
#primeList=[2]
#normCounter=0
#listCount=0


# brute force!
while (TARGET_PRIME > primeCounter):
    counter+=1
    for i in range (2, counter+1):
	    if (i == counter):
	    	primeCounter+=1
	    	print i
	    	break
	    if (counter % i == 0):
	        break
			

	



#Create list
'''
for i in range(2,MAXNUMBER):
	normalList.append(True)

#Check for prime numbers
while (primeCounter<TARGET_PRIME):
	while (inc<MAXNUMBER):
		inc=primeList[primeCounter]*2
		normalList[inc]=False
	
primeList.append()
'''


'''
while(len(primeList)<TARGET_PRIME):
	
	for i in primeList:
		print "i "+str(i)
		print "number "+str(number)
		print "list count "+str(listCount)
		print "len primeList "+str(len(primeList))
		if (number%i != 0):
			if (listCount >= len(primeList)):
				primeList.append(number)
				listCount=0
				print "yes"
			else:
				listCount+=1
		else:
			number+=1
			listCount+=1
			

for i in primeList:
	print str(i)
'''
