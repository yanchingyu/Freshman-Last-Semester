import string

alphabet=string.ascii_letters


address="idiot"

count_letters={}
   
for letter in address:
    if letter in alphabet:        
        if letter in count_letters:
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1

print(count_letters)
