# Kombinování řetězců pomocí interpolace
# Interpolace je způsob, jakým můžeme do řetězce vložit hodnoty proměnných.
# Interpolace se provádí pomocí znaku f a složených závorek {}. Do složených závorek se vloží název proměnné, kterou chceme vložit do řetězce.
# Interpolace se používá v Pythonu 3.6 a vyšších verzích.
# Interpolace se provádí pomocí f-strings, což je způsob, jakým můžeme do řetězce vložit hodnoty proměnných.

jmeno = "Karel"
prijmeni = "Novák"
zprava = f"Jeho příjmení je {prijmeni}."
print(zprava) #výstup celého jména

# Pouužití interpolace řetězců s více proměnnými
celeJmeno = f"{jmeno} {prijmeni}"
print(celeJmeno) #výstup celého jména
print(f"Celé jméno je {jmeno} {prijmeni}.") #výstup celého jména