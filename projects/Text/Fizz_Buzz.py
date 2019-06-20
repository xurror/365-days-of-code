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
