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
