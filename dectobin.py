def dec_to_bin(num):
    answer = []

    while num > 0:
        remainder = num % 2
        answer = [remainder] + answer
        num = int(num / 2) # converted to int because by default, it is float
    return int("".join(map(str, answer))) # 1st converted list of int to list of strings and joins it into single string
