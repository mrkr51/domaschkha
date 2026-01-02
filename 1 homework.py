desicion = input("Привет, хочешь сняться в кино? [Да\Нет]")

if desicion.lower() == "да":
    person = input("Кем хочешь быть? [Халк\Локи]")

    if person.lower() == "халк":
        try:
            biceps = int(input("Сколько см твой бицепс? "))
            if biceps >= 60:
                print("с кайфом ты хорош")
            else:
                print("немощь")
        except:
            print("Ты что-то перепутал, начинай сначала")

    elif person.lower() == "локи":
        love = input("Кого любишь больше - маму или папу?")

        if love.lower() == "папу":
            print("неправильно")
        elif love.lower() == "маму":
            print("Иди к папе и спроси еще раз")
        else:
            print("общайся нормально")

    else:
        print("Такой роли нет, ошибка")

elif desicion.lower() == "нет":
    print("тогда пока")

else:
    print("еще раз")