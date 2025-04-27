# Kombinování řetězců pomocí zřetězení řetězců
# Zřetězení pomocí operátoru + a * (opakování)
zbozi = "Auto"
pismeno = "A"
zprava = 3*pismeno + zbozi #zřetězení se dá použít i při přiřazení do proměnné
print("V dílně se opravovalo " + zbozi) #zřetězení pomocí operátoru +
print("Autobazar se jmenuje " + pismeno* 3 + " Auto.") #opakování pomocí operátoru * a zřetězení pomocí operátoru +
print("Firma" + pismeno* 3 + zbozi +".") #použití více proměnných v jednom příkazu
print(zprava) #výstup zprávy

# Zřetězení pomocí čárky, proměnné se nepíší do uvozovek, více proměnných se odděluje čárkou
print("V obchodě se prodávalo", zbozi, "třídy", pismeno, ".") #výstup zprávy chyba mezery před tečkou
# výstup zprávy bez mezery před tečkou
print("V obchodě se prodávalo", zbozi, "třídy", pismeno + ".") #výstup zprávy bez mezery před tečkou
