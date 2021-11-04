def int_to_a1(num, alphabet):
    base = len(alphabet)
    result = ""
    while num:
        exponent = 0
        while True:
            divisor = base ** exponent
            int_quotient = num // divisor
            if int_quotient and num - divisor * 26 > 0:
                exponent += 1
            else:
                break
        result += alphabet[int_quotient - 1]
        num -= int_quotient * divisor
    return result
