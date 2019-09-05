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

def get_col_index(msg_char, vig_square):
    column_index = ord(msg_char) - 97
    return column_index

def get_row_index(key_char, vig_square):
    row_index = ord(key_char) - 97
    return row_index

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