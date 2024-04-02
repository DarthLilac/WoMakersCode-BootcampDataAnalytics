"""4) O chefe decidiu premiar os melhores funcionários de sua empresa com um brinde. Para isso ela vai entregar um brinde para todos os funcionários que tiverem uma performance superior a média da equipe.

Elabore uma função que recebe uma lista de nome em formato de dict (dicionário) com nome do funcionário e a média do funcionário (Valor de 0 a 10). Esta função deve calcular a média da equipe, 
identificar quais funcionários tem média igual ou superior a média da equipe e retornar uma lista com o nome dos funcionários que possuem média igual ou superior a média da equipe. 
A ordem dos nomes da lista de retorno deve ser em ordem decrescente."""

def premiar_melhores(funcionarios):
    medias = [funcionario['media'] for funcionario in funcionarios]
    media_equipe = sum(medias) / len(medias)

    melhores = [funcionario['nome'] for funcionario in funcionarios if funcionario['media'] >= media_equipe]

    melhores = sorted(melhores, key=lambda x: funcionarios[[f['nome'] for f in funcionarios].index(x)]['media'], reverse=True)

    return melhores


funcionarios = [
    {'nome': 'Isabela', 'media': 8},
    {'nome': 'Mario', 'media': 6},
    {'nome': 'Patricia', 'media': 7},
    {'nome': 'Felipe', 'media': 9},
    {'nome': 'Claudia', 'media': 5}
]

funcionarios_premiados = premiar_melhores(funcionarios)
print("Funcionários premiados:", funcionarios_premiados)
