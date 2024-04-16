# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 27
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
     print("Numarul este pozitiv")
else : 
     print("Numarul nu este negativ sau egal cu zero")
   # CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
     print("Numarul este par")
else : 
     print("Numarul nu este par")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if not number % 2 == 0:
     print("Numarul este impar")
else : 
     print("Numarul nu este impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
txt = '''There are not too many differences between the spectra of different samples.\n 
However, there are some variations of the intensity of some peaks.'''
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in txt:
     print("Textul contine cuvantul \"Python\"")
else:
     print("Textul nu contine cuvantul cautat")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in txt:
     print("Textul contine cuvantul \"Java\"")
else:
     print("Textul nu contine cuvantul cautat")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in txt:
     print("Textul contine cuvantul \"Python\"")
elif "Java" in txt:
     print("Textul nu contine cuvantul Python, dar contine cuvantul \"Java\"")
else: print("Textul nu contine niciun cuvant din cele cautate") 
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in txt and "Java" in txt:
     print("Textul contine cuvantele \"Python\" si \"Java\"")
elif "Python" in txt or "Java" in txt:
     print("Textul contine un cuvant din cele cautate")
else: 
     print("Textul nu contine niciun cuvant din cele cautate")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = int(input("Scrieti un numar de la 1 la 5: "))
if number == 1:
     print("Unu")
elif number == 2:
     print("Doi")
elif number == 3:
     print("Trei")
elif number == 4:
     print("Patru")
else: print("Cinci")  
# CODUL TĂU VINE MAI SUS:


