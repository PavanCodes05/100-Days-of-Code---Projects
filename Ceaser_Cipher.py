print('CEASER CIPHER')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("What do you want to do?, ENCODE OR DECODE")
user = input("Type encode or decode: ").lower()
shift = int(input("Enter the shift number: "))

shift = shift % 26


def encode(word, shift):
    encoded_word = ""
    for letter in word:
        if letter in alphabet:
            place = alphabet.index(letter)
            pos = place + shift
            encoded_word += alphabet[pos]
        else:
            encoded_word += letter
    print(encoded_word)    
    

if user == "encode":
    word = input('Enter the word to encode: ').lower()
    encode(word, shift)
elif user == 'decode':
    word = input("Enter the word to decode: ").lower()
    encode(word, shift * -1)