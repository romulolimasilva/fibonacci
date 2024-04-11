def fibonacci(n):
    fib_sequence = [10, 5]  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, inicia a sequencia com os dois primeiros valores da sequência.

    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

n = 10  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
print(fibonacci(n))
