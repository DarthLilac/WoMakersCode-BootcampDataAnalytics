"""6) Um jogador de um jogo de vídeo game deseja subir de nível em seu personagem ao atingir 50 inimigos derrotados. Enquanto esse número não é alcançado, uma mensagem indicando quantos inimigos ainda faltam é exibida na tela."""

inimigos_derrotados = 0
nivel = 0

while inimigos_derrotados < 50:
    print(f"Faltam {50 - inimigos_derrotados} inimigos para você mudar de nível!")

    inimigos_derrotados += 10

    if inimigos_derrotados >= 50:
        print("\nVocê atingiu o próximo nível!")
        nivel = 1
