### Aitor Palma ### ###---### ### Iker Jimenez ###
### 22/02/2024 ### ###---### ### Paraules Boges ###


def paraulesBoges(frase):
    paraules = frase.split()
    fraseBoga = ""
    for paraula in paraules:
        if len(paraula) > 3:
            paraula = paraula[0] + paraula[1:-1][::-1] + paraula[-1]
        fraseBoga += paraula + " "
    return fraseBoga

frase = input("Frase: ")

print("Sortida:", paraulesBoges(frase))


