from stiva import Stiva

g1 = Stiva("grupa1.txt")

g2 = Stiva("grupa2.txt")

an = g1 + g2

e = Stiva("exmatriculati.txt")

an = an - e

an.sorteaza_alfabetic()

an.afiseaza()

an.sorteaza_medie()

an.afiseaza()