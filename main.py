import aroeira as ar
import mapa
import player as pl

velocidade = 5

tela = ar.Tela("Roguelike", 15*50, 9*50)


mapa.drawRoom(mapa.roomLayout, tela)
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
        player.dano(vidas)

def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
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