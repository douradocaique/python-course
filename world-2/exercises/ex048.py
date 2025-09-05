s = 0.0
for n in range(1,500):
    if n %2 != 0 and n % 3 == 0:
        s += n
print(f'Result of the sum: {s}')
