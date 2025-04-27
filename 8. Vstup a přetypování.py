# Vnější vstup se v Pythonu provádí pomocí funkce input().
# Funkce input() přečte vstup od uživatele a vrátí ho jako řetězec. 
# Pokud chceme přečíst číslo, musíme ho převést na číslo pomocí funkce int() nebo float(). Tomutu se říká přetypování.

jmeno = input("Zadej jméno: ") #vstup jména
print("Tvoje jméno je: ", jmeno) #výstup jména

cislo = int(input("Zadej číslo: ")) #vstup čísla
cislo += 1 #přičtení 1 k číslu
print("Tvoje číslo je: ", cislo) #výstup čísla

# Přetypování čísel
# Přetypování čísel se provádí pomocí funkcí int(), float() a str().
# int() - převede číslo na celé číslo
# float() - převede číslo na desetinné číslo
# str() - převede číslo na řetězec
# pomocí funkce type() zjistíme typ proměnné

# Převod na celé číslo
num_str = "42"
num_int = int(num_str)
print(num_int)  # Výstup: 42
print(type(num_int))  # Výstup: <class 'int'>

# Převod na float
num = 10
num_float = float(num)
print(num_float)  # Výstup: 10.0

# Převod na řetězec
num = 123
num_str = str(num)
print(num_str)  # Výstup: "123"
print(type(num_str))  # Výstup: <class 'str'>

