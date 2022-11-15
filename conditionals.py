estaLloviendo = False

#if estaLloviendo: # Solo va a ejecutar lo que contiene si al comparar o evaluar da un True
    #print("Entra la ropa")


# Ayudas de las comparaciones
#print(estaLloviendo != True) # Diferente de 
#print(not estaLloviendo == True) # Negación de la comparación

hayRopa = False

# AND: Las dos comparaciones son verdaderas = True, si al menos una es falsa = False
#print(estaLloviendo == True and hayRopa == True)

# OR: Al menos una de las comparaciones debe ser verdadera = True, Si las dos son falsas = False
#print(estaLloviendo == True or hayRopa == True)

"""
if estaLloviendo and hayRopa: # equ estaLloviendo == True and hayRopa == True
    print("Entra la ropa")
elif estaLloviendo:
    print("Abrigate")
elif hayRopa:
    print("Revisa que nada se haya caido")
else:
    print("Sigue en lo tuyo")
"""

userReply = input("Qué tipo de paquete va a enviar: (sobre, caja o bolsa)")

if userReply == "sobre":
    print("Recuerda usar un sobre que no esté deteriorado")
elif userReply == "caja":
    print("No se puede exceder de tal dimensión")
elif userReply == "bolsa":
    print("Revise que no esté rota")
else:
    print("Por favor coloque un paquete valido")