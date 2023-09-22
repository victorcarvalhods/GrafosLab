from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]

    def addArestas(self, v1, v2):
        self.grafo[v1].append(v2)
        self.grafo[v2].append(v1)

    def bfs(self):
        fila = deque()
        visitados = [False] * self.vertices
        predecessores = [-1] * self.vertices

        inicio = 0  # Primeiro vértice
        fim = self.vertices - 1  # Último vértice

        fila.append(inicio)
        visitados[inicio] = True

        while fila:
            vertice_atual = fila.popleft()

            if vertice_atual == fim:
                caminho = self.construir_caminho(predecessores, inicio, fim)
                return caminho

            for vizinho in self.grafo[vertice_atual]:
                if not visitados[vizinho]:
                    fila.append(vizinho)
                    visitados[vizinho] = True
                    predecessores[vizinho] = vertice_atual

        return None

    def construir_caminho(self, predecessores, inicio, fim):
        caminho = []
        atual = fim
        while atual != -1:
            caminho.insert(0, atual)
            atual = predecessores[atual]
        return caminho



