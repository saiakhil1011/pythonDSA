#For an integer N find the number of trailing zeroes in N!.

def trailingZeroes(N):
    	#code here 
    if N < 0:
    	return(-1)
    	
    #if N is not zero and greater than or equal to 5
    zeros = 0
    while N >= 5:
    	N //= 5   #calculate floor division and reassign the value to N
    	zeros += N #update the trailing zeros
    return(zeros)