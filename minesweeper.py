# OBS: Esse jogo só funciona no Linux

# - : Um campo revelado que não tem nenhuma bomba adjacente.
# 1, 2, ... : Campos onde tem o número correspondente de bombas adjacentes.
# # : Campo ainda não revelado.
# X : Bomba

from os import system
from telnetlib import GA
import numpy as np

arquivo_csv = open("./maps/facil.csv", "r")
GABARITO = np.loadtxt(arquivo_csv, delimiter=",", dtype="str")

JOGO = np.full(GABARITO.shape, fill_value="#", dtype="str")

def solicita_input():
    input_coluna = int(input("Informe o número da coluna: "))
    while input_coluna < 0 or input_coluna > len(GABARITO):
        input_coluna = int(input("Informe o número da coluna: "))
 
    input_linha = int(input("Informe o número da linha: "))
    while input_linha < 0 or input_linha > len(GABARITO):
        input_linha = int(input("Informe o número da linha: "))

    return input_coluna, input_linha

def mostra_campo_minado(campo_minado):
    for linha in campo_minado:
        print("|", end=" ")
        for coluna in linha:
            print(coluna, sep=" ", end=" | ")
        print() # Para pular uma linha do Terminal após cada linha

def revela_campos_adjacentes(coluna, linha):
    range_campos = [-1, 0, 1] # Valores para revelar os campos adjacentes
    for i in range_campos:
        for j in range_campos:
            if linha + i >= 0 and coluna + j >= 0 and linha + i <= len(GABARITO) and coluna + j <= len(GABARITO): # Limita para que não de indices negativos ou ultrapasse o tamanho do Array
                if GABARITO[linha + i][coluna + j] != "X":
                    JOGO[linha + i][coluna + j] = GABARITO[linha + i][coluna + j]

def game_over(score):
    system("cls||clear") # Executa ou o cls (Windows) ou o clear (Linux)
    print("Você perdeu :(")
    print("Sua pontuação final foi: ", score)
    print("\nVeja aonde estavam todas as bombas: ")
    mostra_campo_minado(GABARITO)

def jogo():
    is_playing = True
    score = 0

    while is_playing:
        system("cls||clear") # Para limpar o terminal 
        print("Pontuação: ", score)
        mostra_campo_minado(JOGO)

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