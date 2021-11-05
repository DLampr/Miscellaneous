
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_new = alphabet*2 #We provide the alphabet two times for debugging reasons (when we want to encrypt the last letters of the alphabet)

def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "de":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet_new:
            position = alphabet_new.index(char)
            new_position = position + shift_amount   
            end_text += alphabet_new[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}coded text is {end_text}")
    
should_continue = True
while should_continue:
    direction = input("Type 'en' to encrypt, type 'de' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
        
    shift = shift % 26
    
    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")