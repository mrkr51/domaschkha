n = int(input())

def fib_rec(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    
    summa = fib_rec(k - 1) + fib_rec(k - 2)
    return summa

itog_list = []
for i in range(n):
    chislo = fib_rec(i)
    itog_list.append(chislo)

print(itog_list)
