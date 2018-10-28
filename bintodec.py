def bin_to_dec(num):
    given = list(map(int, num)) # map means converting strings to int
    multiples = []

    for i in range(len(given)):
        a = 2**i
        multiples = [a] + multiples # appending to the left

    temp_ans = []
    for i, j in zip(multiples, given): # ZIP - accessing 2 lists in one loop
        multiply = i * j
        temp_ans.append(multiply)

    return sum(temp_ans)
