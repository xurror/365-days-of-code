from random import randint

if __name__ == "__main__":
    head, tail = 0, 0
    while True:
        try:
            user = input("(t)oss, (c)ounts, (r)eset, (q)uit\n> ")
            if user == 't' or user == 'toss':
                if randint(0,1) == 0:
                    print("\tHEAD")
                    head += 1
                elif randint(0,1) == 1:
                    print("\tTAIL")
                    tail += 1
            elif user == 'c' or user == 'counts':
                print(f"\tHEADS = {head}\n\tTAILS = {tail}")
            elif user == 'r' or user == 'reset':
                head, tail = 0, 0
            elif user == 'q' or user == 'quit':
                exit()
            else:
                print("Wrong Input!")

        except KeyboardInterrupt:
            exit()