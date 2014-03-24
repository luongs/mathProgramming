# first find pyth triplet for numbers 1-10
# 3,4,5 should be returned

def reverseList(firstList):
	tempList=[]
	for i in range(len(firstList)): 
		tempList.append(firstList.pop())
	return tempList

listInc=[]
tempList=[]
listDec=[]
fstTriple = 0
secTriple = 0
thdTriple = 0

for i in range(1,100):
	listInc.append(i)
	tempList.append(i)
listDec=reverseList(tempList)

# Using euclid's method
# m and n do not have to be coprime!
for k in range(1,100):
	for m in listInc:
		for n in listDec:
			fstTriple=k*(m**2-n**2)
			secTriple= k*(2*m*n)
			thdTriple = k*(n**2 + m**2)
		if (fstTriple+secTriple+thdTriple==1000):
				print str(fstTriple)
				print str(secTriple) 
				print str(thdTriple)
				print("Final value: "+str(fstTriple*secTriple*thdTriple))
		


'''
# Create a list of prime numbers
primeArray_length = 100
primeArray = []
revPrimeArray = []
tempList=[]
count = 0
number = 3
fstTriple = 0
secTriple = 0
thdTriple = 0


while count <= primeArray_length:
	for i in range(2,number):
		if number % i == 0:
			break
		if i == number - 1:
			primeArray.append(number)
			tempList.append(number)
			count += 1
	number += 1

#for i in primeArray:
#	print i

revPrimeArray = reverseList(tempList)
for k in range (2,50):
	for n in revPrimeArray:
		for m in primeArray:
			if (n==m):
				break
			print (n-m)
			if ((n-m)%2==0):
				continue
			#print("reached")
			fstTriple=k*(n**2-m**2)
			secTriple= k*(2*m*n)
			thdTriple = k*(n**2 + m**2)
			print (fstTriple+secTriple+thdTriple)
			if (fstTriple+secTriple+thdTriple==1000):
				print("Yes!")
				print str(fstTriple)
				print str(secTriple) 
				print str(thdTriple)

# Find prime pythogorean triple
# Check and stop if the three add up to 1000
'''

'''
listA=[]
listB=[]
listC=[]
listCrev=[]

def reverseList(firstList):
	tempList=[]
	for i in range(len(firstList)): 
		tempList.append(firstList.pop())
	return tempList

def subtractList(revListC, listB, listA):
	print revListC
	print listB
	sumList=[]
	for i in range(len(listA)):
		for p in range(len(listB)):
			sumList.append(listA[i]+listB[p])
	for i in sumList: 
		for p in range(len(revListC)):
			if (i==revListC[p]):
				print i
				break
	
			

# Set up all squared values within lists
for i in range(1,11):
	listA.append(i**2)
	listB.append(i**2)
	listC.append(i**2)
	#print "List A: "+str(listA[i-1])

reverseC=reverseList(listC)
subtractList(reverseC, listB, listA)
'''
