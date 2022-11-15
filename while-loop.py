# Repetir un bloque de código hasta que una condición sea falsa
# El diferencial es que no siempre sabemos realmente cuándo va a acabar

"""
count = 10

while count < 10: # En algún momento esto sea falso y rompa el ciclo
    print(count)
    count += 1 # Va aumentando
"""

import random # Biblioteca Random 

number = random.randint(1, 10)

isCorrect = False # Inicialización

while isCorrect != True: # Mientras que no adivine se sigue preguntando
    adivina = int(input("Ingresa un número: "))
    
    if number == adivina:
        print("Felicidades, ganaste")
        isCorrect = True
    else:
        print("Sigue intentando")
