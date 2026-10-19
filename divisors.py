n = int(input("n = "))
i = 1
out = ""
first = True  
while i <= n:
    if n % i == 0 and i % 2 != 0:
        if not first:
            out += ", "
        out += str(i)
        first = False
    i += 1
print(f"{n} -> {out}")