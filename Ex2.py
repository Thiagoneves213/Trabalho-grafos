class GrafoMatriz:
    def _init_(self):
        self.vertices = []
        self.matriz = []

    def inserir_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            for linha in self.matriz:
                linha.append(0)
            self.matriz.append([0] * len(self.vertices))

    def remover_vertice(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            self.vertices.pop(i)
            self.matriz.pop(i)
            for linha in self.matriz:
                linha.pop(i)

    def inserir_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices.index(v1), self.vertices.index(v2)
            self.matriz[i][j] = 1

    def remover_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices.index(v1), self.vertices.index(v2)
            self.matriz[i][j] = 0

    def grau_vertices(self):
        for i, v in enumerate(self.vertices):
            grau = sum(self.matriz[i])
            print(f'{v}: {grau}')

    def existe_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i, j = self.vertices.index(v1), self.vertices.index(v2)
            return self.matriz[i][j] == 1
        return False

    def vizinhos(self, v):
        if v in self.vertices:
            i = self.vertices.index(v)
            return [self.vertices[j] for j in range(len(self.vertices)) if self.matriz[i][j] == 1]
        return []

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i + 1]):
                return False
        return True


g = GrafoMatriz()
g.inserir_vertice('A')
g.inserir_vertice('B')
g.inserir_vertice('C')
g.inserir_aresta('A', 'B')
g.inserir_aresta('B', 'C')
g.grau_vertices()
print(g.existe_aresta('A', 'B'))
print(g.vizinhos('B'))
print(g.percurso_possivel(['A', 'B', 'C']))
g.remover_aresta('A', 'B')
g.remover_vertice('C')