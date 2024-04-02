"""2) Crie uma função que recebe uma palavra (string), separa todos os caracteres em uma lista, retorna esta lista e quantidade de letras."""

def separar_caracteres(palavra):
    lista_caracteres = list(palavra)
    quantidade_letras = len(lista_caracteres)
    return lista_caracteres, quantidade_letras

palavra_inserida = input("Digite uma palavra: ")

caracteres, qtd_letras = separar_caracteres(palavra_inserida)
print("Lista de caracteres:", caracteres)
print("Quantidade de letras:", qtd_letras)
