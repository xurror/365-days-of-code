def isHappyNumber(number):   
    sum = 0 
    if number == '1':
        return True
    else:
        number = list(number)
        for i in range(len(number)):
            sum += int(number[i])**2

        return isHappyNumber(str(sum))
    

if __name__ == "__main__":
    try:
        number = input("Enter a number: ")
        try:
            if isHappyNumber(number):
                print(f"{number} is a Happy Number")

        except RecursionError:
            print(f"{number} is not a Happy Number")

    except KeyboardInterrupt:
        exit()