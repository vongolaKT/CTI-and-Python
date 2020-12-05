# CTI-110
# P4HW1 - Expenses
# Kevin Griffin
# 12/4/2020

def Expenses():
    # Starting balance
    acctStartBal = float(input('Enter starting amount in account $'))
    # establish cont var
    cont = 'y'
    # Ask for first Expense
    expenAmt = float(input('Enter expense '+str(1)+': '))
    # Variable for keeping track of balance after each expense
    newBal = acctStartBal - expenAmt
    # establish 1st transaction
    transNum = 1

    # While loop if user enters y
    while cont == 'y':

        cont = input('Do you want to enter another Expense? (enter y to continue): ')

        #Lazy coding haha, didn't want to figure out where to place cont because where it is right now doesn't
        #work correctly, so if cont is != y then break before looping again
        if cont != 'y':
            break

        # Keeping track of number of expenses
        transNum += 1

        # Asking for the next expense and every one after
        expenAmt = float(input('Enter expense '+str(transNum)+': '))

        # Subtracting each new expense
        newBal =  newBal - expenAmt


    print('Original amount in account before expenses: $'+str(acctStartBal))
    print('Number of expenses entered: '+str(transNum))
    print('Amount in account after expenses: $'+str(newBal))

Expenses()