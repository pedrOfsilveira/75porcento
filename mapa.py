import aroeira as ar

class Pixel:
    def __init__(self, origem: ar.Ponto, cor: str, colisao: bool):
        self.shape: ar.Retangulo = ar.Retangulo(
            altura= 50, 
            largura= 50,
            origem= origem,
            cor= cor
        )
        self.colisao = colisao

roomLayout = [
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 0, 3, 3, 3, 2, 3, 3, 3, 0, 3, 0, 1],
    [4, 0, 3, 0, 3, 2, 0, 0, 0, 2, 3, 0, 3, 0, 4],
    [1, 0, 3, 0, 3, 3, 3, 2, 3, 3, 3, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
]

renderizado: list[Pixel] = []

def drawRoom(roomMatrix, tela):
    global renderizado
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
                4: False,
            }

            pixel = Pixel(
                origem=ar.Ponto(col * 50, i * 50),
                cor=cores[tipo],
                colisao=colisao[tipo]
            )


            if pixel.colisao:
                renderizado.append(pixel)

            tela.adicionar(pixel.shape)