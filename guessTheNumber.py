#Number guessing game

import random
salaNumero=random.randint(1, 20)

print('Arvaa oikein numero 1 ja 20 välillä')

#arvuutetaan  kuusi kertaa

for arvaukset in range(1, 7):
    print('Arvaa')

    try:
        arvaus=int(input())
       

        if arvaus == salaNumero:
            print('Oikein!')
            print('Käytit ' + str(arvaukset) + ' arvausta.')
            break
        elif arvaus < salaNumero:
            print('Vähän alakanttiin')

        elif arvaus > salaNumero:
            print('Liikaa')

    except ValueError:
        print('Kokeile numeroa')
      

if arvaus != salaNumero:
    print('Et arvannut oikein')


    
