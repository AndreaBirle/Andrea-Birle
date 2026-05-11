from __future__ import annotations
from dataclasses import dataclass
from student import StudentCNP


@dataclass
class Nod:
    student: StudentCNP
    urmator: 'Nod | None' = None

    def __str__(self):
        return str(self.student)


class Stiva:

    def __init__(self, fisier: str):

        self.varf = None
        self.n = 0

        with open(fisier, "r", encoding="utf-8") as f:

            for linie in f:

                linie = linie.strip()

                if not linie:
                    continue

                parts = [p.strip() for p in linie.split(",")]

                if len(parts) != 6:
                    raise ValueError(f"Linie CSV invalida: {linie}")

                nume, prenume, spec, an, medie, cnp = parts

                st = StudentCNP(
                    nume_prenume=f"{nume} {prenume}",
                    specializare=spec,
                    an_studiu=int(an),
                    medie=float(medie),
                    cnp=cnp
                )

                self.adauga(st)

    def adauga(self, student: StudentCNP):

        self.varf = Nod(student, self.varf)
        self.n += 1

    def afiseaza(self):

        print()

        a = self.varf

        while a:
            print(a.student)
            a = a.urmator

    def __getitem__(self, i):

        return self.sari_peste(i).student

    def __setitem__(self, i, student):

        self.sari_peste(i).student = student

    def sari_peste(self, i):

        a = self.varf

        if i < 0 or i >= self.n:
            raise ValueError(f"Index out of range: {i}")

        for _ in range(i):
            a = a.urmator

        return a

    # operator +

    def __add__(self, other):

        rezultat = Stiva.__new__(Stiva)

        rezultat.varf = None
        rezultat.n = 0

        a = self.varf
        while a:
            rezultat.adauga(a.student)
            a = a.urmator

        b = other.varf
        while b:
            rezultat.adauga(b.student)
            b = b.urmator

        return rezultat

    # operator -

    def __sub__(self, other):

        rezultat = Stiva.__new__(Stiva)

        rezultat.varf = None
        rezultat.n = 0

        cnp_exmatriculati = set()

        a = other.varf
        while a:
            cnp_exmatriculati.add(a.student.cnp)
            a = a.urmator

        b = self.varf
        while b:

            if b.student.cnp not in cnp_exmatriculati:
                rezultat.adauga(b.student)

            b = b.urmator

        return rezultat

    # sortare alfabetica

    def sorteaza_alfabetic(self):

        sortat = False

        while not sortat:

            sortat = True

            for i in range(self.n - 1):

                if self[i].nume_prenume > self[i + 1].nume_prenume:

                    self[i], self[i + 1] = self[i + 1], self[i]

                    sortat = False

    # sortare dupa medie

    def sorteaza_medie(self):

        sortat = False

        while not sortat:

            sortat = True

            for i in range(self.n - 1):

                if self[i].medie < self[i + 1].medie:

                    self[i], self[i + 1] = self[i + 1], self[i]

                    sortat = False