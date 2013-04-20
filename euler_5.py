#Euler Smallest multiple question
#Sebastien Luong

multiple=20
divider=19
# increases the multiple by its original value until all other smaller numbers  
# can be divided by it
while (divider != 0) :
	if multiple%divider !=0:
		multiple=multiple+20
		divider=19
	else:
		divider-=1

print multiple
