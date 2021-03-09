# Name: Daniel Greenwald
# Investment Report Assignment
#This program gathers investment information from the user such as innitial investment amount, desired interest rate, and the amount of years for the projected investment. Then the program uses those imputs to calculate a table of differnent values during the investment's life cycle.

def inputs():
    global rate
    global years
    global InitialAmount
    InitialAmount = float(input('Please enter your initial investment amount in USD (do not include $ sign): ')) #Promps user to enter investment amount.
    rate = float(input('Enter your desired interest rate (do not include % sign): ')) #Prompts user to enter the desired interest rate.
    years = float(input('Enter the amount of years you plan to invest: ')) #Prompts the user to enter the investment time.

inputs()

def adjusters():
    global decimal_rate
    global i
    global y
    global fb
    global te
    decimal_rate = rate * 0.01 #Turns the interest rate from a whole number to a decimal so that it can be calculated properly in the equation.
    fb = InitialAmount * ((1 + decimal_rate) ** years) #Calculated the final balance of the investment.
    te = fb - InitialAmount # Calculated the Total Amount of Income Earned for the investment period.
    i = 1
    y = 1
    print('{:<13} {:<1}'.format('','Annual Fixed Investment Report')) #Prints the table heading.
    print('{:<8} {:<19} {:<17} {:<2}'.format('Year','Starting Balance','Annual Income','Ending Balance')) #Prints the Columb headers.
adjusters()


def outputs():
    global i
    global InitialAmount
    global decimal_rate
    global eb
    ai = (InitialAmount * (1 + decimal_rate)) - InitialAmount #Calculates all the rows for the annual income columb.
    eb = InitialAmount * (1 + decimal_rate) #Calculates all the rows for the ending balance columb.
    print('{:<8} {:<19} {:<17} {:<2}'.format(i, str(round(InitialAmount, 2)), str(round(ai, 2)), str(round(eb, 2)))) #Prints the table outputs in a loop until the desired year is hit.
    i = i + 1
    if i <= years:
        InitialAmount = (InitialAmount * (1 + decimal_rate))
        outputs()
outputs()

def final():
    print('')
    print('Ending Balance: ${}'.format(str(round(fb, 2)))) #Prints the final ending balance.
    print('')
    print('Total Amount of Income Earned: ${}'.format(str(round((te), 2)))) #Prints the total amount of income earned for the investment.

final()
