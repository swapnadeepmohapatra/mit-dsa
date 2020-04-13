def power(b, p):
    if p == 1:
        return b
    else:
        return b * power(b, p-1)


print(power(2, 4))
