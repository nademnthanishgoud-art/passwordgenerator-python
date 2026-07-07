import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")

n_letters = int(input("How many letters? "))
n_symbols = int(input("How many symbols? "))
n_numbers = int(input("How many numbers? "))

password_list = []

for i in range(n_letters):
    password_list.append(random.choice(letters))

for i in range(n_symbols):
    password_list.append(random.choice(symbols))

for i in range(n_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)

print("Your password is:", password)