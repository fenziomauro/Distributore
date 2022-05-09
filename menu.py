from model.Distributore import Distributore
from model.Popolare import popolaIlDatabase

distributore = Distributore()
popolaIlDatabase(distributore)


while True:
    print(" Ciao Utente. Pronto per una bibita fresca?")
    ordine = str(
        input("""
        Cosa vuoi fare?
        [a] Aggiungi Bevanda
        [rn] Cerca il nome di una bevanda partendo dal codice 
        [rp] Cerca il prezzo di una bevanda partendo dal codice
        [c]  Carica una tessera
        [vc] Verifica il tuo credito
        [ac] Aggiorna una colonna di bibite
        [ld] Guarda quante lattine disponibili sono rimaste di una determinata bibita 
        [e]  Inserisci il codice e la tessera e avrai la tua lattina
        [u] Uscire.
    """))
    if ordine == "a":
        codice = str(input("Quale è il codice: "))
        nome = str(input("quale è il Nome della bevanda: "))
        prezzo = str(input("Quale è il prezzo della bevanda: "))

        distributore.aggiungiBevanda(codice, nome, prezzo)

    elif ordine == "rn":
        codice = str(input("Quale è il codice della bevanda: "))
        print("Il nome della bevanda con codice ",codice, "è: ", distributore.getNome(codice))

    elif ordine == "rp":
        codice = str(input("Quale è il codice della bevanda: "))
        print("Il prezzo della bevanda con codice ", codice, "è: ", distributore.getPrice(codice))

    elif ordine == "c":
        id = int(input("Dammi il codice della tessera: "))
        money = int(input("Quanto credito vuoi nella tessera? "))
        distributore.caricaTessera(id,money)

    elif ordine == "vc":
        id = int(input("Dammi il codice della tessera: "))
        print("Al momento la tua tessera dispone di un credito di: ", distributore.leggiCredito(id))

    elif ordine == "ac":
        n = int(input("Dammi il numero della colonna: "))
        desc = str(input("Dammi la descrizione della bevanda: "))
        numero = int(input("Quante lattine ci sono nella colonna? "))
        distributore.aggiornaColonna(n,desc,numero)

    elif ordine == "ld":
        id = str(input("Dammi il codice della bibita di cui vuoi sapere il residuo: "))
        bibita = distributore.getNome(id)
        print("Ci sono ",distributore.lattineDisponibili(id), "lattine disponibili di ", bibita, "all'interno del distributore")

    elif ordine == "e":
        code = str(input("Dammi il codice della bibita che vuoi prelevare: "))
        credito = int(input("Dammi il codice ID della tua tessera: "))
        distributore.erogaBibita(code, credito)

    elif ordine == "u":
        print("Ciao ciao")
        break
    else:
        print("Selezione errata")