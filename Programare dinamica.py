import json
import random

def citeste_datele(denumire_fisier):
    with open(denumire_fisier, 'r') as f:
        return json.load(f)

def calculeaza_rest(rest, bancnote):
    dp = [(float('inf'), None)] * (rest + 1)
    dp[0] = (0, [0] * len(bancnote))

    for i, (valoare, stoc) in enumerate(bancnote):
        for r in range(rest, -1, -1):
            for k in range(1, stoc + 1):
                if r + valoare * k > rest:
                    break
                prev_count, prev_used = dp[r]
                if prev_used is not None:
                    new_used = prev_used.copy()
                    new_used[i] += k
                    new_count = prev_count + k
                    if new_count < dp[r + valoare * k][0]:
                        dp[r + valoare * k] = (new_count, new_used)

    return dp[rest] if dp[rest][1] is not None else None
0
def actualizeaza_stoc(bancnote, folosire):
    for i in range(len(bancnote)):
        bancnote[i] = (bancnote[i][0], bancnote[i][1] - folosire[i])

def simuleaza_casa(json_input):
    data = citeste_datele(json_input)
    produse = data['produse']
    bancnote = [(b['valoare'], b['stoc']) for b in data['bancnote']]

    client_id = 1
    while True:
        produs = random.choice(produse)
        pret = produs['pret']
        suma_platita = pret + random.randint(1, 20)
        rest = suma_platita - pret

        rezultat = calculeaza_rest(rest, bancnote)

        print(f"\nClient #{client_id}")
        print(f"Produs: {produs['nume']}")
        print(f"Preț: {pret} lei")
        print(f"Suma plătită: {suma_platita} lei")
        print(f"Rest de oferit: {rest} lei")

        if rezultat is None:
            print("NU se poate oferi restul cu bancnotele disponibile. Simularea se oprește.")
            break

        numar_bancnote, folosire = rezultat
        print("Rest oferit cu următoarele bancnote:")
        for (valoare, _), nr in zip(bancnote, folosire):
            if nr > 0:
                print(f"{nr} x {valoare} lei")

        actualizeaza_stoc(bancnote, folosire)
        client_id += 1
