### Aitor Palma ### ###---### ### Iker Jimenez ###
### 22/02/2024 ### ###---### ### Paraules Boges ###

import re

def paraulesBoges(frase):
    paraules = re.findall(r'\b\w+\b', frase)
    for paraula in paraules:
        if len(paraula) > 2:
            paraulaBoga = paraula[0] + paraula[1:-1][::-1] + paraula[-1]
            frase = frase.replace(paraula, paraulaBoga)
    return frase

frase = input("Introdueix una frase: ")

print(paraulesBoges(frase))


