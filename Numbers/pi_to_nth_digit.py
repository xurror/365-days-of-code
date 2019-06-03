if __name__ == "__main__":
    try:
        num_of_dp = int(input("Enter the number of decimal places: "))

        print(f"{22/7:.{num_of_dp}F}")

    except KeyboardInterrupt:
        exit()