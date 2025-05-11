# Kombinování řetězců pomocí řídicích sekvencí znaků
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
print("Analýzy prospěchu žáků ... \n");
print("Třída: IT1A\t\tHotovo");
print("Třída: IT2B\t\tHotovo");
print("\nAnalýza je uložena ve složce:\t");

#Doslovný řetězec
#Doslovný řetězec zachovává všechny mezery a znaky bez nutnosti použít řídicí znak (zpětné lomítko).
#Pro použití doslovného řetězce použijeme znak "r" před uvozovkami. Ten neumožňuje použití Enteru pro nový řádek, jako u jiných programovacích jazyků.
print(r"    C:\users\Karel\Dokumenty\Analýzy\
      (sem patří tvůj kod)")

#Pro použití doslovného řetězce použijeme znak tři uvozovky místo jednich """. Ten umožňuje použití Enteru pro nový řádek.
print(r"""C:\users\Karel\Dokumenty\Analýzy\
      (sem patří tvůj kod)""")

#Řídicí znaky Unicode
#Pomocí Unicode můžeme použít znaky, které nejsou na klávesnici.
#Například: ©, ™, ®, €, £, ¥, ¢, §, ¶, ÷, ±, µ, ∞, ∑, ∏, ∫, ∆, √
#Unicode znaky začínají znakem "\u" a za ním následuje čtyřmístné hexadecimální číslo.

print("Tři japonské opice:\nMizaru - \u307F\u3056\u308B\nKikazaru - \u304D\u304B\u3056\u308B\nIwazaru - \u3044\u308F\u3056\u308B") #výstup Japonské opice: Mizaru (nevidím zlo), Kikazaru (vidím zlo), Iwanaga (zlo)
