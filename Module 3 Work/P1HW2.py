# Description: Make a function that, when called, asks for hours worked and pay rate, rejects past a certain amount, to make it better I could nest ->
# another if else statement in to ask if they are allowing an the values that excede the presets, if yes then print ttlPay, if no then calls
# the function again as a reset
# 11/17/2020
# CTI-110 P1HW2 - Basic Math
# Kevin Griffin

# Pseudo Code
# get input vales from user and make sure to convert them to float to do math and avoid an error
# add them and multiply them
# print out string version of numbers and sum and product so they can be added to a string for a message at the end

# I wrote this during class when the example was for a payment calculation function. This can still be used for addition and multiplication

def payCalc():                                                          # Defining the function so it can be used elsewhere in a larger project
    hrsWorked = float (input('Enter Hours'))                            # Create an input that returns a float value of the entered number str
    payRate = float (input('What is your pay?'))                        # Create an input that returns a float value of the entered number str
    ttlPay = float (hrsWorked * payRate)                                # Multiplies the values for the total pay (product of the given numbers)
    sumNum = float (hrsWorked + payRate)                                # Adds the two values for the sum of the two numbers

    if hrsWorked > 40:                                                  # If else statement to help determine if the numbers are valid
        print('Please check your numbers to verify you are correct')    # This was a one off suggestion in class, and doesnt really help as
    elif payRate > 20:                                                  # all it does is print this statement if the value is true and doesnt
        print('Please check your numbers to verify you are correct')    # do anything else, you even have to call the function again haha
    else:
        print('')                                                       # Added these to have a space in the prompt for easier reading
        print(str(hrsWorked) + ' ' + 'Was the first number entered')
        print(str(payRate) + ' ' + 'Was the second number entered')
        print('')                                                       # Added these to have a space in the prompt for easier reading
        print(str(sumNum) + ' ' + 'Is the sum of the two numbers')
        print(str(ttlPay) + ' ' + 'Is the product of the two numbers equating to weekly pay in the context of hours and hourly wage.')

# I wrote this during class when the example was for a payment calculation function. This can still be used for addition and multiplication
        
payCalc()