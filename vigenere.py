"""
The main function first creates the vigenere square by assigning the value vig_square to the function create_vig_square().
The user is then asked to enter a message then a key to use for encryption and decryption.
The message and key are then changed to lower case using lower() method.
The message, key, and vig square are sent to the function encrypt and assigned to the value coded_message.
Then the coded_message, key, and vig square are sent to the function decrypt and assigned to the value decoded_message.
The encoded and decoded messages are then displayed.
"""
def main():
    vig_square = create_vig_square()
    message = input("Enter a multi-word message with punctuation: ")
    input_key = input("Enter a single word key with no punctuation: ")
    msg = message.lower()
    key = input_key.lower()
    coded_msg = encrypt(msg, key, vig_square)
    decoded_msg = decrypt(coded_msg, key, vig_square)
    print("The encoded message is: ",coded_msg)
    print("The decoded message is: ", decoded_msg)

"""
Creates a blank string for the encoded message. This uses the functions get_row_index for a letter in the key
and get_col_index for a letter in the message to find the row and column index in the vigenere square. 
The encrypted letters are then added to the blank string and returned. 
"""
def encrypt(msg, key, vig_square):
    coded_msg = ""
    key_inc = 0
    for i in range(len(msg)):
        msg_char = msg[i]
        if key_inc == len(key):
            key_inc = 0
        key_char = key[key_inc]
        if msg_char.isalpha():
            row_index = get_row_index(key_char,vig_square)
            col_index = get_col_index(msg_char,vig_square)
            coded_msg = coded_msg+vig_square[row_index][col_index]
            key_inc = key_inc+1 
        else:
            coded_msg = coded_msg + msg_char
    return coded_msg

"""
Creates a blank string for the decoded message. This function takes the coded message and key and uses the
get_plain_text_char function to search the vigenere square the decrypted characters and adds them to the string
decoded_msg and returns it.
"""
def decrypt(coded_msg, key, vig_square):
    decoded_msg = ""
    key_inc = 0
    for i in range(len(coded_msg)):
        coded_char = coded_msg[i]
        if key_inc == len(key):
            key_inc = 0
        key_char = key[key_inc]
        if coded_char.isalpha():
            plain_text = get_plain_text_char(coded_char,key_char,vig_square)
            decoded_msg = decoded_msg + plain_text
            key_inc = key_inc + 1
        else:
            decoded_msg = decoded_msg + coded_char
    return decoded_msg

"""
Grabs the column/message index from the vigenere square and returns it.
"""
def get_col_index(msg_char, vig_square):
    column_index = ord(msg_char) - 97
    return column_index
"""
Grabs the row/key index from the vigenere square and returns it."""
def get_row_index(key_char, vig_square):
    row_index = ord(key_char) - 97
    return row_index

"""
Creates the vig_square nested list. This function uses Python's built in methods ord which converts a letter to ASCII
and chr which converts ASCII to a letter.
A list assigned to value vig_square. 
Rows are created using a for loop with the value with a range of 26. In this for loop, another list is created assigned to the value
next_row and the value chr_code is created to hold ASCII values which is added to the row number.
The inner for loop contains the logic that structures the columns. This also has a range of 26, and each letter is
appended onto the next row. The if statement handles the wrap back from 'z' to 'a'. 
"""
def create_vig_square():
    vig_square = list()
    for row in range(26):
        next_row = list()
        chr_code = ord('a') + row
        for col in range(26):
            letter = chr(chr_code)
            next_row.append(letter)
            chr_code = chr_code + 1
            if chr_code > 122:
                chr_code = ord('a')
        vig_square.append(next_row)
    return vig_square

"""
This functions uses the row index for the key and runs throught the columns in the vigenere square to find the matching
column for the coded character, and changes it to the regular characters for the message. The regular characters are
added to the string plain_text_char and returned.
"""
def get_plain_text_char(coded_char, key_char, vig_square):
        row_index = get_row_index(key_char, vig_square)
        col_index = 0
        row = 0
        for col in range(26):
            if vig_square[row_index][col] == coded_char:
                col_index = col
        plain_text_char = vig_square[row][col_index]
        return plain_text_char

main()
