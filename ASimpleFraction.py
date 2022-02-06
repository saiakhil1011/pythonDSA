def fractionToDecimal(numerator, denominator):
    if denominator == 0:
        return("Operation not possible!! Change denominator to non-zero number")
    fraction = numerator / denominator
    if numerator % denominator == 0: # if the remainder is zero there is no decimal so return integer.
        return(int(fraction))
    if fraction * denominator == numerator:
        return(5)
    print("check!!")
    quotient = numerator // denominator
    remainder = numerator % denominator
    repeat = ''
    decimal = str(remainder/denominator).split(".")[1]
    p = 1
    i = 0
    while i+p < len(decimal):
        if decimal[i] == decimal[i+p]:
            i += 1
            repeat = decimal[i]
        else:
            repeat = decimal[:i]
            p = len(repeat)
            i = 0
    #return('{}.({})'.format(quotient, repeat))
    return(repeat)



p = fractionToDecimal(1,3)
print(p)