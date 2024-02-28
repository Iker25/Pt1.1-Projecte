### Aitor Palma ### ###---### ### Iker Jimenez ###
### 22/02/2024 ### ###---### ### Paraules Boges ###

import re

def invertirParaula(paraula):
    return paraula[0] + paraula[1:-1][::-1] + paraula[-1]

def substituirParaula(frase, paraula, paraulaBoga):
    return frase.replace(paraula, paraulaBoga)

def paraulesBoges(frase):
    paraules = re.findall(r'\b\w+\b', frase)
    for paraula in paraules:
        if len(paraula) > 2:
            paraulaBoga = invertirParaula(paraula)
            frase = substituirParaula(frase, paraula, paraulaBoga)
    return frase

frase = input("Posa una frase: ")
print(paraulesBoges(frase))


