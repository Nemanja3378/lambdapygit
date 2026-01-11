from datetime import date

while(True):
    risultato = 0
    operazione = input("Inserisci un operazione (+, -, *, /, giorni): ")
    if operazione in ["+", "-", "*", "/"]:
        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError:
            print("Errore: devi inserire numeri validi.")
            continue

        if operazione == "+":
            risultato = num1 + num2
        elif operazione == "-":
            risultato = num1 - num2
        elif operazione == "*":
            risultato = num1 * num2
        elif operazione == "/":
            if num2 == 0:
                print("Errore: divisione per 0 non permessa.")
            else:
                risultato = num1 / num2

        print("Il risultato è: ", risultato)

    else:
        print("Errore: input non validi.")

    continuo = input("Vuoi continuare? (si/no) ")
    if continuo == "no":
        break