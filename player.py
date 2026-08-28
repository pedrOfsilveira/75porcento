import aroeira as ar
import mapa 
class Player():
    def __init__(self):
        self.shape = ar.Retangulo(origem= ar.Ponto(x= 7 * 50, y= 0), largura=25, altura=25, cor="roxo")

    def tocando(self, tile: mapa.Pixel):
        quadrado = self.shape
        tile = tile.shape
        return quadrado.x < tile.x + tile.largura and quadrado.x + quadrado.largura > tile.x and quadrado.y < tile.y + tile.altura and quadrado.y + quadrado.altura > tile.y

    
        
