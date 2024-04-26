import time

size = 0
limit = 0
dishes = {}
dishes_washed = {}

print("Esta lava-louça suporta:")
print("-(1)Talheres;")
print("-(2)Copos;")
print("-(4)Pratos;")
print("-(8)Panelas.")
print(" ")
print("Cada louça tem um número designado, que é seu tamanho. Este tamanho é calculado por esse número e pela quantidade inserida.")
print("Como a máquina suporta um volume limitado (30), você não pode ultrapassar seu limite.")
print(" ")

while size < 30:
    dish = str(input("Que louça deseja colocar na máquina? (digite em plural): "))
    qtty = int(input("Quantas louças deste tipo?: "))

    if dish.capitalize() == "Talheres" and qtty > 0:
        volume = qtty * 1
        size += volume
        print(f"A máquina está com um volume de {size}/30")
    elif dish.capitalize() == "Copos" and qtty > 0:
        volume = qtty * 2
        size += volume
        print(f"A máquina está com um volume de {size}/30")
    elif dish.capitalize() == "Pratos" and qtty > 0:
        volume = qtty * 4
        size += volume
        print(f"A máquina está com um volume de {size}/30")
    elif dish.capitalize() == "Panelas" and qtty > 0:
        volume = qtty * 8
        size += volume
        print(f"A máquina está com um volume de {size}/30")
    else:
        print("A máquina não conseguiu identificar esta louça ou você inseriu uma quantidade menor que 1. Tente novamente.")
        continue

    dishes.update({dish.capitalize(): qtty})
    washing = []
    washing.append(dishes)

    if size > 30:
        print("A máquina quebrou!")
        break
    elif size == 30:
        print("A máquina está cheia! Estas são as louças que estão nela:", dishes)
        break

    limit += 1

    if limit == 4:
        print("Estas são as louças que estão na máquina:", dishes)
        break

    answer = str(input("Continuar? [s/n]: "))

    if answer == "n":
        print("Estas são as dishes que estão na máquina:", dishes)
        break

print(" ")

while size <= 30:
    dish_filtered = str(input("Que tipo de louça deseja lavar agora?: "))
    qtty_dish = [d[dish_filtered.capitalize()] for d in washing if dish_filtered.capitalize() in d]

    if qtty_dish:
        print(f"Há {qtty_dish} {dish_filtered}.")
        wash = str(input("Lavar? [s/n]: "))

        if wash == "n":
            continue
        else:
            for d in washing:
                if dish_filtered.capitalize() in d:
                    drying = []

                    def oper_washing():
                        dishes_washed.update({dish_filtered.capitalize(): dishes[dish_filtered.capitalize()]})
                        drying.append(dishes_washed)
                        del d[dish_filtered.capitalize()]
                        print(f"A máquina acabou de colocar {qtty_dish} {dish_filtered} para secar.")

                        if dishes:
                            print(f"Há ainda {dishes} para lavar.")
                    
                    def countdown_washing(timer):
                        while timer > 0:
                            print("A louça será lavada em", timer, "segundos")
                            time.sleep(1)
                            timer -= 1
                        
                        oper_washing()
                    
                    if dish_filtered.capitalize() == "Talheres":
                        timer = dishes[dish_filtered.capitalize()] * 0.5
                        countdown_washing(timer)
                    elif dish_filtered.capitalize() == "Copos":
                        timer = dishes[dish_filtered.capitalize()] * 1
                        countdown_washing(timer)
                    elif dish_filtered.capitalize() == "Pratos":
                        timer = dishes[dish_filtered.capitalize()] * 2
                        countdown_washing(timer)
                    elif dish_filtered.capitalize() == "Panelas":
                        timer = dishes[dish_filtered.capitalize()] * 4
                        countdown_washing(timer)
    else:
        print("Esta louça não está na máquina. Tente novamente.")
        continue
    if not dishes:
        print("A máquina lavou toda a louça! Vamos secar agora.")
        break

    answer2 = str(input("Continuar? [s/n]: "))

    if answer2 == "n":
        print("Vamos secar agora.")
        break

print(" ")

while dishes_washed:
    dish_filtered2 = str(input("Que tipo de louça deseja secar agora?: "))
    qtty_dish_washed = [d[dish_filtered2.capitalize()] for d in drying if dish_filtered2.capitalize() in d]

    if qtty_dish_washed:
        print(f"Há {qtty_dish_washed} {dish_filtered2}")
        dry = str(input("Secar? [s/n]: "))

        if dry == "n":
            continue
        else:
            for d in drying:
                if dish_filtered2.capitalize() in d:
                    def oper_drying():
                        del d[dish_filtered2.capitalize()]
                        print(f"A máquina secou {qtty_dish_washed} {dish_filtered2}.")

                        if dishes_washed:
                            print(f"Há ainda {dishes_washed} para secar.")

                    def countdown_drying(timer2):
                        while timer2 > 0:
                            print("A louça será secada em", timer2, "segundos")
                            time.sleep(1)
                            timer2 -= 1
                            
                        oper_drying()

                    if dish_filtered2.capitalize() == "Talheres":
                        timer2 = dishes_washed[dish_filtered2.capitalize()] * 0.5
                        countdown_drying(timer2)
                    elif dish_filtered2.capitalize() == "Copos":
                        timer2 = dishes_washed[dish_filtered2.capitalize()] * 1
                        countdown_drying(timer2)
                    elif dish_filtered2.capitalize() == "Pratos":
                        timer2 = dishes_washed[dish_filtered2.capitalize()] * 2
                        countdown_drying(timer2)
                    elif dish_filtered2.capitalize() == "Panelas":
                        timer2 = dishes_washed[dish_filtered2.capitalize()] * 4
                        countdown_drying(timer2)
    else:
        print("Esta louça não está para secar. Tente novamente.")
        continue
    if not dishes_washed:
        print("Você secou toda a louça!")
        break

    answer3 = str(input("Continuar? [s/n]: "))

    if answer3 == "n":
        break