def is_leap(year):
    leap=False
    if (year % 4 != 0):
        leap = False
    else:
        if (year % 100 != 0):leap = True
        else:
            if (year % 400 == 0):leap = True
            else: leap=False
    return leap

#In this function we find whether a given year is a leap year or not.
#A year is said to be leap year if it is divisible by 4.
#If the year divisible by 4 is also divisible by 100 then it must be divisible by 400 else it is not a leap year.
#The logical operators used are :
#'==' is equal - It validates whether the operands on both sides are equal and returns true relse false.
#'!=' is not equal - It validates whether the operands on either side are not equal and returns true else false.