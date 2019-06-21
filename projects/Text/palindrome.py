
def isPalindrome(string):
    
    string_arr = string.split(' ')
    string = ''.join(string_arr)
    reversed_string = string[::-1]
    if string == reversed_string:
        
        return True
    
    else:

        return False

if __name__ == "__main__":
    
    try:
        string = input("> ")
        print(f'{isPalindrome(string)}')

    except KeyboardInterrupt:
        exit(0)
