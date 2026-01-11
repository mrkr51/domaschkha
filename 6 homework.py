n = int(input())

cache = {}

def get_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in cache.keys():
        saved_value = cache[n]
        return saved_value

    first_part = get_fib(n - 1)
    second_part = get_fib(n - 2)

    total_result = first_part + second_part

    cache[n] = total_result

    return total_result

final_answer = get_fib(n)
print(final_answer)