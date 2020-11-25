# Description: 
# 11/17/2020
# CTI-110 P1HW2 - Basic Math
# Kevin Griffin

################################################################    OLD     ################################################################ 
# Pseudo Code
# get input vales from user and make sure to convert them to float to do math and avoid an error
# add them and multiply them
# print out string version of numbers and sum and product so they can be added to a string for a message at the end

# I wrote this during class when the example was for a payment calculation function. This can still be used for addition and multiplication

#def payCalc():                                                          # Defining the function so it can be used elsewhere in a larger project
#    hrsWorked = float (input('Enter Hours'))                            # Create an input that returns a float value of the entered number str
#    payRate = float (input('What is your pay?'))                        # Create an input that returns a float value of the entered number str
#    ttlPay = float (hrsWorked * payRate)                                # Multiplies the values for the total pay (product of the given numbers)
#    sumNum = float (hrsWorked + payRate)                                # Adds the two values for the sum of the two numbers

#    if hrsWorked > 40:                                                  # If else statement to help determine if the numbers are valid
#        print('Please check your numbers to verify you are correct')    # This was a one off suggestion in class, and doesnt really help as
#    elif payRate > 20:                                                  # all it does is print this statement if the value is true and doesnt
#        print('Please check your numbers to verify you are correct')    # do anything else, you even have to call the function again haha
#    else:
#        print('')                                                       # Added these to have a space in the prompt for easier reading
#        print(str(hrsWorked) + ' ' + 'Was the first number entered')
#        print(str(payRate) + ' ' + 'Was the second number entered')
#        print('')                                                       # Added these to have a space in the prompt for easier reading
#        print(str(sumNum) + ' ' + 'Is the sum of the two numbers')
#        print(str(ttlPay) + ' ' + 'Is the product of the two numbers equating to weekly pay in the context of hours and hourly wage.')

# I wrote this during class when the example was for a payment calculation function. This can still be used for addition and multiplication
        
#payCalc()
################################################################    OLD     ################################################################ 



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