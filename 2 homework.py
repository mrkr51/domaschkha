def naiti_chislo_rekursiej(niz, verh, popitka):
    if niz == verh:
        print("************************************")
        print(f"Ура! Ответ найден. Это число: {niz}")
        print(f"Всего было задано вопросов: {popitka}")
        return

    sredinka = (niz + verh) // 2

    print(f"Шаг №{popitka}. Проверяю между {niz} и {verh}...")

    vopros = input(f"Твое число меньше чем {sredinka}? (да/нет): ")
    vopros = vopros.lower()

    if vopros == "да":
        naiti_chislo_rekursiej(niz, sredinka - 1, popitka + 1)
    elif vopros == "нет":
        naiti_chislo_rekursiej(sredinka, verh, popitka + 1)
    else:
        print("Ой, я не понял ответ. Попробуй еще раз написать 'да' или 'нет'.")
        naiti_chislo_rekursiej(niz, verh, popitka)


print("--- Программа 'Рекурсивный Угадайка' ---")
print("Загадай что-нибудь от -1000 до 1000")

naiti_chislo_rekursiej(-1000, 1000, 1)