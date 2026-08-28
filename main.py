import aroeira as ar
import mapa
import player as pl


tela = ar.Tela("Roguelike", 15*50, 9*50)

mapa.drawRoom(mapa.roomLayout, tela)
player = pl.Player()

def colisao():
    for pixel in mapa.renderizado:
        if player.tocando(pixel):
            return True
    return False

teclas = set()

def pressionar(nome):
    teclas.add(nome.casefold())

def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
    if "w" in teclas:
        player.shape.mover(dy=-5)
        if colisao():
            player.shape.mover(dy=5)
    if "s" in teclas:
        player.shape.mover(dy=5)
        if colisao():
            player.shape.mover(dy=-5)
    if "a" in teclas:
        player.shape.mover(dx=-5)
        if colisao():
            player.shape.mover(dx=5)
    if "d" in teclas:
        player.shape.mover(dx=5)
        if colisao():
            player.shape.mover(dx=-5)

tela.adicionar(player.shape)
tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=300)
tela.executar()




