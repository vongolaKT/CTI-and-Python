# Description: Make a function that calculates the price per mile given a vehicles mpg and the cost of gas for 20, 75, and 500 mile intervals
# 11/25/2020
# CTI-110 P2LAB1 - Driving Costs
# Kevin Griffin

def mpgCost(): 
    mileGal = float(input('What is your vehicles miles per gallon?'))
    gasCost = float(input('What is the price of gas?'))
    costMile = gasCost / mileGal

    
    mile20 = 20 * costMile
    mile75 = 75 * costMile
    mile500 = 500 * costMile


    print('{:.2f} {:.2f} {:.2f}'.format(mile20, mile75, mile500))


mpgCost()

