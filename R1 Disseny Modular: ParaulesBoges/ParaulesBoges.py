### Aitor Palma ### ###---### ### Iker Jimenez ###
### 22/02/2024 ### ###---### ### Paraules Boges ###

import re

def paraulesBoges(frase):
    paraules = re.findall(r'\b\w+\b', frase)
    fraseBoga = ""
    for paraula in paraules:
        if len(paraula) > 2:
            fraseBoga += paraula[0] + paraula[1:-1][::-1] + paraula[-1] + " "
        else:
            fraseBoga += paraula + " "
    return fraseBoga

frase = input("Posa una frase: ")

print(paraulesBoges(frase))


