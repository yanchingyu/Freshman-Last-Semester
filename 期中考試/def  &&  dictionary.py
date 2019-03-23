import string

def counter(input_string):
    alphabet=string.ascii_letters

    count_letters={}
    
    for letter in input_string:
        if letter in alphabet:        
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1

    return count_letters

address_count=counter(input())

print(address_count)
