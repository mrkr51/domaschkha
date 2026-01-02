imya_polzovatelya = input("Введите любое имя на ваш вкус : ")


def sdelat_krasivoe_imya(staroe_imya):
    itogovij_rezultat = ""
    kolichestvo_bukv = len(staroe_imya)

    for nomer in range(kolichestvo_bukv):
        simvol = staroe_imya[nomer]

        if (nomer + 1) % 2 == 0:
            bukva_v_verhnem_registre = simvol.upper()
            itogovij_rezultat = itogovij_rezultat + bukva_v_verhnem_registre
        else:
            bukva_v_nizhnem_registre = simvol.lower()
            itogovij_rezultat = itogovij_rezultat + bukva_v_nizhnem_registre

    return itogovij_rezultat


def skazat_privet(imya):
    print("<<< Результат программы >>>")
    print("Hello", imya)


izmenennoe_imya = sdelat_krasivoe_imya(imya_polzovatelya)
skazat_privet(izmenennoe_imya)