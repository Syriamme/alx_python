def fibonacci_sequence(n):
    if n == 1:
        return [0]
    elif n <= 0:
        return []
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            next = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next)
        return fib_seq