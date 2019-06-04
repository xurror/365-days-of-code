
def change(dollars):
    cents = dollars * 100
    remainder = 0
    
    remainder = cents
    """    
#    if cents >= 100:
    remainder = cents % 100
    print("dollars: ",
        f"\t{(cents - remainder) / 100:.0f}")            
    cents = remainder"""
    
#    if remainder >= 25:
    remainder = (cents % 25)
    print("quarters: ",
        f"\t{(cents - remainder) / 25:.0f}")            
    cents = remainder

#    if remainder >= 10:
    remainder = cents % 10
    print("dimes: ",
        f"\t{(cents - remainder) / 10:.0f}")
    cents = remainder

#    if remainder >= 5:
    remainder = cents % 5
    print("nickels: ",
        f"\t{(cents - remainder) / 5:.0f}")            
    cents = remainder

#    if remainder < 5:
    print("pennies: ",
        f"\t{cents:.0f}")

if __name__ == '__main__':
    try:
        print("*** For this program I will be ",
            "using US dollars and cents. ***")
        
        print("In the US:\n",
            "\t- 1 dollar is 100 cents.\n",
            "\t- 1 quarter is 25 cents.\n",
            "\t- 1 dime is 10 cents.\n",
            "\t- 1 nickel is 5 cents.\n",
            "\t- 1 penny is 1 cent.\n",
            "-----------------------------------------\n")

        cost = eval(input("Cost of item: "))
        amount = eval(input("Amount paid: "))

        change(amount-cost)
                    
    except KeyboardInterrupt:
        exit()