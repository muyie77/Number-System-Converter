def dec_to_hex(num):
    hex_val = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    answer = []

    while num > 0:
        modulu = num % 16
        remainder = modulu
        answer = [hex_val[remainder]] + answer
        num = int(num / 16)
    return "".join(answer)
