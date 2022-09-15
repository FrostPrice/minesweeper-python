from os import system
import numpy as np

def solicita_input(gabarito_shape):
    tamanho_x, tamanho_y = gabarito_shape

    input_coluna = int(input("Informe o número da coluna: "))
    while input_coluna < 0 or input_coluna >= tamanho_y or input_coluna == "":
        input_coluna = int(input("Informe o número da coluna: "))

    input_linha = int(input("Informe o número da linha: "))
    while input_linha < 0 or input_linha >= tamanho_x or input_linha == "":
        input_linha = int(input("Informe o número da linha: "))

    return input_coluna, input_linha

def define_dificuldade():
    print("+--------------------------------------------------------------+")
    print("|                                                              |")
    print("|                   Selecione a dificuldade                    |")
    print("|                                                              |")
    print("| 1 - Fácil (5x8)                                              |")
    print("| 2 - Médio (10x12)                                            |")
    print("| 2 - Difícil (Boa Sorte ;) )                                  |")
    print("+--------------------------------------------------------------+\n")
    input_dificuldade = int(input("Informe o nível que você quer jogar [1-3]: "))
    while input_dificuldade < 1 or input_dificuldade > 3:
        input_dificuldade = int(input("Informe o nível que você quer jogar [1-3]: "))

    if input_dificuldade == 1:
        nome_arquivo = "facil"
    elif input_dificuldade == 2:
        nome_arquivo = "medio"
    else:
        nome_arquivo = "dificil"

    caminho_arquivo = "./maps/{}.csv".format(nome_arquivo)

    arquivo_csv = open(caminho_arquivo, "r")
    gabarito = np.loadtxt(arquivo_csv, delimiter=",", dtype="str")
    jogo = np.full(gabarito.shape, fill_value="#", dtype="str")

    counter = 0
    for linha in gabarito:
        for coluna in linha:
            if coluna != "X":
                counter = counter + 1

    return counter, gabarito, jogo

def mostra_campo_minado(campo_minado):
    x, y = campo_minado.shape

    espacamento = "     " # Espaçamento de 5 espaços
    
    y_string = "   " # Espaçamentos para as colunas
    for y_index in range(y):
        y_string = y_string + espacamento + str(y_index)
    print(y_string)

    # Os loops abaixo são usados para perfumaria do Campo Minado
    for linha in range(x):
        string = "     "
        if linha == 0:
            for coluna in range(y):
                string = string + "______" 
            print(string)
 
        string = "     "
        for coluna in range(y):
            string = string + "|     "
        print(string + "|")
         
        string = "  " + str(linha) + "  "
        for coluna in range(y):
            string = string + "|  " + campo_minado[linha][coluna] + "  "
        print(string + "|") 
 
        string = "     "
        for coluna in range(y):
            string = string + "|_____"
        print(string + '|')

def revela_campos_adjacentes(linha, coluna, gabarito, jogo):
    tamanho_x, tamanho_y = gabarito.shape
    range_campos = [-1, 0, 1] # Valores para revelar os campos adjacentes

    score_campos_adjacentes = 0
    for i in range_campos:
        linha_atual = linha + i
        for j in range_campos:
            coluna_atual = coluna + j

            if linha_atual >= 0 and coluna_atual >= 0 and linha_atual < tamanho_x and coluna_atual < tamanho_y: # Limite para que não ocorra indices negativos ou ultrapasse o tamanho do Array
                if gabarito[linha_atual][coluna_atual] != "X" and jogo[linha_atual][coluna_atual] == "#": # Se o espaço não for uma bomba e não foi descoberto ainda
                    jogo[linha_atual][coluna_atual] = gabarito[linha_atual][coluna_atual]
                    score_campos_adjacentes = score_campos_adjacentes + 1

    return score_campos_adjacentes

def menu_principal():
    print("+--------------------------------------------------------------+")
    print("|                                                              |")
    print("|                        Campo Minado                          |")
    print("|                                                              |")
    print("| 1 - Começar o Jogo                                           |")
    print("| 2 - Sair do Jogo                                             |")
    print("+--------------------------------------------------------------+\n")

    input_usuario = int(input("Escolha [1-2]: "))
    while input_usuario < 1 or input_usuario > 2:
        input_usuario = int(input("Escolha [1-2]: "))

    if input_usuario == 1:
        return True
    else:
        return False

def vitoria(score, campo_minado):
    system("cls||clear")
    print("\t\tParabéns você Ganhou!!!\n")
    print("- Sua pontuação final foi: ", score)
    print()
    mostra_campo_minado(campo_minado)

def game_over(score, gabarito):
    system("cls||clear") # Executa ou o cls (Windows) ou o clear (Linux)
    print("\t\tVocê perdeu :(\n")
    print("- Sua pontuação final foi: ", score)
    print("\nVeja aonde estavam todas as bombas: \n")
    mostra_campo_minado(gabarito)

def jogo():
    score = 0
    is_playing = menu_principal()

    if(is_playing):
        max_score, GABARITO, JOGO = define_dificuldade()

    while is_playing:
        if score == max_score:
            vitoria(score, JOGO)
            break

        system("cls||clear") # Para limpar o terminal
        print("\t\tCampo Minado\n")
        print("- Pontuação: ", score)
        print() # Para pular uma linha no terminal
        mostra_campo_minado(JOGO)
        print() # Para pular uma linha no terminal

        coluna, linha = solicita_input(GABARITO.shape)
        valor_escolhido = GABARITO[linha][coluna]

        while JOGO[linha][coluna] == GABARITO[linha][coluna]:
            if JOGO[linha][coluna] == GABARITO[linha][coluna]:
                print("Campo já foi encontrado! Por favor, selecione outro...")

                coluna, linha = solicita_input(GABARITO.shape)
                valor_escolhido = GABARITO[linha][coluna]

        if valor_escolhido == "X":
            is_playing = False
            game_over(score, GABARITO)

        elif valor_escolhido == "-":
            score = score + revela_campos_adjacentes(linha, coluna, GABARITO, JOGO)

        elif int(valor_escolhido) > 0:
            JOGO[linha][coluna] = valor_escolhido
            score = score + 1

jogo()