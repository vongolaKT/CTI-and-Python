# Description: Make a function that takes two number and adds and multiplies them then displays all necessary info
# 11/17/2020
# CTI-110 P1HW2 - Basic Math
# Kevin Griffin

def basicMath():
    num1 = float (input('Enter first number :'))                     #Ask for first number and assign it to variable
    num2 = float (input('Enter second number :'))                    #Ask for second number and assign it to variable
    sumNum = num1 + num2                                           #Calculate summ of both numbers and assign it to a new variable     
    prodNum = num1 * num2                                          #Calc the product of the nums and give it a new variable

    print('')                                                   #space
    print(str(num1) + ' ' + 'Was the first number entered')         #prints first number
    print(str(num2) + ' ' + 'Was the second number entered')        #prints second number
    print('')                                                   #space
    print(str(sumNum) + ' ' + 'Is the sum of the two numbers')      #prints sum of both numbers
    print(str(prodNum) + ' ' + 'Is the product of the two numbers') #prints product of two numbers


basicMath()