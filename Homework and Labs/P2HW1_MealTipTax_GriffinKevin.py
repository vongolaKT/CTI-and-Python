# function that calculates tip and tax and displays them along with the total
# 11/25/2020
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Kevin Griffin

def tipTax():
    # Get the total for the food and the tip and tax

    foodCost = float(input('Enter Food Cost: '))
    print(' ')
    tipPercent = float(input('Enter tip percentage: '))
    taxPercent = float(input('Enter tax percentage: '))
    print(' ')

    # In the instructions it says the input should be a decimal, however in the picture it clearly show that
    # an integer was entered so idk
    # I am going to make it like the instructions

    # calculate the tip total and tax total

    tipTotal = foodCost * tipPercent    # I could use an if else statement on if the number entered
    taxTotal = foodCost * taxPercent    # was greater than or equal to 1 and then if it was divide by 100

    # Print the number which is already a float, formatted to 2 decimal places
    print("{:.2f}".format(tipTotal))
    print("{:.2f}".format(taxTotal))

    # calculate the final cost by adding the orignal cost with the tip and tax
    finalTotal = foodCost + tipTotal + taxTotal

    print(' ')  # Space them out cause it looks better

    # Print the final total formatted to 2 decimal places
    print('Total including tip and tax: ' + "{:.2f}".format(finalTotal))

tipTax()