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


#Lida com a porta e os espinhos por enquanto
def blocos_extras():
    playery = player.shape.y
    playerx = player.shape.x
    playerlargura = player.shape.largura
    playeraltura = player.shape.altura

    for extras in mapa.extras:
        if extras.tipo == 3:
            if (playerx < extras.shape.x + extras.shape.largura and playerx + playerlargura > extras.shape.x) and (playery < extras.shape.y + extras.shape.altura and playery + playeraltura > extras.shape.y):

                player.dano(vidas)
        
        if extras.tipo == 4:
            if (playerx < extras.shape.x + extras.shape.largura and playerx + playerlargura > extras.shape.x) and (playery < extras.shape.y + extras.shape.altura and playery + playeraltura > extras.shape.y):

                if extras.shape.y <= 50 :
                    mapa.change_room('cima',tela, player)
                    player.shape.y = 374

                if extras.shape.y >= 400:
                    mapa.change_room('baixo',tela, player)
                    player.shape.y = 51

                if extras.shape.x <= 50:
                    mapa.change_room('esquerda',tela, player)
                    player.shape.x = 674

                if extras.shape.x > 650:
                    mapa.change_room('direita',tela, player)
                    player.shape.x = 51


def atualizar():
    blocos_extras()
    if "w" in teclas:
        player.shape.mover(dy=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y + bloco.shape.altura) - player.shape.y)

    if "s" in teclas:
        player.shape.mover(dy=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y - player.shape.altura) - player.shape.y)


    if "a" in teclas:
        player.shape.mover(dx=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x + bloco.shape.largura) - player.shape.x)

                
    if "d" in teclas:
        player.shape.mover(dx=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x - player.shape.largura) - player.shape.x)    

    if player.invenc != 0:
        player.invenc -= 1

tela.adicionar(player.shape)
tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=300)
tela.executar()