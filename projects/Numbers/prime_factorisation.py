from math import sqrt

# Check if n is a prime number
# Method 1
def prime1(n):
    isPrime = True        

    divisor = 2
    while divisor <= n/2:
        if n % divisor == 0:
            isPrime = False
            break
        divisor += 1        
    return isPrime

# Check if n is a prime number
# Method 1
def prime2(n):
    isPrime = True
    if n<=1:
        return False
    else:
        try:
            for i in range(round(sqrt(n))):
                if n%i == 0:
                    return False
                else: 
                    isPrime = True
        except ZeroDivisionError:
            i = 1
    
    return isPrime
            
if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        
        print("Factors")

        i = 2
        while i <= n:        
            if prime1(i):
                if n % i == 0:
                    print(f"{i:3}")
            i += 1
    except KeyboardInterrupt:
        exit()