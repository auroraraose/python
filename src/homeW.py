def prblm(matrix):
    res = [num ** 2 for row in matrix for num in row if num % 2 == 0]
    return res

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

def prblmW(word_list):
    res = [word.upper() for row in word_list for word in row if len(word) > 3]
    return res

word_list = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]

def generate_fibonacci():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


def generate_sequence(limit):
    for number in range(1, limit + 1):
        yield number

def is_prime_number(n):
    if n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True

def generate_primes():
    current = 2
    while True:
        if is_prime_number(current):
            yield current
        current += 1

def count_characters(input_text):
    from collections import Counter
    frequency = Counter(input_text)
    for character, occurrences in frequency.items():
        yield character, occurrences

fib_sequence = generate_fibonacci()
print("Fibonacci Sequence:")
for _ in range(5):
    print(next(fib_sequence), end=" ")  

print("\n\nCustom Sequence Generator :")
for value in generate_sequence(5):
    print(value, end=" ")  

print("\n\nPrime Number Generator:")
prime_numbers = generate_primes()
for _ in range(5):
    print(next(prime_numbers), end=" ") 

print("\n\nCharacter Counter:")
for character, count in count_characters("hello reckonsys"):
    print(f"'{character}' appeared {count} times")


result = prblmW(word_list)
print(result)


result = prblm(matrix)
print(result)
