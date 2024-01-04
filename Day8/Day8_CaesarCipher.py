alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from Day8_cipher_art import logo

# Debugging strings below
# texts = 'dogs are cute'
# shifts = 12
# i_texts = 'pase mdq ogfq'
# i_shifts = 12

def caesarv1(text, shift, direction):
    shifted_list = []
    if shift > 26:
        shift = shift % 26
    for letter in text:
        if letter not in alphabet:
            shifted_list.append(letter)
        else:
            current = alphabet.index(letter)
            if direction == 'encode':
                if current + shift >= 26:
                    temp_shift = shift - 26
                    shifted_list.append(alphabet[current + temp_shift])
                else:
                    shifted_list.append(alphabet[current + shift])
            elif direction == 'decode':
                current = alphabet.index(letter)
                if current + shift >= 26:
                    temp_shift = shift + 26
                    shifted_list.append(alphabet[current - temp_shift])
                else:
                    shifted_list.append(alphabet[current - shift])
    print("Your message is: ", *shifted_list, sep='')


def caesarv2(text, shift, direction):  # Alternative option using strings instead of lists for storage
    shifted_text = ""
    if shift > 26:
        shift = shift % 26
    if direction == 'decode':  # cut entire elif out by using *= -1 for decode
        shift *= -1  # can reuse the same code for both operations by using this method
    for letter in text:
        if letter not in alphabet:
            shifted_text += letter
        else:
            current = alphabet.index(letter)
            if current + shift >= 26:  # Adjust the shift if the sum is greater than 26
                temp_shift = shift - 26
                shifted_text += alphabet[current + temp_shift]
            else:
                shifted_text += alphabet[current + shift]
    print(f"Here's the {direction}d result: {shifted_text}")


while True:  # added while loop to continue program if desired
    cipher = input("Would you like to use the cipher program? Type y to begin or n to quit.\n").lower()
    if cipher == "y":
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("What is the message?\n").lower()
        shift = int(input("Type the shift number\n"))
        caesarv2(text,shift,direction)
    elif cipher == "n":
        print("Goodbye")
        break
    else:  # error handling for invalid values of cipher start
        print("please enter a valid value.")