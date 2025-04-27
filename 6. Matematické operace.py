# Provádění matematických operací
# Sčítání: +
# Odčítání: -
# Násobení: *
# Dělení: /
# Celočíselné dělení: //
# Zbytek po dělení: %
# Mocnina: **

prvniCislo = 20
druheCislo = 10
tretimCislo = 3

print (f"{prvniCislo} + {druheCislo} = ",prvniCislo + druheCislo) #výstup součtu čísel
print (f"{prvniCislo} - {druheCislo} = ",prvniCislo - druheCislo) #výstup rozdílu čísel
print (f"{prvniCislo} * {druheCislo} = ",prvniCislo * druheCislo) #výstup součinu čísel
print (f"{prvniCislo} / {druheCislo} = ",prvniCislo / druheCislo) #výstup podílu čísel
print (f"{prvniCislo} // {tretimCislo} = ",prvniCislo // tretimCislo) #výstup celočíselného podílu čísel
print (f"{prvniCislo} % {tretimCislo} = ",prvniCislo % tretimCislo) #výstup zbytku po dělení čísel
print (f"{druheCislo} ** {tretimCislo} = ",druheCislo ** tretimCislo) #výstup mocniny čísel

# Pro složitější výpočty můžeme použít modul math
import math
print(math.sqrt(16)) #výstup odmocniny z 16

celeCislo = 7
desetinneCislo = 3.5
print(celeCislo / desetinneCislo) #výstup součtu celého a desetinného čísla
print(desetinneCislo / celeCislo) #výstup součtu celého a desetinného čísla

# Pořadí operací
# 1. závorky ()
# 2. mocniny
# 3. násobení a dělení
# 4. sčítání a odčítání
# 5. zbytek po dělení
# 6. celočíselné dělení

vypocet1 = 2 + 3 * 4 #výstup 14
print(vypocet1) #výstup 14
vypocet2 = (2 + 3) * 4 #výstup 20
print(vypocet2) #výstup 20
vypocet3 = 2 + 3 * 4 - 5 #výstup 9
print(vypocet3) #výstup 9
vypocet4 = 2 + 3 * (4 - 5) #výstup -1
print(vypocet4) #výstup -1

# Zaokrouhlení čísel
# Zaokrouhlení pomocí funkce round() se používá k zaokrouhlení čísla na celé číslo nebo na určité desetinné místo.
# Pokud je číslo přesně uprostřed mezi dvěma celými čísly, zaokroulí se na nejbližší sudé číslo.
# Například: 2.5 se zaokrouhlí na 2, 3.5 se zaokrouhlí na 4, 4.5 se zaokrouhlí na 4, 5.5 se zaokrouhlí na 6.
print("Zaokrouhlední čísla 3.5 na celé číslo: ", round(3.5)) #výstup zaokrouhlení čísla 3.5 na celé číslo
print("Zaokrouhlední čísla 2.5 na celé číslo: ", round(2.5)) #výstup zaokrouhlení čísla 2.5 na celé číslo
print("Zaokrouhlední čísla 3.14159 na 2 desetinná místa: ", round(3.14159, 2)) #výstup zaokrouhlení čísla 3.14159 na 2 desetinná místa
# Zaokrouhlení pomocí funkce math.ceil() se používá k zaokrouhlení čísla na nejbližší celé číslo směrem nahoru.
print("Zaokrouhlední čísla 3.5 na celé číslo směrem nahoru: ", math.ceil(2.3)) #výstup zaokrouhlení čísla 2.3 na celé číslo směrem nahoru
# Zaokrouhlení pomocí funkce math.floor() se používá k zaokrouhlení čísla na nejbližší celé číslo směrem dolů.
print("Zaokrouhlední čísla 3.5 na celé číslo směrem dolů: ", math.floor(3.5)) #výstup zaokrouhlení čísla 3.5 na celé číslo směrem dolů
