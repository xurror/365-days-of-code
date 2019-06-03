# Funtion to compute Factorial number
def factorial(n):
    if n == 1:
        return 1
    
    else:
        #print(f"call factorial funtion")
        return n*factorial(n - 1)

def eulersNumber(limit):
    # Initialise Euler's Number
    e = 1
    while limit > 0:
        e += 1/factorial(limit)
        limit -= 1

    return e

if __name__ == "__main__":
    try:
        number_of_dp = int(input("Enter the number of decimal places: "))        
        print(f"{eulersNumber(200):.{number_of_dp}f}")
    except KeyboardInterrupt:
        exit()