# function that calculates tip and tax and displays them along with the total
# 12/4/2020
# CTI-110 P4HW2 - Meal Tip Tax Calculator Revised with loops
# Kevin Griffin

def tipTax():
    # Get the total for the food
    cont = 'y'
    while cont == 'y':
        if cont != 'y':
            break
        foodCost = float(input('Enter Food Cost: '))
        print(' ')
            # function for getting tip input, calls until one of the three prompted are typed in
        def tipPerc():
            # need to reset this value in each call
            tipPercent = float(input('Enter tip percentage 16, 18 or 20: '))

            if tipPercent == 16:
                return tipPercent
            elif tipPercent == 18:
                return tipPercent
            elif tipPercent == 20:
                return tipPercent
            else:
                print('Please re-enter a correct value')
                # calls until one of the above inputs is given, some form of recursion?
                tipPercent = tipPerc()
                return tipPercent
        
        # call the function and assign the returned value to tipPercent
        tipPercent = tipPerc()
        print(' ')
        taxPercent = 6
        print(' ')


        # calculate the tip total and tax total

        tipTotal = foodCost * (tipPercent/100)
        taxTotal = foodCost * (taxPercent/100)   

        # Print the number which is already a float, formatted to 2 decimal places
        print(' ')
        print('Meal price: ' + str("{:.2f}".format(foodCost)))
        print('Tip: ' + str("{:.2f}".format(tipTotal)))
        print('Tax: ' + str("{:.2f}".format(taxTotal)))

        # calculate the final cost by adding the orignal cost with the tip and tax
        finalTotal = foodCost + tipTotal + taxTotal

        print(' ')  # Space them out cause it looks better

        # Print the final total formatted to 2 decimal places
        print('Total: ' + str("{:.2f}".format(finalTotal)))

        cont = input('Do you want to calculate a different tip? (y/n) :')

tipTax()