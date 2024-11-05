# 1. Lista de cuvinte si alegerea cuvantului la întâmplare

import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _incuvant_de_ghicit]

# 2. Inițializarea numarului de încercări
incercari_ramase = 6
litere_incercate = []

print(" ".join(progres))

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introduceți o literă: ").lower()
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog introdu doar o singură literă!")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă! Încearcă altă literă.")
        continue

litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
else:
incercari_ramase -= 1
print(f"Încercări rămase: {incercari_ramase}")

print(" ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}!")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
