import struct
# === CS 115 Lab 7 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 7 ===
def lagrassian_cipher_word(words,k):
    """encrypts and returns a single word in lagrassian cipher"""
    memo = {}
    def _lagrassian_cipher_word(words,k):
        if len(words) == 0:
            return ""
        if (words,k) in memo:
            return memo[(words,k)]
        if ord(words[0]) % 2 == 0:
            new_letter = ord(words[0]) + k
            memo[(words, k)] = chr(new_letter) + _lagrassian_cipher_word(words[1:],k)
            return chr(new_letter) + _lagrassian_cipher_word(words[1:], k)
        else:
            new_letter = ord(words[0]) - k
            memo[(words, k)] = chr(new_letter) + _lagrassian_cipher_word(words[1:],k)
            return chr(new_letter) + _lagrassian_cipher_word(words[1:],k)
    return _lagrassian_cipher_word(words,k)

def lagrassian_cipher(words, k):
    """encrypts and returns a message in the form of a tuple in lagrassian cipher"""
    memo = {}
    def _lagrassian_cipher(words, k):
        if len(words) == 0:
            return ()
        if (words, k) in memo:
            return memo[(words, k)]
        if len(words) == 1:
            memo[(words, k)] = tuple([lagrassian_cipher_word(words[0],k)])
            return tuple([lagrassian_cipher_word(words[0],k)])
        memo[(words,k)] = tuple([lagrassian_cipher_word(words[0],k)]) + _lagrassian_cipher(words[1:],k)
        return tuple([lagrassian_cipher_word(words[0],k)]) + _lagrassian_cipher(words[1:],k)
    return _lagrassian_cipher(words,k)
            



### Helper functions (do not edit)
def print_bytes_as_bits(bytes):
    """Given Python bytes data, prints them as bits
    grouped by bytes"""
    bits_as_string = ' '.join(f'{b:08b}' for b in bytes)
    print(bits_as_string)


def pack_data(data, byte_order, number_format):
    """
    Packs the data in data as a number_format (ex. int)
    the order of bytes is specified by the variable byte_order.

    Valid number_formats include int, unsigned int, float, double
    """
    byte_order_to_byte_order_char = {"native": "@", "little endian": "<", "big endian": ">", "network": "!"}
    c_type_to_format = {"char": "c", "bool": "?", "short": "h", "int": "i", "unsigned int": "I", "long": "l",
                        "float": "f", "double": "d"}
    if byte_order not in byte_order_to_byte_order_char:
        raise ValueError(f"{byte_order} not in list of supported byte orders: {byte_order_to_byte_order_char.keys()}")
    if number_format not in c_type_to_format:
        raise ValueError(f"{number_format} not in list of supported number formats: {c_type_to_format.keys()}")
    format_string = byte_order_to_byte_order_char[byte_order] + c_type_to_format[number_format]
    return struct.pack(format_string, data)

if __name__ == '__main__':
    pass
    # your testing code should stay indented in this block
    # if you run lab7.py, this code will run
    # but it won't run if we import your functions
    #
    # for example, if you uncomment the code below, it will print the bits in the float representation of 0.25
    my_number = 10
    print_bytes_as_bits(pack_data(my_number, 'network', 'int'))
    print(pack_data(-15, 'network', 'int'))
    data_in_bytes = pack_data(0.25, "network", "double")
    print_bytes_as_bits(data_in_bytes)
