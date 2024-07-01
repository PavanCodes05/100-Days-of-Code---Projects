# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'H', 'I', 'j', 'K', 'L','M', 'n', 'O', 'p', 'q', 'R', 's','T', 'u', 'V', 'W', 'x', 'y', 'z']

symbols = ["!", '@', '#', '$', '%', '^', '&', '*', '(', ')']

numbers = str(range(1,11))

print("Welcome to the password generator!")

no_of_letters = int(input("How many number of letters you need in password? "))
no_of_symbols = int(input("How many number of symbols youn need in password?:"))
no_of_numbers = int(input("How many number of numbers you need in password?: "))


letter = ''
symbol = ''
number = ''

for i in range(no_of_letters + 1):
    letter += letters[random.randint(0, len(letters) - 1)]

for i in range(no_of_symbols + 1):
    symbol += symbols[random.randint(0, len(symbols) - 1)]

for i in range(no_of_numbers + 1):
    number += numbers[random.randint(0, len(numbers) - 1)]
    
print("Your Password:", letter + symbol + number)
