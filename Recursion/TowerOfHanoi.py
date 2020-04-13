def toh(n, from_bar, to_bar, aux_bar):
    if n == 1:
        print("Move 1 from", from_bar, "to", to_bar)
        return
    else:
        toh(n-1, from_bar, aux_bar, to_bar)
        print("Move 1 from", from_bar, "to", to_bar)
        toh(n-1, aux_bar, to_bar, from_bar)


toh(3, "A", "C", "B")
