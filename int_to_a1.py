from string import ascii_uppercase

def int_to_a1(num, alphabet):
    '''
    Converts column position integer
    to correponding A1 notation letter.
    Expects alphabet to be the ASCII 26
    lowercase or uppercase letters.
    1 indexed. 0 returns empty string.
    '''
    base = len(alphabet)
    result = ""
    while num:
        exponent = 0
        while True:
            divisor = base ** exponent
            int_quotient = num // divisor
            if int_quotient and num - divisor * base > 0:
                exponent += 1
            else:
                break
        result += alphabet[int_quotient - 1]
        num -= int_quotient * divisor
    return result


# EXAMPLE
# =======
# num_to_a1(3000, ascii_uppercase) => 'DKJ'
# num_to_a1(3000, ascii_uppercase) => 'DKJ'
# num_to_a1(3000, ascii_uppercase) => 'DKJ'
