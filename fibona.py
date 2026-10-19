n = int(input("n = "))
if n <= 0:
    print("Моля, въведете число по-голямо от 0.")
else:
    i = 0
    fib = []
    while i < n:
        if i == 0 or i == 1:
            fib.append(1)
        else:
            next_val = fib[i-1] + fib[i-2]
            fib.append(next_val)
        i += 1
    out = ""
    i = 0
    while i < len(fib):
        out += str(fib[i])
        if i < len(fib) - 1:
            out += ", "
        i += 1
    print(out)