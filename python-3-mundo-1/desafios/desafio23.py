# Faca um programa que leia um numero de 0 a 9999 e mostre cada digito separado.
# Exemplo: 1834
# Unidade: 4, dezena: 3, centena: 8, milhar: 1

# Le o numero digitado e converte de texto para inteiro.
numero = int(input("Digite um numero de 0 a 9999: "))

# Pega o ultimo digito do numero, que representa a unidade.
unidade = numero // 1 % 10

# Remove a unidade com // 10 e pega o ultimo digito que sobra.
dezena = numero // 10 % 10

# Remove unidade e dezena com // 100 e pega o ultimo digito que sobra.
centena = numero // 100 % 10

# Remove unidade, dezena e centena com // 1000 e pega o ultimo digito que sobra.
milhar = numero // 1000 % 10

# Mostra cada casa numerica separadamente.
print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")
