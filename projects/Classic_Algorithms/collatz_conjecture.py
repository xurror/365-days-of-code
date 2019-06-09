"""
Collatz Conjecture:
 Start with a number n > 1.
 Find the number of steps it takes to reach one using the following process:
 If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
 """

def numberOfSteps(n, count=0):
    if n == 1:
        return count
    else:
        if n%2 == 0:
            count += 1
            return numberOfSteps(n/2, count)
        else:
            count += 1
            return numberOfSteps((n*3) + 1, count)

if __name__ == "__main__":
    n = int(input("> "))
    print(numberOfSteps(n))