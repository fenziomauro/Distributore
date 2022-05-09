from model.Distributore import Distributore
from model.Popolare import popolaIlDatabase

distributore = Distributore()
popolaIlDatabase(distributore)


distributore.caricaTessera(33, 10)
print ("Al momento la tua carta ha un credito di", distributore.leggiCredito(33))
