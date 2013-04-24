# find 10,001st prime num

max=0
divisorArr=[]
num=long(600851475143)
#num=20

div=num
initPrime=2
while (div > 1): 
	while (div%initPrime==0):
		divisorArr.append(initPrime)
		div /= initPrime
	initPrime += 1

for i in divisorArr:
	print i