from model.Distributore import Distributore
from model.Popolare import popolaIlDatabase

distributore = Distributore()
popolaIlDatabase(distributore)#Aggiunge bibite, carte e colonne.
print("------------------------------")

#distributore.aggiungiBevanda("l","limonata",10) #Aggiungo una bevanda al database
#Richiedo il prezzo di una bevanda indicando il suo codice
#print("Prezzo bevanda richiesta:",distributore.getPrice("l"))# La bevanda è presente nel DB
#print("Prezzo bevanda richiesta:",distributore.getPrice("m"))# La bevanda non è presente nel DB

#Richiedo il nome di una bevanda indicando il suo codice
#print ("Nome bevanda richiesta:", distributore.getNome("l")) #La bevanda è presente nel DB
#print ("Nome bevanda richiesta:", distributore.getNome("m")) #La bevanda non è presente nel DB

#distributore.caricaTessera(33,100) #Carico una tessera con codice 33 e credito 100
#Controllo il credito su una tessera
#print("Il credito disponibile sulla tessera è: ", distributore.leggiCredito(33)) #La tessera è presente
#print("Il credito disponibile sulla tua tessera è ", distributore.leggiCredito(44)) #la tessera non è presente

#distributore.aggiornaColonna("2","acqua","30") #Aggiungo una colonna (N°2) con 30 lattine di acqua.
#print("Le lattine disponibili sono:", distributore.lattineDisponibili("A")) #Controllo quante lattine di (acqua) sono presenti nel distributore


#distributore.erogaBibita("b",10)#Prelevo una lattina di birra con la carta 10
#distributore.erogaBibita("a",10)#Prelevo una lattina di acqua con la carta 10
#distributore.erogaBibita("z",10)#Non ho unabibita con codice z
#distributore.erogaBibita("k",10)#Le lattine con codice k sono terminate
#distributore.erogaBibita("a",40)#Erogo una lattina di acqua con la carta 40
#distributore.erogaBibita("a",40)#La carta 40 non ha più credito per prelevare una lattina di acqua