# Random Strong Password Generator
<p>Jennifer Kaiser 2023 
<p>
<a href="http://www.jenniferkaiser.tech">www.jenniferkaiser.tech</a>
<p>
<a href="http://www.linkedin.com/in/jenniferkaiser-tech">www.linkedin.com/in/jenniferkaiser-tech</a>
<p>
<a href="http://www.github.com/jenniferkaiser21">www.github.com/jenniferkaiser21</a>

# Demo of Working Code
<a href="https://youtu.be/0kX3fHsm6Zc">https://youtu.be/0kX3fHsm6Zc</a>


# Languages Used:
* Python (Version 3.9.12)

# Packages/Libraries Used:
* random 

# IDE Used:
* VSCode

# Version Control:
* Git

# Summary of Project:
https://github.com/jenniferKaiser21/Random-Password-Generator

This project generates strong passwords based on user parameters input currently through the terminal. It uses the random library to randomly assign user-requested characters, such as lower case English alphabet characters, upper case English alphabet characters, digits (0-9), and special characters (!, @, #, $, %, ^, &, *, (, ), -, _, +, =, {, }, [, ], |, :, ;, ., ?, /, etc).
<img src="https://github.com/jenniferKaiser21/Random-Password-Generator/blob/9c9e0afe36dece380b4bb25ad5a8d9afffe383c9/images/generator_1.png">

Once running, the program asks for the number of passwords the user wishes to generate. This number is checked in a try/except block to ensure it is a non-negative number greater than 0. 

Next, the program asks the user for the desired password length. It suggests that at least 12 characters is recommended for a strong password. Again, this number is checked in a try/except block to ensure it is non-negative, and greater than 0.
<img src="https://github.com/jenniferKaiser21/Random-Password-Generator/blob/9c9e0afe36dece380b4bb25ad5a8d9afffe383c9/images/generator_2.png">

Lastly, the program asks the user how many characters they wish to be from the English alphabet (non-numeric and special characters). In a try/except block, it checks to ensure that the value is less than or equal to the user desired length of the password, and that the value is greater than 0.
<img src="https://github.com/jenniferKaiser21/Random-Password-Generator/blob/9c9e0afe36dece380b4bb25ad5a8d9afffe383c9/images/generator_3.png">

Using random.randint, the program then goes through a series of loops to randomly generate the appropriate number of characters in each of the four categories (lower case alpha, upper case alpha, digit, and symbol), appends them to a temporary list, and shuffles the list before adding a resulting generated password (as a string) to a result list.

The program completes by printing the list of generated passwords, with a self-incrementing password number pre-pending the password.
<img src="https://github.com/jenniferKaiser21/Random-Password-Generator/blob/9c9e0afe36dece380b4bb25ad5a8d9afffe383c9/images/generator_4.png">

# Additional Notes:
In the future, I would like to expand this project into a working website, with the use of either Flask or Django. I would also like to add additional features, such as a toggle for turning on and off special characters in the resulting generated passwords.
