# - : Um campo revelado que não tem nenhuma bomba adjacente.
# 1, 2, ... : Campos onde tem o número correspondente de bombas adjacentes.
# # : Campo ainda não revelado.
# X : Bomba

# TODO:
# - Tela de Vitória

from os import system
import numpy as np

arquivo_csv = open("./maps/facil.csv", "r")
GABARITO = np.loadtxt(arquivo_csv, delimiter=",", dtype="str")
tamanho_x, tamanho_y = GABARITO.shape
JOGO = np.full(GABARITO.shape, fill_value="#", dtype="str")

def solicita_input():
    input_coluna = int(input("Informe o número da coluna: "))
    while input_coluna < 0 or input_coluna > tamanho_y:
        input_coluna = int(input("Informe o número da coluna: "))

    input_linha = int(input("Informe o número da linha: "))
    while input_linha < 0 or input_linha > tamanho_x:
        input_linha = int(input("Informe o número da linha: "))

    return input_coluna, input_linha

def define_dificuldade(): # TODO: Terminar essa função
    arquivo_csv = open("./maps/facil.csv", "r")
    GABARITO = np.loadtxt(arquivo_csv, delimiter=",", dtype="str")
    tamanho_x, tamanho_y = GABARITO.shape
    JOGO = np.full(GABARITO.shape, fill_value="#", dtype="str")

def mostra_campo_minado(campo_minado):
    x, y = campo_minado.shape

    espacamento = "     " # Espaçamento de 5 espaços
    
    y_string = "   " # Espaçamentos para o eixo Y
    for y_index in range(y):
        y_string = y_string + espacamento + str(y_index)
    print(y_string)

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

def revela_campos_adjacentes(linha, coluna):
    range_campos = [-1, 0, 1] # Valores para revelar os campos adjacentes

    for i in range_campos:
        linha_atual = linha + i
        for j in range_campos:
            coluna_atual = coluna + j

            if linha_atual >= 0 and coluna_atual >= 0 and linha_atual < tamanho_x and coluna_atual < tamanho_y: # Limite para que não ocorra indices negativos ou ultrapasse o tamanho do Array
                if GABARITO[linha_atual][coluna_atual] != "X":
                    JOGO[linha_atual][coluna_atual] = GABARITO[linha_atual][coluna_atual]

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

def game_over(score):
    system("cls||clear") # Executa ou o cls (Windows) ou o clear (Linux)
    print("\t\tVocê perdeu :(\n")
    print("- Sua pontuação final foi: ", score)
    print("\nVeja aonde estavam todas as bombas: \n")
    mostra_campo_minado(GABARITO)

def jogo():
    is_playing = menu_principal()
    max_score 
    score = 0

    while is_playing:
        system("cls||clear") # Para limpar o terminal
        print("\t\tCampo Minado\n")
        print("- Pontuação: ", score)
        print() # Para pular uma linha no terminal
        mostra_campo_minado(JOGO)
        print() # Para pular uma linha no terminal

        coluna, linha = solicita_input()
        valor_escolhido = GABARITO[linha][coluna]

        while JOGO[linha][coluna] == GABARITO[linha][coluna]:
            if JOGO[linha][coluna] == GABARITO[linha][coluna]:
                print("Campo já foi encontrado! Por favor, selecione outro...")

                coluna, linha = solicita_input()
                valor_escolhido = GABARITO[linha][coluna]

        if valor_escolhido == "X":
            is_playing = False
            game_over(score)

        elif valor_escolhido == "-":
            JOGO[linha][coluna] = valor_escolhido
            revela_campos_adjacentes(linha, coluna)
            score = score + 1

        elif int(valor_escolhido) > 0:
            JOGO[linha][coluna] = valor_escolhido
            score = score + 1

jogo()