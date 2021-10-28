def cipher_encrypt(plain_text, key):

    encrypted = ""

    for i in plain_text:

        #check if it's an uppercase character
        if i.isupper():

            i_index = ord(i) - ord('A')

            # shift the current character by key positions
            i_shifted = (i_index + key) % 26 + ord('A')

            i_new = chr(i_shifted)

            encrypted += i_new

        #check if its a lowercase character
        elif i.islower():

            # subtract the unicode of 'a' to get index in [0-25) range
            i_index = ord(i) - ord('a')

            i_shifted = (i_index + key) % 26 + ord('a')

            i_new = chr(i_shifted)

            encrypted += i_new

        elif i.isdigit():

            # if it's a number,shift its actual value
            i_new = (int(i) + key) % 10

            encrypted += str(i_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += i

    return encrypted

#driver code
if __name__ == '__main__':
    plain_text = input("Plain Text: ") # Take input of text to be shifted

    shift = input("Shift: ")

    converted_shift = int(shift) # Convert from string to int

    ciphertext = cipher_encrypt(plain_text, converted_shift) # Call function

    print("Cipher: ", ciphertext)
