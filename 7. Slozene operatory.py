#Složené operátory
# Složené operátory jsou zjednodušené zápisy pro provádění aritmetických operací a přiřazení hodnoty proměnné.
# Složené operátory se používají pro zjednodušení zápisu a zlepšení čitelnosti kódu.
# Složené operátory se používají pro provádění aritmetických operací a přiřazení hodnoty proměnné v jednom kroku.

# Při sčítání nazýváme proces "inkrementace".
x = 5
x += 3  # Ekvivalentní: x = x + 3
print(x)  # Výstup: 8

# Pri odčítání nazýváme proces "dekrementace".
x = 5
x -= 2  # Ekvivalentní: x = x - 2
print(x)  # Výstup: 3

# Při násobení používáme operátor *=.
x = 4
x *= 2  # Ekvivalentní: x = x * 2
print(x)  # Výstup: 8

# Při dělení používáme operátor /=.
x = 10
x /= 2  # Ekvivalentní: x = x / 2
print(x)  # Výstup: 5.0

# Při celočíselném dělení používáme operátor //=.
x = 10
x //= 3  # Ekvivalentní: x = x // 3
print(x)  # Výstup: 3

# Při zbytku po dělení používáme operátor %=.
x = 10
x %= 3  # Ekvivalentní: x = x % 3
print(x)  # Výstup: 1

# Při mocnině používáme operátor **=.
x = 3
x **= 2  # Ekvivalentní: x = x ** 2
print(x)  # Výstup: 9

x = 5
x +=1 # Ekvivalentní: x = x + 1
print (f"prvni interpolace {x}") #výstup 6
x +=1
print (f"druha interpolace {x}") #výstup 7
x +=1
print (f"treti interpolace {x}") #výstup 8


# Následující variata, nebude fungovat, protože += není platný operátor pro interpolaci. Není to jako v jazkyce C.
# print(f"{+=cislo3}") #výstup 2