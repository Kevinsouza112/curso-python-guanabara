import math

angulo = int(input("Digite um angulo para saber o Seno, Cosseno e Tangente: "))

angulo_rad = math.radians(angulo)

print("O seno de {} é igual a {:.3f}".format(angulo, math.sin(angulo_rad)))
print("O cosseno de {} é igual a {:.3f}".format(angulo, math.cos(angulo_rad)))
print("A tangente de {} é igual a {:.3f}".format(angulo, math.tan(angulo_rad)))

