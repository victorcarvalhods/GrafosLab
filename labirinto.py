from grafo import Grafo

def marcar_caminho_no_labirinto(caminho, labirinto):
    for vertice in caminho:
        x, y = cordenadas[vertice]
        if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[x]) and labirinto[x][y] == ' ':
            labirinto[x][y] = 'X'

    with open('L1Path.txt', 'w') as l1:
        for linha in labirinto:
            l1.write(''.join(linha))
            l1.write('\n')

def ler_labirinto_de_arquivo(nome_arquivo):
    labirinto = []
    with open(nome_arquivo, 'r+') as arquivo:
        for linha in arquivo:
            labirinto.append(list(linha.rstrip('\n')))

    return labirinto

def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print(''.join(linha))



def lado(chave, valor, dic, grafo):     ##Busca um vertice ao lado
    aux = [valor[0], valor[1]+1]
    if aux in dic.values():
        grafo.addArestas(chave, chave+1)

def obter_chave(val):
    for chave, valor in cordenadas.items():
         if val == valor:
             return chave

def baixo(chave, valor, dic, grafo):    ##Busca um vertice abaixo
    aux = [valor[0]+1, valor[1]]
    if aux in dic.values():
        grafo.addArestas(chave, obter_chave(aux))

# Lê as coordenadas do labirinto
with open("L1.txt", "r") as l1:
    cordenadas = {}
    abscissa = 1
    aux = 0
    for i in l1:
        j = i.rstrip('\n')
        ordenada = 1
        for linha in i:
            if linha == ' ':
                cordenadas[aux] = ([abscissa, ordenada])
                aux += 1
            ordenada += 1
        abscissa += 1

print(cordenadas)
# Cria o grafo
g1 = Grafo(len(cordenadas))

# Adiciona as arestas ao grafo
for chave, valor in cordenadas.items():
    lado(chave, valor, cordenadas, g1)
    baixo(chave, valor, cordenadas, g1)

# Encontra o menor caminho no grafo
caminho_mais_curto = g1.bfs()

if caminho_mais_curto:
    print("\nMenor caminho:", caminho_mais_curto, '\n')

    # Lê o labirinto do arquivo
    labirinto = ler_labirinto_de_arquivo("L1.txt")

    # Marca o caminho no labirinto
    marcar_caminho_no_labirinto(caminho_mais_curto, labirinto)

    # Imprime o labirinto com o caminho marcado
    imprimir_labirinto(labirinto)
else:
    print("Não foi possível encontrar um caminho.")