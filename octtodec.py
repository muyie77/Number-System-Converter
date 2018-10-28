def oct_to_dec(num):
    given = list(map(int, num))
    multiples = []

    for i in range(len(given)):
        a = 8**i
        multiples = [a] + multiples

    temp_ans = []
    for i, j in zip(multiples, given):
        multiply = i * j
        temp_ans.append(multiply)

    return sum(temp_ans)
