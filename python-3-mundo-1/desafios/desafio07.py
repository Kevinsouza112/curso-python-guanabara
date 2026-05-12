# DESAFIO 07
# Objetivo: ler duas notas, calcular a media e mostrar o resultado.

# print() mostra um titulo simples para identificar o desafio no terminal.
print('===== DESAFIO 007 =====')

# input() recebe a primeira nota como texto.
# float() converte esse texto para numero decimal.
# A nota convertida fica guardada na variavel nt1.
nt1 = float(input('Digite uma nota: '))

# input() recebe a segunda nota como texto.
# float() converte esse texto para numero decimal.
# A nota convertida fica guardada na variavel nt2.
nt2 = float(input('Digite uma nota: '))

# Soma as duas notas e divide por 2 para calcular a media aritmetica.
media = (nt1 + nt2) / 2

# Mostra a media com uma casa decimal usando {:.1f}.
print('A media das notas e {:.1f}'.format(media))
