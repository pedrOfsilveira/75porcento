import aroeira as ar
import mapa 
class Player():
   
    def __init__(self):
        self.shape = ar.Retangulo(origem= ar.Ponto(x= 7 * 50, y= 0), largura=25, altura=25, cor="roxo")
        self.health = 3
        self.invenc = 80

    def tocando(self, bloco: mapa.Pixel):
        quadrado = self.shape
        tile = bloco.shape
        return quadrado.x < tile.x + tile.largura and quadrado.x + quadrado.largura > tile.x and quadrado.y < tile.y + tile.altura and quadrado.y + quadrado.altura > tile.y

    def dano(self, vidas):
        if self.invenc == 0:
            #Esse -1 pode ser adicionado como argumento na função para colocar o dano do inimigo
            self.health -= 1
            self.invenc = 80
            vidas.conteudo = f"Vidas: {self.health}"

