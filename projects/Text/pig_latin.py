from random import randint

def generate():
    
    rand = randint(0,2)

    if rand == 0:

        return 'yay'

    elif rand == 1:

        return "way"

    elif rand == 2:

        return 'ay'
### Consonant at the start of word
def case1(word):
    
    suffix = ''
    index = 0
    
    for i in word:

        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':

            break
        
        else:

            suffix += i
            index += 1

    return word[index:]+suffix+'ay'

### word beings with a vowel
# TYPE 1
def case2(word):

    return word+generate()

# TYPE 2
def case3(word):

    suffix = ''
    index = 0
    
    for i in word:

        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':

            suffix += i
            index += 1
        
        else:

            break
    
    suffix += word[index]

    return word[index+1:]+suffix+'ay'

if __name__ == "__main__":

    string = input("> ")

    string_arr = string.split(' ')
    
    for i in range(len(string_arr)):

        if (string_arr[i][0]=='a' or string_arr[i][0]=='e'
            or string_arr[i][0]=='i' or string_arr[i][0]=='o'
            or string_arr[i][0]=='u'):
            
            string_arr[i] = case3(string_arr[i])

        else:
            
            string_arr[i] = case1(string_arr[i])

    new_string = ' '.join(string_arr)
    print(new_string)
