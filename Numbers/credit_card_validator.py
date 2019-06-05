class Card(object):
    def __init__(self, code=None):        
        self.code = code        
        

    def issuer(self):
        print("BIN\t\t", end="")
        for i in range(len(self.code[:5])):
            print(f"{int(self.code[i])}", end="")
        print("\nAccount Number\t", end="")

        for i in range(len(self.code[6:14])):
            print(f"{int(self.code[i])}", end="")

        print(f"\nChecksum \t{self.code[-1]}")

        print("\n\t DETAILS")
        print("---------------------------")
        if int(self.code[0]) == 1 or int(self.code[0]) == 2:
            print("Issuing:\tAirlines")
        elif int(self.code[0]) == 3:
            print("Issuing:\tBank")
        elif int(self.code[0]) == 4:
            print("Issuing:\tVISA")
        elif int(self.code[0]) == 5:
            print("Issuing:\tMasterCard")
        elif int(self.code[0]) == 6:
            print("Issuing:\tMerchandising and Banking")
        elif int(self.code[0]) == 7:
            print("Issuing:\tPetroleum Companies")
        elif int(self.code[0]) == 8:
            print("Issuing:\tTelecommunications Companies")
        elif int(self.code[0]) == 9:
            print("Issuing:\tNational Assignment")


    def company():
        pass

    def validate(self):
        i = len(self.code) - 2
        final_sum_of_digits = []
        while i >= 0:            
            doubled_digits = 2*int(self.code[i])
            sum_of_digits = 0
            
            if 2*int(self.code[i]) > 9:                
                doubled_digits = list(str(doubled_digits))
                print("doubled digits", doubled_digits)
                sum_of_digits = int(doubled_digits[0]) + int(doubled_digits[1])
                self.code[i] = str(sum_of_digits)
                final_sum_of_digits.append(sum_of_digits)

            else:
                self.code[i] = str(doubled_digits + sum_of_digits)

            """if sum_of_digits == int(self.code[-1]):
                print("Sum of digits", sum_of_digits)                
                break
            else:
                print("Invalid Code! 1")
                return False"""
            print(self.code[i])
            i -= 2

        i, sum = 0, 0
        for i in range(len(self.code)-1):
            sum += int(self.code[i])
            print("Sum", sum)

        try:
            sum += final_sum_of_digits[0]
            print("final sum", sum)
        except IndexError:
            sum += 0
            print("final sum", sum)

        if sum % 10 == 0:
            print("Valid Code")
            return True
        else:
            print("Invalid Code! 2")
            return False


if __name__ == "__main__":
    try:
        code = int(input("Enter code\n> "))
        code = list(str(code))

        MyCard = Card(code)
        #MyCard.issuer()
        if MyCard.validate():
            MyCard.issuer()

    except KeyboardInterrupt:
        exit()