"""
This program is a strong password generator with customizations for password length and the inclusion of the following:
Lowercase Characters: e.g. abcdef
Uppercase Characters: e.g. ABCDEF
Digits: e.g. 123456
Special Characters: e.g. !, @, #, $, %, ^, &, *, (, ), -, _, +, =, {, }, [, ], |, :, ;, <, >, ,, ., ?, /
"""

import random
lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = "!@#$%^&*()_-+=[]}{|;:',.<>/?"
d = {1: lowercase_characters, 2: uppercase_characters, 3: digits, 4: symbols}
generated_password = ""
password_list = []
result = []

"""
test print statements
"""
# print(lowercase_characters)
# print(uppercase_characters)
# print(symbols)
# print(d)

print("""
 _        _______ _________ _______  _______  _______                            
| \    /\(  ___  )\__   __/(  ____ \(  ____ \(  ____ )                           
|  \  / /| (   ) |   ) (   | (    \/| (    \/| (    )|                           
|  (_/ / | (___) |   | |   | (_____ | (__    | (____)|                           
|   _ (  |  ___  |   | |   (_____  )|  __)   |     __)                           
|  ( \ \ | (   ) |   | |         ) || (      | (\ (                              
|  /  \ \| )   ( |___) (___/\____) || (____/\| ) \ \__                           
|_/    \/|/     \|\_______/\_______)(_______/|/   \__/                           
                                                                                 
 _______  _______  _______  _______           _______  _______  ______           
(  ____ )(  ___  )(  ____ \(  ____ \|\     /|(  ___  )(  ____ )(  __  \          
| (    )|| (   ) || (    \/| (    \/| )   ( || (   ) || (    )|| (  \  )         
| (____)|| (___) || (_____ | (_____ | | _ | || |   | || (____)|| |   ) |         
|  _____)|  ___  |(_____  )(_____  )| |( )| || |   | ||     __)| |   | |         
| (      | (   ) |      ) |      ) || || || || |   | || (\ (   | |   ) |         
| )      | )   ( |/\____) |/\____) || () () || (___) || ) \ \__| (__/  )         
|/       |/     \|\_______)\_______)(_______)(_______)|/   \__/(______/          
                                                                                 
 _______  _______  _        _______  _______  _______ _________ _______  _______ 
(  ____ \(  ____ \( (    /|(  ____ \(  ____ )(  ___  )\__   __/(  ___  )(  ____ )
| (    \/| (    \/|  \  ( || (    \/| (    )|| (   ) |   ) (   | (   ) || (    )|
| |      | (__    |   \ | || (__    | (____)|| (___) |   | |   | |   | || (____)|
| | ____ |  __)   | (\ \) ||  __)   |     __)|  ___  |   | |   | |   | ||     __)
| | \_  )| (      | | \   || (      | (\ (   | (   ) |   | |   | |   | || (\ (   
| (___) || (____/\| )  \  || (____/\| ) \ \__| )   ( |   | |   | (___) || ) \ \__
(_______)(_______/|/    )_)(_______/|/   \__/|/     \|   )_(   (_______)|/   \__/
                                                                                 
      """)

"""
num = number of passwords to be generated
n = number of total characters to be generated
l = number of minimum characters that are letters
sc = number of non-alpha characters left that can be special digits or symbols
"""

"""
while loop ensures that the number of passwords to be generated is greater than 0.
"""
while True:
    try:
        num = int(input("How many passwords would you like to generate today? "))
        if num > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")


"""
while loop ensures that the password length is greater than 0.
"""
while True:
    try:
        n = int(input(
            "What is the desired password length? (At least 12 characters is recommended.) "))
        if num > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

"""
while loop ensures that number of letters is less than or equal to the desired password length.
"""
while True:
    try:
        l = int(input("Number of desired letters (a-z)? "))
        if l <= n and l > 0:
            break
        else:
            print(f"Please enter a value less than or equal to {n}.")
    except ValueError:
        print("Please enter a valid number.")

sc = n - l
# print(n)
# print(l)
# print(sc)


# lowercase_characters
# uppercase_characters
# digits
# symbols

"""
use random.choice() to select a string element
append to list
use random.shuffle() to shuffle contents of list
use ''.join(list_name) set to a variable as the final result 

Use a random generator for either a 1 or a 2 to determine if the letter should be upper or lower case
Use a random generator for 3 or 4 to determine if the special character (sc) should be a digit or a symbol
"""

for i in range(num):
    generated_password = ""
    password_list = []
    # generating and appending random alpha characters to password_list
    for i in range(0, l):
        upper_or_lower = random.randint(1, 2)

        if upper_or_lower == 1:  # lowercase letter
            # generate random index for letter
            random_letter_index = random.randint(0, 25)
            #print("d[1][random_letter_index]", d[1][random_letter_index])
            password_list.append(str(d[1][random_letter_index]))

        elif upper_or_lower == 2:  # uppercase letter
            # generate random index for letter
            random_letter_index = random.randint(0, 25)
            #print("d[2][random_letter_index]", d[2][random_letter_index])
            password_list.append(str(d[2][random_letter_index]))

    for i in range(0, sc):
        digit_or_symbol = random.randint(3, 4)

        if digit_or_symbol == 3:  # digit
            # generate random digit (0-9)
            random_digit = random.randint(0, 9)
            #print("random digit", random_digit)
            password_list.append(str(random_digit))

        elif digit_or_symbol == 4:  # symbol
            # generate random index for symbol
            random_symbol_index = random.randint(0, 24)
            #print("d[4][random_symbol_index]", d[4][random_symbol_index])
            password_list.append(str(d[4][random_symbol_index]))

    # print(password_list)
    # Shuffle contents of password_list using random.shuffle
    random.shuffle(password_list)
    # print(password_list)
    # Convert list to string
    for i in password_list:
        generated_password += i
    # Return/print generated_password
    #print("GENERATED PASSWORD: ", generated_password)
    result.append(generated_password)


# Print final list of generated passwords
print("---LIST OF GENERATED PASSWORDS---")
for i in result:
    print(f"Password #{result.index(i)+1}:  {i}")
