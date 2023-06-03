fib_sequence = [0, 1]

i = 2
while i < 10:
    fib_num = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(fib_num)
    i += 1

for num in fib_sequence:
    print(num)