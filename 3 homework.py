kolichestvo_strok = int(input("Введите количество строк для треугольника Паскаля: "))

vse_stroki = []

for nomer_stroki in range(kolichestvo_strok):
    novaya_stroka = []

    for j in range(nomer_stroki + 1):
        if j == 0 or j == nomer_stroki:
            novaya_stroka.append(1)
        else:
            predidushaya_stroka = vse_stroki[nomer_stroki - 1]
            summa_chisel = predidushaya_stroka[j - 1] + predidushaya_stroka[j]
            novaya_stroka.append(summa_chisel)

    vse_stroki.append(novaya_stroka)

print("\n--- Результат ---")

shirina_polya = kolichestvo_strok * 3

for i in range(kolichestvo_strok):
    stroka_dlya_pechati = ""

    for chislo in vse_stroki[i]:
        stroka_dlya_pechati = stroka_dlya_pechati + str(chislo) + " "

    print(stroka_dlya_pechati.center(shirina_polya))