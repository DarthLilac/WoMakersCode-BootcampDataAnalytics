"""1 ) Para determinar se um candidato está qualificado para uma vaga de emprego, são aplicados dois critérios:

a) O candidato deve ter uma presença igual ou superior a 60% em um treinamento obrigatório.

b) O candidato deve ter uma média de desempenho igual ou superior a 7 em uma série de testes.

Para auxiliar na avaliação dos candidatos, você deve criar uma função que recebe uma lista de dicionários contendo o nome do candidato, a média de desempenho e a quantidade de horas de ausência do treinamento. Com esses dados, a função deve calcular se o candidato está qualificado ou não. A presença do candidato é calculada considerando que o treinamento teve um total de 60 horas e utilizando a fórmula:

(Total horas - número de faltas)/Total horas * 100;"""

def avaliar_candidatos(candidatos):
    for candidato in candidatos:
        presenca = ((60 - candidato['horas_ausentes']) / 60) * 100
        if presenca >= 60 and candidato['media_desempenho'] >= 7:
            print(f"{candidato['nome']} está qualificado(a) para a vaga.")
        else:
            print(f"{candidato['nome']} não está qualificado(a) para a vaga.")

lista_candidatos = [
    {'nome': 'Sofia', 'media_desempenho': 8, 'horas_ausentes': 10},
    {'nome': 'Luisa', 'media_desempenho': 6, 'horas_ausentes': 5},
    {'nome': 'Marina', 'media_desempenho': 7, 'horas_ausentes': 20},
    {'nome': 'Heitor', 'media_desempenho': 10, 'horas_ausentes': 30}
]

avaliar_candidatos(lista_candidatos)
