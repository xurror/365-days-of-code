from math import pow

def decimal_to_binary():
    decimal = int(input("Decimal Number: "))
    binary = '\0'

    while (decimal+1 // 2) != 0:
        binary = str(decimal%2) + binary        
        decimal = decimal // 2

    binary = binary[0:len(binary)]
    print(binary[:-1])

def binary_to_decimal():
    decimal, i = 0, 0
    binary = input("Binary Number: ")
    list(binary)

    for digit in binary:
        if digit != 1 or digit != 0:
            print("The number is not a binary number")
            print("Please enter a binary number")
            return 0

    if int(binary[len(binary) - 1]) == 0:
        while i < (len(binary)-1):
            digit = int(binary[i])*2
            power = (len(binary)-1)-i
            
            decimal += pow(digit, power)
            print("digit", binary[i], "power", power)            
            i += 1
    
    else:
        while i < len(binary):
            digit = int(binary[i])*2
            power = (len(binary)-1)-i
            
            decimal += pow(digit, power)
            print("digit", binary[i], "power", power)            
            i += 1

    print(decimal)

if __name__ == '__main__':
    try:
        while True:
            try:
                choice = input("Enter (b)inary conversion or (d)ecimal converion: ")        

                if choice == 'b' or choice == 'B':
                    decimal_to_binary()
                elif choice == 'd' or choice == 'D':
                    binary_to_decimal()
                else:
                    raise ValueError
                
            except ValueError:
                print("Wrong input\nPlease try again")

    except KeyboardInterrupt:
        exit()