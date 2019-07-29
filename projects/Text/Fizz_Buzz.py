def fizz(i):
    
    if i % 3 == 0:

        return True
    
    else:

        return False

def buzz(i):

    if i % 5 == 0:

        return True
    
    else:

        return False

def more_fizz_buzz(x, y, z):
    a, b, c = x, y, z

    for i in range(1,c+1):
        if i % a == 0 and i % b != 0:
            print("Fizz")
        elif i % b == 0 and i % a != 0:
            print("Buzz")
        elif i % b == 0 and i % a == 0:
            print("FizzBuzz")
        else:
            print(i)
    
if __name__ == "__main__":

    print("Number\tFizz-Buzz")
    
    for i in range(1, 101):

        if fizz(i) and buzz(i):
        
            print(f"  {i} \t FizzBuzz")

        else:

            if fizz(i):

                print(f"  {i} \t Fizz")

            elif buzz(i):

                print(f"  {i} \t Buzz")

            else:

                print(f"  {i} \t {i}")
