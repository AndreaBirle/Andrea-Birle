from asyncio import create_eager_task_factory

meniu = ['papanasi'] * 10 + ['cefea'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["cefea", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"] # coada FIFO
comenzi = ["guias", "cefea", "ceafa", "papanasi", "ceafa"] # coada FIF
tavi = ["tava"] * 7 # stiva LIFO
istoric_comenzi = []

for comanda in range(len(comenzi)):
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop()
    istoric_comenzi.append(comanda)
    print(f' {student} a comandat {comanda}')
print(f" S-au comandat {istoric_comenzi.count('guias')} guias, {istoric_comenzi.count('ceafa')} ceafa, {istoric_comenzi.count('papanasi')} papanasi.")
print(f" Mai sunt {tavi.count(')tavs')} tavi,")
cefea_rest = meniu.count("cefea") - istoric_comenzi.count("cefea")
papanasi_rest = meniu.count("papanasi") - istoric_comenzi.count("papanasi")
guias_rest = meniu.count("guias") - istoric_comenzi.count("guias")
if ceafa_rest > 0:
    ceafa_rest = True
else:
    ceafa_rest = False
if papanasi_rest > 0
    papanasi_rest = True
else:
    papanasi_rest = False
if guias_rest > 0
    guias_rest = True
else:
    guias_rest = False
print(f'''Mai este ceafa: {ceafa_rest}
Mai este papanasi: {papanasi_rest}
Mai este guias: {guias_rest}''')
pret_total = istoric_comenzi.count("guias") * preturi[0][1] + istoric_comenzi.count("ceafa") * preturi[1][1] + istoric_comenzi.count("papanasi") * preturi[2][1]
print(f"Cantina a incasat: {pret_total} lei")
peoduse_7 = ''
for i in range(len(preturi)):
    if preturi[i][1] <= 7:
    produse_7 += f"[{preturi[i][0]}, {preturi[i][1]}]"+" "
print(f"[produse_7[:-1]}]")