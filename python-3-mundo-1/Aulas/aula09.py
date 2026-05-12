# AULA 09
# Objetivo: estudar manipulacao de strings em Python.
# Nesta aula aparecem indices, fatiamento, metodos de texto e strings multilinha.

# Cria uma variavel chamada frase e guarda nela um texto.
# Repare que existem dois espacos antes da palavra Curso.
# Esses espacos tambem fazem parte da string e contam como caracteres.
frase = '  Curso em Video Python'

# Mostra o caractere que esta no indice 3 da string.
# Em Python, a contagem dos indices comeca em 0.
# Como a frase tem dois espacos no inicio, o indice 3 aponta para a letra 'u'.
print(frase[3])

# Mostra um pedaco da string, indo do indice 3 ate o indice 12.
# O indice final 13 nao entra no resultado.
print(frase[3:13])

# Mostra a string desde o inicio ate o indice 12.
# Quando o inicio e omitido, o Python considera que comeca no indice 0.
print(frase[:13])

# Mostra a string do indice 13 ate o final.
# Quando o fim e omitido, o Python considera que vai ate o ultimo caractere.
print(frase[13:])

# Mostra a string do indice 1 ate o indice 14.
# O indice final 15 nao entra no resultado.
print(frase[1:15])

# Mostra a string do indice 1 ate o indice 14, pulando de 2 em 2 caracteres.
# A terceira informacao do fatiamento e o passo.
print(frase[1:15:2])

# Mostra a string do indice 1 ate o final, pulando de 2 em 2 caracteres.
# Como o fim foi omitido, o Python percorre ate o ultimo caractere.
print(frase[1::2])

# Mostra a string inteira, pulando de 2 em 2 caracteres.
# Como inicio e fim foram omitidos, o Python usa a string completa.
print(frase[::2])

# count('o') conta quantas vezes a letra minuscula 'o' aparece na string.
# Letras maiusculas e minusculas sao consideradas diferentes.
print(frase.count('o'))

# count('O') conta quantas vezes a letra maiuscula 'O' aparece na string.
# Se nao existir 'O' maiusculo, o resultado sera 0.
print(frase.count('O'))

# upper() cria uma versao da string toda em letras maiusculas.
# Depois disso, count('O') conta quantas letras 'O' existem nessa versao maiuscula.
print(frase.upper().count('O'))

# lower() cria uma versao da string toda em letras minusculas.
# Esse metodo e util quando queremos padronizar um texto antes de comparar ou exibir.
print(frase.lower())

# len() retorna o tamanho total da string.
# Os dois espacos no inicio tambem entram nessa contagem.
print(len(frase))

# strip() cria uma versao da string sem espacos no inicio e no fim.
# len() conta o tamanho dessa nova versao sem os espacos externos.
print(len(frase.strip()))

# replace() cria uma nova string trocando 'Python' por 'Android'.
# A variavel frase original nao e alterada, porque strings sao imutaveis.
print(frase.replace('Python', 'Android'))

# O operador in verifica se a palavra 'Curso' existe dentro da string.
# O resultado sera True se existir e False se nao existir.
print('Curso' in frase)

# find() procura a posicao onde a palavra 'Curso' comeca.
# Se encontrar, retorna o indice inicial; se nao encontrar, retorna -1.
print(frase.find('Curso'))

# split() separa a string em partes usando os espacos como divisores.
# O resultado e uma lista com as palavras encontradas.
dividido = frase.split()

# Mostra o item de indice 2 da lista dividido.
# Depois do split(), a lista fica: ['Curso', 'em', 'Video', 'Python'].
print(dividido[2])

# Mostra o item de indice 0 da lista dividido.
# O indice 0 representa o primeiro item da lista.
print(dividido[0])

# Primeiro, dividido[2] acessa o terceiro item da lista, que e a palavra 'Video'.
# Depois, [3] acessa o caractere de indice 3 dentro da palavra 'Video'.
# Como a contagem comeca em 0, dividido[2][3] mostra a letra 'e'.
print(dividido[2][3])

# Tres aspas permitem criar uma string com varias linhas.
# Aqui, print() mostra um texto longo exatamente como foi escrito entre as aspas.
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")
