from model.Bibita import Bibita
from model.Tessera import Tessera
from model.Colonna import Colonna

class Distributore:
    def  __init__(self):
        self.Tesserati = []
        self.Bibite = []
        self.Colonne = []


    def aggiungiBevanda(self, codice, nome, prezzo): #Aggiunge una bevanda alla lista delle selezionabili
        if prezzo >0:
            bevanda = Bibita(codice, nome , prezzo)
            self.Bibite.append(bevanda)
            print("Bevanda ", nome, " aggiunta con codice ", codice, " e prezzo", prezzo)
        else:
            print("Il prezzo deve esser maggiore di zero")


    def getPrice(self, codiceBibita): #Dato un codiceBibita restituisce il prezzo della bibita se esiste
        for bibita in self.Bibite:
            if bibita.codice.lower() == codiceBibita.lower():
                return(bibita.prezzo)

        else:
            return("Bevanda non valida")

    def getNome(self, codiceBibita): #Dato un codiceBibita restituisce il nome se esiste
        for bibita in self.Bibite:
            if bibita.codice.lower() == codiceBibita.lower():
                return(bibita.bevanda)
        else:
            return("Bibita non trovata")



    def caricaTessera(self, codiceTessera, credito):  #Permette di aggiungere una tessera e un credito
        if credito > 0:
            tessera = Tessera(codiceTessera,credito)
            for tes in self.Tesserati:
                if tes.codice == codiceTessera:
                    self.cancellaTessera(codiceTessera)#se la tessera è già esistente la cancella

            else:
                self.Tesserati.append(tessera)
        else:
            print("il credito deve esser maggiore di 0")

    def cancellaTessera(self, codiceTessera): #Cerca un codiceTessera e se esiste lo cancella
        for tessera in self.Tesserati:
            if tessera.codice == codiceTessera:
                self.Tesserati.remove(tessera)


    def leggiCredito(self, codiceTessera ): #Dato un ID tessera restituisce il credito presente. Se l'id esiste
        for tessera in self.Tesserati:
            if tessera.codice == codiceTessera:
                return (tessera.credito)
                break
        else:
            return ("Tessera non esistente")

    def aggiornaColonna(self,colonna, bibita, lattine): #Permette di aggiungere una colonna con il quantitativo e la descrizione di bevande
        storage = Colonna(colonna, bibita, lattine)
        for col in self.Colonne:
            if col.numero == int(colonna):
                self.cancellaColonna(col.numero) #Se la colonna esiste già la cancella per ricrearla
        else:
            self.Colonne.append(storage)


    def normalizzaColonne(self): #Porta a zero tutte le colonne che hanno un numero negativo di lattine
        for colonna in self.Colonne:
            if int(colonna.lattine) <= 0:
                colonna.lattine = 0

    def cancellaColonna(self, numeroColonna): #Controlla che numero colonna esiste e lo cancella
        for colonna in self.Colonne:
            if colonna.numero == numeroColonna:
                self.Colonne.remove(colonna)



    def lattineDisponibili(self, codiceBibita): #dato un ID bibita restituisce la disponibilità in tutte le colonne
        self.normalizzaColonne()
        nome = self.getNome(codiceBibita)
        if nome != "Bibita non trovata":
            cont=0
            for lattina in self.Colonne:
                if lattina.bibita == nome:
                    cont=cont+lattina.lattine
            if cont == 0:
                return("Bibita esaurita")
            else:
                return(cont)

        else:
            return(nome)



    def erogaBibita(self, codiceBibita, codiceTessera):
        """Controlla che la tessera esista e che abbia credito a sufficienza. Controlla che la bevanda esista e ci sia almeno una lattina
        dopo di che eroga la lattina e restituisce da quale colonna viene ritirata. Aggiornando scorte e credito"""
        credito = self.leggiCredito((codiceTessera))
        prezzo = self.getPrice(codiceBibita)
        disp= self.lattineDisponibili(codiceBibita)
        nome = self.getNome(codiceBibita)
        if type(prezzo) != str:
            if type(credito) != str :
                if type(disp) !=str:
                    for lattina in self.Colonne:
                        if lattina.bibita == nome and lattina.lattine > 0:
                            if(credito>prezzo):
                                credito =round(credito - prezzo, 2)
                                lattina.lattine=lattina.lattine-1
                                print("Hai scelto una lattina di", nome,"il cui costo è: ", prezzo,"è stata erogata dalla colonna", lattina.numero, "il credito finale della tesssera", codiceTessera, " è:", credito)
                                self.cancellaTessera(codiceTessera)
                                self.cancellaColonna(lattina.numero)
                                self.caricaTessera(codiceTessera, credito)
                                self.aggiornaColonna(lattina.numero, nome, lattina.lattine )
                                break
                            else:
                                print("credito insufficiente")
                else:
                    print(disp)
            else:
                print(credito)
        else:
            print(prezzo)


