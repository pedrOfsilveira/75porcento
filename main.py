import aroeira as ar
import mapa


tela = ar.Tela("Roguelike", 15*50, 9*50)

mapa.drawRoom(mapa.roomLayout, tela)

tela.executar()




