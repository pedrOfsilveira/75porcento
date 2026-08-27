vou tentar criar um roguelike (baseado em isaac) usando a biblioteca aroeira.

vou usar esse documento para anotar o raciocínio e tentar me organizar melhor :) 

## REGRAS:

- utilizar ao máximo a biblioteca aroeira para criar o jogo
- sem IA 
- manter a simplicidade




## TORÓ DE IDEIAS

O PERSONAGEM PRECISA IR PRA AULA POIS ESTÁ NO LIMITE DAS FALTAS, ENTÃO ELE PRECISA CHEGAR NA SALA DE AULA ANTES QUE O PROFESSOR CHEGUE.

NO CAMINHO ELE PRECISA LUTAR CONTRA VARIOS OBSTACULOS E TENTAR CONSEGUIR ITENS QUE O AJUDEM A CHEGAR NA SALA DE AULA.

SE ELE NÃO CONSEGUIR E MORRER, NA PROXIMA VEZ ELE PODERÁ TER ALGUMAS VANTAGENS. 


## TEORIA

GERAR MAPAS:

8x8

1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 0 0 1 1 2 0 1
1 0 0 0 0 0 0 1
1 0 0 2 0 0 0 1
1 0 0 1 1 0 0 1
1 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1

UMA MATRIZ EM QUE TUDO QUE É 1 É PAREDE, O 0 É CHÃO, E O 2 SÃO ITENS, ALGO ASSIM.
AÍ MAIS COISAS TIPO INIMIGOS, BURACOS, ESPINHOS, ETC
