""" 4, 5, 9, 2, 6, 1, 8, 3, 7 """
def bubbleSort(string):
    
    my_list = string.split(', ')
    my_list = [int(my_list[i]) for i in range(len(my_list))]
    
    while my_list[0] != min(my_list):
        for i in range(len(my_list) - 1):
            if int(my_list[i+1]) < int(my_list[i]):
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp
        
    return my_list


if __name__ == "__main__":
    string = input("List: ")
    print(bubbleSort(string))