import random

while True:
    print("\nVali:")
    valik = input("Ülesanded (10, 12, 21, 22, 31), 0 - väljumiseks: ")

    if valik == "10":
        print("Valisid 10. Klaviatuurilt sisestatakse 10 arvu paari. Võrdle neid ja väljasta suurem.")
        for i in range(10):
            while True:
                try:
                    a = float(input(f"Paar {i+1} - sisesta esimene arv: "))
                    b = float(input(f"Paar {i+1} - sisesta teine arv: "))
                    break
                except ValueError:
                    print("VIGA! Palun sisesta numbrid.")
            
            if a > b:
                print(f"Suurem arv on: {a}")
            elif b > a:
                print(f"Suurem arv on: {b}")
            else:
                print("Arvud on võrdsed.")

    elif valik == "12":
        print("Valisid 12. Heina niitmise brigaad (N niidukit).")
        while True:
            try:
                N = int(input("Sisesta niidukite arv N: "))
                m = float(input("Sisesta esimese niiduki töötunnid m: "))
                if N < 1 or m < 0:
                    print("Vale sisend! Arvud peavad olema positiivsed.")
                    continue
                break
            except ValueError:
                print("VIGA! Palun sisesta täisarvud/arvud.")

        kokku_tunde = 0
        aktiivne_tund = m
        for i in range(N):
            kokku_tunde += aktiivne_tund
            aktiivne_tund += 10 / 60 

        print(f"Brigaad töötas kokku {round(kokku_tunde, 2)} tundi.")

    elif valik == "21":
        print("Valisid 21. 10 arvu: asenda negatiivsed arvud nende absoluutväärtustega.")
        arvud = []
        for i in range(10):
            while True:
                try:
                    arv = float(input(f"Sisesta {i+1}. arv: "))
                    break
                except ValueError:
                    print("VIGA! Palun sisesta arv.")
            if arv < 0:
                arv = abs(arv)
            arvud.append(arv)
        print("Tulemus:", arvud)

    elif valik == "22":
        print("Valisid 22. Arvude 100 kuni 200 summa, mis on 17-ga jaguvad.")
        summa = 0
        for i in range(100, 201):
            if i % 17 == 0:
                print(i, end=" ")
                summa += i
        print(f"\nNende arvude summa on: {summa}")

    elif valik == "31":
        print("Valisid 31. Spongi Bob praeb kotlette")
        while True:
            try:
                K = int(input("Sisesta kotlettide kogus (K): "))
                M = int(input("Sisesta pannile mahtuvate kotlettide arv (M): "))
                if K < 0 or M <= 0:
                    print("Vale sisend! Kogus peab olema >= 0 ja pann mahutama vähemalt 1 kotleti.")
                    continue
                break
            except ValueError:
                print("VIGA! Palun sisesta täisarvud.")

        tais_pannid = K // M
        viimane_pann = K % M
        print(f"Täis pannitäisi: {tais_pannid}")
        if viimane_pann > 0:
            print(f"Viimasele pannile jääb: {viimane_pann} kotletti")
        else:
            print("Kõik kotletid mahtusid täpselt täispannidele!")

    elif valik == "0":
        print("Väljumine...")
        break
    else:
        print("Vale valik!")