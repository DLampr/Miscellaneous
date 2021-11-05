"""Password Generator. Does what the title suggests.
   Takes 3 inputs: Number of desired letters, number of desired symbols and number of desired numbers.
   Then returns a random password based on these inputs."""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator(let,symb,numb):
    password = []
    for char in range(0, let):
        password.append(random.choice(letters))
    for char in range(0, symb):
        password.append(random.choice(symbols))
    for char in range(0, numb):
        password.append(random.choice(numbers))

    random.shuffle(password)

    password1 = ""
    for n in password:
        password1 += n

    return password1
    
def main():
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    print(password_generator(nr_letters,nr_symbols,nr_numbers))
    

if __name__ == "__main__":
    main()
