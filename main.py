import aroeira as ar
import mapa
import player as pl
import random as rd

velocidade = 5

tela = ar.Tela("Roguelike", 15*50, 9*50)


mapa.drawRoom(mapa.roomLayout[rd.randint(0,len(mapa.roomLayout)- 1)], tela)
player = pl.Player()

vidas = ar.Texto(ar.Ponto(50,50),f"Vidas: {player.health}", 16, 'preto')
tela.adicionar(vidas)

def colisao():
    for pixel in mapa.renderizado:
        if player.tocando(pixel):
            return True, pixel
        
    return False, pixel

teclas = set()

def pressionar(nome):
    teclas.add(nome.casefold())

    #Teste do dano
    if nome == "F":
        print(f"Localização do player: {mapa.colunas},{mapa.linhas}")
        print(mapa.extras)
        player.dano(vidas)

def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
    if "w" in teclas:
        player.shape.mover(dy=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y + bloco.shape.altura) - player.shape.y)

        if sit == True and bloco.tipo == 4:
            if bloco.shape.y <= 50 :
                mapa.change_room('cima',tela, player)
                player.shape.y = 375

    if "s" in teclas:
        player.shape.mover(dy=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y - player.shape.altura) - player.shape.y)

        if sit == True and bloco.tipo == 4:
            if bloco.shape.y >= 400:
                mapa.change_room('baixo',tela, player)
                player.shape.y = 50

    if "a" in teclas:
        player.shape.mover(dx=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x + bloco.shape.largura) - player.shape.x)

        if sit == True and bloco.tipo == 4:
            if bloco.shape.x <= 50:
                mapa.change_room('esquerda',tela, player)
                player.shape.x = 675
                
    if "d" in teclas:
        player.shape.mover(dx=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x - player.shape.largura) - player.shape.x)

        if sit == True and bloco.tipo == 4:
            if bloco.shape.x > 650:
                mapa.change_room('direita',tela, player)
                player.shape.x = 50

    if player.invenc != 0:
        player.invenc -= 1

tela.adicionar(player.shape)
tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=300)
tela.executar()