class GrafoListaArestas:
    def _init_(self):
        self.vertices = []
        self.arestas = []

    def inserir_vertice(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

    def remover_vertice(self, v):
        if v in self.vertices:
            self.vertices.remove(v)
            self.arestas = [(a, b) for (a, b) in self.arestas if a != v and b != v]

    def inserir_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            if (v1, v2) not in self.arestas:
                self.arestas.append((v1, v2))

    def remover_aresta(self, v1, v2):
        if (v1, v2) in self.arestas:
            self.arestas.remove((v1, v2))

    def grau_vertices(self):
        for v in self.vertices:
            grau = sum(1 for (a, b) in self.arestas if a == v)
            print(f'{v}: {grau}')

    def existe_aresta(self, v1, v2):
        return (v1, v2) in self.arestas

    def vizinhos(self, v):
        return [b for (a, b) in self.arestas if a == v]

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if (caminho[i], caminho[i + 1]) not in self.arestas:
                return False
        return True


g = GrafoListaArestas()
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