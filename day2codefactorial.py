                  #150 DAYS PYTHON CODING
                   #DAY2 PYTHON CODE
#TO FIND A FACTORIAL OF A GIVEN INPUT NUMBER
#4!=4*3*2*1=24
def fact(number):
    if number==0:
        return 1
    return number*fact(number-1)
print("enter the value of the number")
number=int(input())
print("factorial of number is :", fact(number))