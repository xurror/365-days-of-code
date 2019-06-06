from math import pow

class Mortgage(object):
    def __init__(self, principal, rate, term):
        self.__principal = principal
        self.__rate = rate/100
        self.__term = term

    def calculate(self):
        # Get mode of calculation
        
        try:
            method = str(input("Enter (y)early, (m)onthly, (w)eekly or (d)aily mortgage computing: "))

            if method == 'y' or method == 'yearly':
                self.__term = self.__term
                
            elif method == 'm' or method == 'monthly':
                self.__term = self.__term * 12                    

            elif method == 'w' or method == 'weekly':
                self.__term = self.__term * 54

            elif method == 'd' or method == 'daily':
                self.__term = self.__term * 365

            else:
                raise ValueError        
        except ValueError:
            print("Wrong Input!")
            calculate(self)

        return ((self.__principal*self.__rate) * 
            (pow(1+self.__rate, self.__term))
            / (pow(1 + self.__rate, self.__term) - 1))
        
        

if __name__ == '__main__':
    try:
        principal = eval(input("Loan Amount: "))
        rate = eval(input("Interest Rate: "))
        term = eval(input("Term(in years): "))

        myMortgage = Mortgage(principal, rate, term)
        print(f"{myMortgage.calculate():.2f}")

    except KeyboardInterrupt:
        exit()