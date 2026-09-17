import aroeira as ar
import random as rd
import player as p1

class Pixel:
    def __init__(self, origem: ar.Ponto, cor: str, colisao: bool, tipo):
        self.shape: ar.Retangulo = ar.Retangulo(
            altura= 50, 
            largura= 50,
            origem= origem,
            cor= cor
        )
        self.colisao = colisao
        self.tipo = tipo

roomLayout = [[
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [4, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
],[
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [4, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
],[
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 1],
    [4, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 2, 0, 4],
    [1, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
],[
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [4, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
]]

extras: list[Pixel] = []
renderizado: list[Pixel] = []
salas = {}
colunas = 0
linhas = 0

def drawRoom(roomMatrix, tela):
    global renderizado, extras
    renderizado = []
    extras = []
    for i, linha in enumerate(roomMatrix):
        for col, tipo in enumerate(linha):
            if tipo == 0:
                continue

            cores = {
                1: "marrom",
                2: "vermelho",
                3: "cinza",
                4: "verde",  
            }
            colisao = {
                1: True,
                2: True,
                3: False,
                4: True,
            }

            pixel = Pixel(
                origem=ar.Ponto(col * 50, i * 50),
                cor=cores[tipo],
                colisao=colisao[tipo],
                tipo=tipo
            )

            if pixel.colisao:
                renderizado.append(pixel)

            if pixel.tipo == 3:
                extras.append(pixel)

            tela.adicionar(pixel.shape)
    salas[f"{colunas},{linhas}"] = renderizado, extras

def change_room(dir, tela, player):
    global colunas, linhas, renderizado, extras
    remove_map(tela, player)
    if dir == "cima":
        linhas -= 1
    if dir == "baixo":
        linhas += 1
    if dir == "direita":
        colunas += 1
    if dir == "esquerda":
        colunas -= 1
          
    if f"{colunas},{linhas}" in salas:

        renderizado = salas[f"{colunas},{linhas}"][0]
        extras = salas[f"{colunas},{linhas}"][1]
        for i in range(len(renderizado)):
            tela.adicionar(renderizado[i].shape)

        for b in range(len(extras)):
            tela.adicionar(extras[b].shape)

    else:
        aleatorio = rd.randint(0,len(roomLayout)- 1)
        drawRoom(roomLayout[aleatorio], tela)
    tela.adicionar(player.shape)

def remove_map(tela, player):
    global renderizado, extras
    tela.remover(player.shape)
    for i in range(len(renderizado)):
        tela.remover(renderizado[i].shape)

    if len(extras) == 1:
        tela.remover(extras[0].shape)
    else:
        for b in range(len(extras)):
            tela.remover(extras[b].shape)