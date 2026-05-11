from dataclasses import dataclass

@dataclass
class Student:
    nume_prenume: str
    specializare: str
    an_studiu: int
    medie: float

    def __str__(self) -> str:
        return (f"{self.nume_prenume:20s} | {self.specializare:5s} | "
                f"an {self.an_studiu} | medie {self.medie:.2f}")


@dataclass
class StudentCNP(Student):
    cnp: str

    def __str__(self) -> str:
        return f"{super().__str__()} | CNP {self.cnp}"