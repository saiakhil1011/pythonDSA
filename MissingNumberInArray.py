#Given an array of size N-1 such that it only 
# contains distinct integers in the range of 1 to N. 
# Find the missing element.
def MissingNumber(array,n):
        # code here
        total_sum = n*(n+1)/2 # calculates the total sum of n integers
        array_sum = sum(array) #calculates the sum of the array
        missingNum = total_sum - array_sum
        return(int(missingNum))