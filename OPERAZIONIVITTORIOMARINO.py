

def somma(addendo1,addendo2):
        return addendo1+addendo2
def sottrazione(sottraendo,minuendo):
        return sottraendo-minuendo
def moltiplicazione(fattore1,fattore2):
        return fattore1*fattore2
def divisione(dividendo,divisore):
        return dividendo/divisore
        
print ("1. Somma")
print ("2. sottrazione")
print ("3. Moltiplicazione")
print ("4. Divisione")

scelta = int(input())

print("Inserisci il primo valore")
valore1 = int(input())
print("Inserisci il secondo valore")
valore2 = int(input())

risultato=0
if scelta==1:
    risultato=somma(valore1,valore2)
elif scelta == 2:
        risultato= sottrazione(valore1,valore2)
elif scelta==3:
        risultato= moltiplicazione(valore1,valore2)
elif scelta==4:
            risultato= divisione(valore1,valore2)
else: risultato ="risultato non valido"
print (f"il risultato è {risultato} ")


     