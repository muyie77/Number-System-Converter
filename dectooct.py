def dec_to_oct(num):
    answer = []

    while num > 0:
        remainder = num % 8
        answer = [remainder] + answer
        num = int(num / 8)
    return int("".join(map(str, answer)))
