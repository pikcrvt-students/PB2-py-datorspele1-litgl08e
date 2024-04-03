from random import randint
import time
import os
print('Datorspēle \'Uzmini skaitli\'.')
print('Dators "iedomājas" veselo skaitli no 1 līdz 10. ', end='\n\n')
print('Uzminiet skaitli. ')
datora_skaitlis = randint(1,100)
iespeja = 9

neuzmineja = True
while neuzmineja:
    ievade = input("Ievadiet skaitli no 1 lidz 100, ieskaitot 100: ")
    lietotaja_skaitlis = int(ievade)
    if iespeja == 0:
        neuzmineja = False
        print(" _______                              .__                   __        __            ___", end='\n', flush=True)
        time.sleep(1)
        print(" \      \   ____  __ __________ _____ |__| ____   ____     |__|____ _/  |_   /\    /  /", end='\n', flush=True)
        time.sleep(1)
        print(" /   |   \_/ __ \|  |  \___   //     \|  |/    \_/ __ \    |  \__  \\   __\   \/   /  / ", end='\n', flush=True)
        time.sleep(1)
        print("/    |    \  ___/|  |  //    /|  Y Y  \  |   |  \  ___/    |  |/ __ \|  |    /\  (  (  ", end='\n', flush=True)
        time.sleep(1)
        print("\____|__  /\___  >____//_____ \__|_|  /__|___|  /\___  >\__|  (____  /__|    \/   \  \ ", end='\n', flush=True)
        time.sleep(1)
        print("        \/     \/            \/     \/        \/     \/\______|    \/              \__\\", end='\n', flush=True)
    elif datora_skaitlis < lietotaja_skaitlis:
        print ( "Neuzminējāt. Ievadiet mazāku skaitli. ")
        iespeja = iespeja - 1
    else:
        if datora_skaitlis > lietotaja_skaitlis:
            print ("Neuzminējāt. Ievadiet lielāku skaitli. ")
            iespeja = iespeja - 1
        else:
            neuzmineja = False
            print(" ____ ___                 __                   __        __  ._._._.", end='\n', flush=True)
            time.sleep(1)
            print("|    |   \________ _____ |__| ____   ____     |__|____ _/  |_| | | |", end='\n', flush=True)
            time.sleep(1)
            print("|    |   /\___   //     \|  |/    \_/ __ \    |  \__  \\   __\ | | |", end='\n', flush=True)
            time.sleep(1)
            print("|    |  /  /    /|  Y Y  \  |   |  \  ___/    |  |/ __ \|  |  \|\|\|", end='\n', flush=True)
            time.sleep(1)
            print("|______/  /_____ \__|_|  /__|___|  /\___  >\__|  (____  /__|  ______", end='\n', flush=True)
            time.sleep(1)
            print("                \/     \/        \/     \/\______|    \/      \/\/\/", end='\n', flush=True)
os.system("PAUSE")