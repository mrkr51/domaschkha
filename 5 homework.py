n = int(input())
def get_fib(n):
    itog = []
    if n <= 0:
        return itog
    if n == 1:
        itog.append(0)
        return itog
    itog = [0, 1]
    a = 0
    b = 1
    for i in range(n - 2):
        sleduyushee = a + b
        itog.append(sleduyushee)
        a = b
        b = sleduyushee
    return itog
rezultat = get_fib(n)
print(rezultat)