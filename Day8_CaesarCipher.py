alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Debugging strings below
# texts = 'dogs are cute'
# shifts = 12
# i_texts = 'pase mdq ogfq'
# i_shifts = 12

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    shifted_list = []
    for letter in text:
        if letter == " ":
            shifted_list.append(letter)
        else:
            current = alphabet.index(letter)
            if current + shift >= 26:
                temp_shift = shift - 26
                shifted_list.append(alphabet[current + temp_shift])
            else:
                shifted_list.append(alphabet[current + shift])
    print(*shifted_list, sep='')

def decrypt(text, shift):
    shifted_list = []
    for letter in text:
        if letter == " ":
            shifted_list.append(letter)
        else:
            current = alphabet.index(letter)
            if current + shift >= 26:
                temp_shift = shift + 26
                shifted_list.append(alphabet[current - temp_shift])
            else:
                shifted_list.append(alphabet[current - shift])
    print(*shifted_list, sep='')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == 'encode':
    texts = input("Type your message:\n").lower()
    shifts = int(input("Type the shift number:\n"))
    encrypt(texts, shifts)
elif direction == 'decode':
    d_texts = input("Type your message:\n").lower()
    d_shifts = int(input("Type the shift number:\n"))
    decrypt(d_texts, d_shifts)