class Dipendenti:
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int):
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale: str = codice_fiscale
        self.paga_oraria: int = paga_oraria

    def calcola_paga(self, ore_mensili: float) -> float:
        return ore_mensili * self.paga_oraria
    
    def __str__(self) -> str:
       return f"Dipendente: {self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}"
    
    def __eq__(self, other: object) -> bool:
        return type(other) is Dipendenti and self.paga_oraria == other.paga_oraria

    def __gt__(self, other: object) -> bool:
        return type(other) is Dipendenti and self.paga_oraria > other.paga_oraria
    
    def __lt__(self, other: object) -> bool:
        return type(other) is Dipendenti and self.paga_oraria < other.paga_oraria
    
class Manager(Dipendenti):
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int, numero_sottoposti: int):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.numero_sottoposti: int = numero_sottoposti


    def calcola_paga(self, ore_mensili: float) -> float:
        stipendio_base = super().calcola_paga(ore_mensili)
        bonus = self.numero_sottoposti * 50
        return stipendio_base + bonus
    
    def __str__(self) -> str:
        return f"Manager: {self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}, Sottoposti: {self.numero_sottoposti}"
    
class Commerciale(Dipendenti):
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int, percentuale_fatturato: float):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.percentuale_fatturato : float = percentuale_fatturato

    def calcola_paga(self, ore_mensili: float) -> float:
        stipendio_base = super().calcola_paga(ore_mensili)
        provvigione = stipendio_base * self.percentuale_fatturato / 100
        return stipendio_base + provvigione
    
    def __str__(self) -> str:
        return f"Commerciale: {self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}, Percentuale sul fatturato: {self.percentuale_fatturato}%"

class Azienda(Dipendenti):
    def __init__(self):
        self.dipendenti = []

    def aggiungi_dipendente(self, dipendente: Dipendenti) -> None:
        self.dipendenti.append(dipendente)

    def costo_totale_stipendi(self, ore_standard: float) -> float:
        totale = 0.0
        for dipendente in self.dipendenti:
            totale += dipendente.calcola_paga(ore_standard)
        return totale

    def commerciale_più_performante(self, fatturato: float) -> str:
        commerciale_migliore = None
        max_stipendio = 0.0
        for dipendente in self.dipendenti:
            if isinstance(dipendente, Commerciale):
                stipendio = dipendente.calcola_paga(fatturato)
                if stipendio > max_stipendio:
                    max_stipendio = stipendio
                    commerciale_migliore = dipendente
        return str(commerciale_migliore) if commerciale_migliore else "Nessun commerciale trovato"


dipendente1 = Dipendenti("Mario", "Rossi", "MRARSS80A01H501U", 15)
dipendente2 = Dipendenti("Luigi", "Verdi", "LGVRDI85B02F205X", 20)
manager1 = Manager("Anna", "Bianchi", "NNABNC90C03D303Y", 20, 5)
manager2 = Manager("Carlo", "Blu", "CRLBLU92D04E404Z", 28, 8)
commerciale1 = Commerciale("Paolo", "Neri", "PLONRI95D04E404Z", 25, 10)
commerciale2 = Commerciale("Sara", "Gialli", "SRAGLL88E05F505W", 30, 15)

azienda = Azienda()
azienda.aggiungi_dipendente(dipendente1)
azienda.aggiungi_dipendente(dipendente2)
azienda.aggiungi_dipendente(manager1)
azienda.aggiungi_dipendente(manager2)
azienda.aggiungi_dipendente(commerciale1)
azienda.aggiungi_dipendente(commerciale2)


for dip in azienda.dipendenti:
    print(dip)
    print("Stipendio mensile:", dip.calcola_paga(160))

if dipendente1.calcola_paga(160) > dipendente2.calcola_paga(160):
    print(f"{dipendente1.nome} ha una paga oraria maggiore di {dipendente2.nome}")
elif dipendente1.calcola_paga(160) < dipendente2.calcola_paga(160):
    print(f"{dipendente2.nome} ha una paga oraria maggiore di {dipendente1.nome}")
else:
    print(f"{dipendente1.nome} e {dipendente2.nome} hanno la stessa paga oraria")

if manager1.calcola_paga(160) > manager2.calcola_paga(160):
    print(f"{manager1.nome} ha una paga oraria maggiore di {manager2.nome}")
elif manager1.calcola_paga(160) < manager2.calcola_paga(160):
    print(f"{manager2.nome} ha una paga oraria maggiore di {manager1.nome}")
else:
    print(f"{manager1.nome} e {manager2.nome} hanno la stessa paga oraria")

if commerciale1.calcola_paga(160) > commerciale2.calcola_paga(160):
    print(f"{commerciale1.nome} ha una paga oraria maggiore di {commerciale2.nome}")
elif commerciale1.calcola_paga(160) < commerciale2.calcola_paga(160):
    print(f"{commerciale2.nome} ha una paga oraria maggiore di {commerciale1.nome}")
else:
    print(f"{commerciale1.nome} e {commerciale2.nome} hanno la stessa paga oraria")

print("Costo totale stipendi azienda:", azienda.costo_totale_stipendi(160))
print("Commerciale più performante:", azienda.commerciale_più_performante(160))