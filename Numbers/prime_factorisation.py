from math import sqrt

# Check if n is a prime number
def prime(n):
    isPrime = True        

    divisor = 2
    while divisor <= n/2:
        if n % divisor == 0:
            isPrime = False
            break
        divisor += 1        
    return isPrime
            
if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        
        print("Factors")

        i = 2
        while i <= n:        
            if prime(i):
                if n % i == 0:
                    print(f"{i:3}")
            i += 1
    except KeyboardInterrupt:
        exit()