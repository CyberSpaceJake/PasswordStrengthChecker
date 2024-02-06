import string

def strength_check(password):
    #Starting Value
    score = 0

    #checking against common passwords
    with open('commonpasswords.txt', 'r') as f:
        common = f.read().splitlines()
    
    if password in common:
        print("That password was found in a common list. As such, it is not secure!")
        exit()
    
    #checking characters
    uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
    digits = any([1 if c in string.digits else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])

    characters = [uppercase, lowercase, digits, special]
    
    #Check password length
    length = len(password)
    if length > 7:
        score += 1
    if length > 11:
        score += 1
    if length > 14:
        score += 1

    #scoring character types
    if sum(characters) > 1:
        score += 1
    if sum(characters) > 2:
        score += 1
    if sum(characters) > 3:
        score += 1

    return score

#accept user input
password = input("Password to Test: ")

#call strength_check function
score = strength_check(password)

#results
if score < 4:
    print("This password is weak, please add more length and character types.")
elif score < 5:
    print("This password is average, consider adding additional character types and length")
elif score < 6:
    print("This password is strong! But can it be better?")
elif score == 6:
    print("Showoff, this password is very strong!")