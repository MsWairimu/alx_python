def fibonacci_sequence(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    fib_seq = [0, 1]

    while len(fib_seq) < n:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)

    return fib_seq

# Test the function
n = 10
result = fibonacci_sequence(n)
print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

