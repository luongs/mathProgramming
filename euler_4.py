# Find largest palindrome made from product of 3 nums
# eg: 9009 = 91 x 99
# Sebastien Luong

# biggest possible 2 digit num
MAXNUM=999
MINNUM=100
startNum=999999
tempNum=startNum

divAns=0
HTHOUSAND=100000
TTHOUSAND=10000
THOUSAND=1000
HUNDRED=100
DEC=10
DIG=1

def checkDig(palNum):
	divisor=MAXNUM
	while(divisor>MINNUM):
		divAns=palNum/divisor
		if (palNum%divisor == 0) and (MAXNUM>=divAns>=MINNUM):
		# divisor giving a palindrome is found
			return str(divisor)+" and "+str(divAns)+" divide "+str(palNum)
		else:
			divisor-=1
	return ""

# Create palindrome numbers
for i in range(0,10):
	tempNum=startNum-i*HTHOUSAND
	tempNum=tempNum-i*DIG
	# check if divisor found
	if (checkDig(tempNum) != ""):
		answer=checkDig(tempNum) 
		print answer
	for p in range(0,10):
		tempNum2=tempNum-p*TTHOUSAND
		tempNum2=tempNum2-p*DEC
		if (checkDig(tempNum2) != ""):
			answer=checkDig(tempNum2) 
			print answer
		for q in range (0,10):
			tempNum3=tempNum2-q*THOUSAND
			tempNum3=tempNum3-q*HUNDRED
			if (checkDig(tempNum3) != ""):
				answer=checkDig(tempNum3) 
				print answer
			#print "Inner "+str(tempNum3)


#front=0
#back=0
#divAns=0





'''
while (startNum>0):
	# check if number is palindrome
	front=startNum/100000
	back=startNum%100000
	print startNum
	if (front == back):
		tempNum=startNum/100000-startNum%100000
		# remove last number
		tempNum/=10
		front=tempNum/1000
		back=tempNum%1000
		if (front == back):
			tempNum=startNum/1000-startNum%1000
			# remove last number
			tempNum/=10
			front=tempNum/10
			back=tempNum%10
			if (front == back):
				# number is a palindrome
				print "yes"
				print str(startNum)
				divAns=startNum/divisor
				if (startNum%divisor == 0) and (divAns > MINNUM):
					# divisor giving a palindrome is found
					break
				# if no divisor found then check next start num
				elif (divisor <= MINNUM):
					divisor=MAXNUM
					startNum-=1
				# move to next divisor
				else:
					divisor-=1
			else:
				startNum-=1
		else:
			startNum-=1
	else:
		startNum-=1


print str(divisor)+" and "+str(divAns)+" create following palindrome: "+str(startNum)
'''