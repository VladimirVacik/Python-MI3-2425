print ("První výstup") #ukázka výstupu

#dynamické proměnné
vek = 25 #proměnná typu int - celé číslo
vyska = 175.5 #proměnná typu float - reálné číslo
vaha = 70.5 #proměnná typu float - reálné číslo
nadvaha = True #proměnná typu bool - logická hodnota místo true/false můžeme použít 1/0
jmeno = "Petr" #proměnná typu str - řetězec
bmi = None #deklarace proměnné bez inicializace, proměnná typu NoneType - žádná hodnota

bmi= vaha / ((vyska / 100) ** 2) #výpočet BMI
print (f"Jméno: {jmeno}, věk: {vek}, výška: {vyska}, váha: {vaha}, nadváha: {nadvaha}, BMI: {bmi}") #výstup pomocí f-stringu

#staticé proměnné pomocí hints
vek1: int = 25 #proměnná typu int - celé číslo
vyska1: float = 175.5 #proměnná typu float - reálné číslo
vaha1: float = 70.5 #proměnná typu float - reálné číslo
nadvaha1: bool = True #proměnná typu bool - logická hodnota místo true/false můžeme použít 1/0
jmeno1: str = "Petr" #proměnná typu str - řetězec
bmi1: float #proměnná typu float - reálné číslo jedná se o deklaraci bez inicializace
bmi1 = vaha1 / ((vyska1 / 100) ** 2) #výpočet BMI
print (bmi1) #výstup 