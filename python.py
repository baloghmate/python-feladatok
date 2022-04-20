'''
1. Feladat
Készíts egy programot, amely [-30; 55] intervallumon kiírja a 4-mal osztható számokat!
'''
#megoldás:  
'''
for szamok in range(-30,55):
    if szamok %4 == 0:
        print(szamok)
'''
#----------------------------------------------


'''
2.1 Feladat
Az adott lista (amely a 'Próbáld ki!' gombra kattintva elérhető) elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket!
'''

#megoldás:
'''
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']

ts_szavak = [szo for szo in szavak if szo[0] == 't' or szo[0] == 'T']

print(ts_szavak)
'''
'''
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 8 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páratlan számok számát, valamint a lista elemeit!
'''

'''
#megoldás
import random
#üreslista
lista = []

#véletlen számot generál 8 darabot 1-10-es intervallumon
randomszam = [random.randint(1,10)for szamok in range(8)]

#hozzáfűzzük az üres listához
lista.append(randomszam)


#páratlan számokat keres
paratlanszamok = len([szamok for szamok in randomszam if szamok %2 != 0])

#ki printeljük a páratlan számokat
print(f'Páratlan számok száma: {paratlanszamok}')
#lista elemei
print(lista)
'''

'''
1. Feladat
Írj egy programot, amely 10 darab véletlenszámot generál [1;10] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
'''

#megoldás
'''
import random

veletlenszam  = [random.randint(1,10)for szamok in range(10)]

beker = int(input('Kérek egy számot (1-10): '))

if beker in veletlenszam:
    print('Előfurdol az általad megadott szám.')
else:
    print('Nem fordul elő a listában.')
'''
