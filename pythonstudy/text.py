# num = 0
# numArr = []
# for i in range( 1, 101 ):
# 	if( i % 5 == 0 ):
# 		num= num + 1
# 		numArr.append(i)

# print( num )
# print( numArr )

num = 12
numArr = []
for i in range(10):
	numArr.append(num)
	num = num + 31
print(numArr)