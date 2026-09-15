import aroeira as ar
import mapa
import player as pl

velocidade = 40

tela = ar.Tela("Roguelike", 15*50, 9*50)

mapa.drawRoom(mapa.roomLayout, tela)
player = pl.Player()

def colisao():
    for pixel in mapa.renderizado:
        if player.tocando(pixel):
            return True, pixel
    return False, pixel

teclas = set()

def pressionar(nome):
    teclas.add(nome.casefold())

def soltar(nome):
    teclas.discard(nome.casefold())

def atualizar():
    if "w" in teclas:
        player.shape.mover(dy=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y + 50) - player.shape.y)
    if "s" in teclas:
        player.shape.mover(dy=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dy=(bloco.shape.y - 25) - player.shape.y)
    if "a" in teclas:
        player.shape.mover(dx=-velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x + 50) - player.shape.x)   
    if "d" in teclas:
        player.shape.mover(dx=velocidade)
        sit, bloco = colisao()
        if sit == True:
            player.shape.mover(dx=(bloco.shape.x - 25) - player.shape.x)
    print(player.shape.origem)

#VER A COLISÃO COM O PEDRO, QUANDO MUITO A VELOCIDADE ESTÁ MUITO ALTA O PERSONAGEM FICA ALGUNS PIXEIS DE DISTÂNCIA DA PAREDE

tela.adicionar(player.shape)
tela.ao_pressionar_tecla(pressionar)
tela.ao_soltar_tecla(soltar)
tela.animar(atualizar, fps=300)
tela.executar()