
def modulus_10_weight_3(code):
    code_string = str(code)
    a = 0
    b = 0

    for i in range(0, len(code_string), 2):
        a += int(code_string[i])

    for i in range(1, len(code_string), 2):
        b += int(code_string[i])

    d = (a + (b * 3)) % 10
    if d == 0:
        return 0
    d = 10 - d
    return d
