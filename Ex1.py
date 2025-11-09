class Grafo:
    def _init_(self):
        self.lista_adj = {}

    def inserir_vertice(self, v):
        if v not in self.lista_adj:
            self.lista_adj[v] = []

    def remover_vertice(self, v):
        if v in self.lista_adj:
            del self.lista_adj[v]
            for vizinhos in self.lista_adj.values():
                if v in vizinhos:
                    vizinhos.remove(v)

    def inserir_aresta(self, v1, v2):
        if v1 in self.lista_adj and v2 in self.lista_adj:
            if v2 not in self.lista_adj[v1]:
                self.lista_adj[v1].append(v2)

    def remover_aresta(self, v1, v2):
        if v1 in self.lista_adj and v2 in self.lista_adj[v1]:
            self.lista_adj[v1].remove(v2)

    def grau_vertices(self):
        for v in self.lista_adj:
            print(f'{v}: {len(self.lista_adj[v])}')

    def existe_aresta(self, v1, v2):
        return v1 in self.lista_adj and v2 in self.lista_adj[v1]

    def vizinhos(self, v):
        if v in self.lista_adj:
            return self.lista_adj[v]
        return []

    def percurso_possivel(self, caminho):
        for i in range(len(caminho) - 1):
            if not self.existe_aresta(caminho[i], caminho[i + 1]):
                return False
        return True


g = Grafo()
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