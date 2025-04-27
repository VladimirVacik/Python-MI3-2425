# Řídící sekvence znaků pomocí znaku \ se používají pro speciální znaky, které nemůžeme napsat přímo do textu, nebo pro úpravu textu
# například:
# \ - zpětné lomítko, které říká, že následující znak má speciální význam, dá se použít na konci řádku pro pokračování na dalším řádku
# \n - nový řádek
# \t - tabulátor
# \\ - zpětné lomítko
# \' - apostrof
# \" - uvozovky
# \r - návrat na začátek řádku
# \( - levá závorka

print ("Ahoj Karle") #ukázka výstupu
print ("Ahoj\nKarle") #ukázka nového řádku
print ("Ahoj\tKarle") #ukázka tabulátoru
print ("Ahoj \"Karle\"!") #ukázka uvozovek
print ("C:\\Github\\Python") #ukázka zpětného lomítka

#Formátování výstupu pomocí řídících znaků
print("Generating invoices for customer \"Contoso Corp\" ... \n");
print("Invoice: 1021\t\tComplete!");
print("Invoice: 1022\t\tComplete!");
print("\nOutput Directory:\t");

#Doslovný řetězec
#Doslovný řetězec zachovává všechny mezery a znaky bez nutnosti použít řídicí znak (zpětné lomítko).
#Pro použití doslovného řetězce použijeme znak "r" před uvozovkami.
print(r"    C:\souerce\repos\
      (sem patří tvůj kod)")

#Řídicí znaky Unicode
#Pomocí Unicode můžeme použít znaky, které nejsou na klávesnici.
#Například: ©, ™, ®, €, £, ¥, ¢, §, ¶, ÷, ±, µ, ∞, ∑, ∏, ∫, ∆, √
#Unicode znaky začínají znakem "\u" a za ním následuje čtyřmístné hexadecimální číslo.

print("\u3053\u3093\u306b\u3061\u306f World") #výstup Kon'nichiwa World
# Řídící sekvence znaků pomocí znaku \ se používají pro speciální znaky, které nemůžeme napsat přímo do textu, nebo pro úpravu textu
# například:
# \ - zpětné lomítko, které říká, že následující znak má speciální význam, dá se použít na konci řádku pro pokračování na dalším řádku
# \n - nový řádek
# \t - tabulátor
# \\ - zpětné lomítko
# \' - apostrof
# \" - uvozovky
# \r - návrat na začátek řádku
# \( - levá závorka

print ("Hello World") #ukázka výstupu
print ("Hello\nWorld") #ukázka nového řádku
print ("Hello\tWorld") #ukázka tabulátoru
print ("Hello \"World\"!") #ukázka uvozovek
print ("C:\\source\\repos") #ukázka zpětného lomítka

#Formátování výstupu pomocí řídících znaků
print("Generating invoices for customer \"Contoso Corp\" ... \n");
print("Invoice: 1021\t\tComplete!");
print("Invoice: 1022\t\tComplete!");
print("\nOutput Directory:\t");

#Doslovný řetězec
#Doslovný řetězec zachovává všechny mezery a znaky bez nutnosti použít řídicí znak (zpětné lomítko).
#Pro použití doslovného řetězce použijeme znak "r" před uvozovkami.
print(r"    C:\souerce\repos\
      (sem patří tvůj kod)")

#Řídicí znaky Unicode
#Pomocí Unicode můžeme použít znaky, které nejsou na klávesnici.
#Například: ©, ™, ®, €, £, ¥, ¢, §, ¶, ÷, ±, µ, ∞, ∑, ∏, ∫, ∆, √
#Unicode znaky začínají znakem "\u" a za ním následuje čtyřmístné hexadecimální číslo.

print("\u3053\u3093\u306b\u3061\u306f World") #výstup Kon'nichiwa World