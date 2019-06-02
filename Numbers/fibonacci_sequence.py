from math import pow,sqrt

class Fibonacci(object):
    def __init__(self,n):
        self.__n = n

    def binetsFormula(self):
        x = (1 + sqrt(5))/2
        y = (1 - sqrt(5))/2
        numerator = pow(x, self.__n) - pow(y, self.__n)
        denominator = x - y
        return numerator / denominator

    def fibonacciSequence(self):        
        numerator = pow((1 + sqrt(5)),self.__n) - pow((1 - sqrt(5)),self.__n)
        denominator = pow(3,self.__n)*sqrt(5)
        self.__n -= self.__n
        return numerator/denominator

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    term = 2

    print("Term \t Sequence")
    print(f"{0:2}{0:10}\n{1:2}{1:10}")
    
    while term <= number:
        fibonacci_1 = Fibonacci(term - 1)
        fibonacci_2 = Fibonacci(term - 2)
        print(f"{term:2}{round(fibonacci_2.binetsFormula() + fibonacci_1.binetsFormula()):10}")
        term += 1