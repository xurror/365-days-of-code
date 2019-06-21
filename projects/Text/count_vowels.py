
def count_vowel(string):

    count = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for word in string:

        for i in word:
            
            if i in vowels:

                count += 1            
    
    return count


if __name__ == "__main__":

    try:        
        string =  input("> ")    
        print(f"There are {count_vowel(string)} vowels.")

    except KeyboardInterrupt:
        exit(0)