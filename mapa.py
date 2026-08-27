import aroeira as ar

class Pixel:
    def __init__(self, origem: ar.Ponto, cor: str):
        self. shape: ar.Retangulo = ar.Retangulo(
            altura= 50, 
            largura= 50,
            origem= origem,
            cor= cor
        )

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


def drawRoom(roomMatrix, tela):
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

            pixel = Pixel(
                origem=ar.Ponto(col * 50, i * 50),
                cor=cores[tipo]
            )

            tela.adicionar(pixel.shape)