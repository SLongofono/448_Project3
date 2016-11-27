import math
import array
array = [
[  4,  6,  1, -3,-12],
[  9, 14, -4, 32,  0],
[ 22, -3, 12, -2,  8],
[  4,  4,  4,  4,  4]]

def calculateStdDev():
	for row in array:
		mean=sum(row)/len(row)
		print("Std Dev=",(sum( (x-mean)**2.0 for x in row ) / float(len(row)) )**0.5)
calculateStdDev()
