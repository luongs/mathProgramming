#Euler Sum Square Difference 
#Sebastien Luong

sumSquare=0
squareSum=0
diff=0

for i in range(1,101):
	sumSquare+=i**2

for i in range(1,101):
	squareSum+=i

squareSum=squareSum**2

diff=squareSum-sumSquare

print diff