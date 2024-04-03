from random import randint
import time, os
print('Datorspēle \'Uzmini skaitli\'.')
print('Lietotājam ir 10 iespējas, lai uzminēt skaitli.')
print('Dators "iedomājas" veselo skaitli no 1 līdz 100(ieskaitot). ', end='\n\n')
print('Uzminiet skaitli. ')
datora_skaitlis = randint(1,100)
iespeja = 1

neuzmineja = True
while neuzmineja:
    print(iespeja, "iespeja no 10.")
    ievade = input("Ievadiet skaitli no 1 lidz 100, ieskaitot 1 un 100: ")
    lietotaja_skaitlis = int(ievade)
    if lietotaja_skaitlis < 1:
        print("Kļūda! Ievadiet pareizo skaitli (no 1 līdz 100).")
    elif lietotaja_skaitlis > 100:
        print("Kļūda! Ievadiet pareizo skaitli (no 1 līdz 100).")
    elif iespeja == 10:
        neuzmineja = False
        print(" _______                              .__                   __        __            ___")
        time.sleep(1)
        print(" \      \   ____  __ __________ _____ |__| ____   ____     |__|____ _/  |_   /\    /  /")
        time.sleep(1)
        print(" /   |   \_/ __ \|  |  \___   //     \|  |/    \_/ __ \    |  \__  \\   __\   \/   /  / ")
        time.sleep(1)
        print("/    |    \  ___/|  |  //    /|  Y Y  \  |   |  \  ___/    |  |/ __ \|  |    /\  (  (  ")
        time.sleep(1)
        print("\____|__  /\___  >____//_____ \__|_|  /__|___|  /\___  >\__|  (____  /__|    \/   \  \ ")
        time.sleep(1)
        print("        \/     \/            \/     \/        \/     \/\______|    \/              \__\\")
    elif datora_skaitlis < lietotaja_skaitlis:
        print ( "Neuzminējāt. Ievadiet mazāku skaitli. ")
        iespeja = iespeja + 1
    else:
        if datora_skaitlis > lietotaja_skaitlis:
            print ("Neuzminējāt. Ievadiet lielāku skaitli. ")
            iespeja = iespeja + 1
        else:
            neuzmineja = False
            print(" ____ ___                 __                   __        __  ._._._.")
            time.sleep(1)
            print("|    |   \________ _____ |__| ____   ____     |__|____ _/  |_| | | |")
            time.sleep(1)
            print("|    |   /\___   //     \|  |/    \_/ __ \    |  \__  \\   __\ | | |")
            time.sleep(1)
            print("|    |  /  /    /|  Y Y  \  |   |  \  ___/    |  |/ __ \|  |  \|\|\|")
            time.sleep(1)
            print("|______/  /_____ \__|_|  /__|___|  /\___  >\__|  (____  /__|  ______")
            time.sleep(1)
            print("                \/     \/        \/     \/\______|    \/      \/\/\/")
os.system("PAUSE")