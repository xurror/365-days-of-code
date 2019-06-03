def prime(n):
    isPrime = True        

    divisor = 2
    while divisor <= n/2:
        if n % divisor == 0:
            isPrime = False
            break
        divisor += 1        
    return isPrime

def printPrime():
    printing = True
    global prime_number
    while printing:
        if prime(prime_number):
            print(prime_number, end="\n")
            break
        else:
            prime_number += 1

if __name__ == '__main__': 
    try:       
        print("2", end="\n")
        prime_number = 3
        while True:
            question = str(input("Do you wish to continue?\n> "))
            if question == 'yes' or question == 'Yes' or question == 'YES':
                printPrime()
                prime_number += 1
            elif question == 'no' or question == 'No' or question == 'NO':
                exit()
            else:
                print("wrong input")

    except KeyboardInterrupt:
        exit()