import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula a hipotenusa diretamente
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa mede: {hipotenusa:.2f}")

#Sem utilizar a biblioteca math
# Lê o comprimento do cateto oposto
#cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
# Lê o comprimento do cateto adjacente
#cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
# Calcula a hipotenusa usando o Teorema de Pitágoras
#hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
# Mostra o resultado
#print(f"A hipotenusa mede: {hipotenusa:.2f}")