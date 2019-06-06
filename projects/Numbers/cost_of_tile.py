if __name__ == '__main__':
    try:
        cost = eval(input("Enter the cost of tiles: "))
        width = eval(input("Enter the width: "))
        length = eval(input("Enter the length: "))

        area  = width * length
        print(f"{cost*area}frs")

    except KeyboardInterrupt:
        exit()