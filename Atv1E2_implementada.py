from collections import deque

class GrafoListaArestas:
    def __init__(self):
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
            if (v1, v2) not in self.arestas and (v2, v1) not in self.arestas:
                self.arestas.append((v1, v2))

    def remover_aresta(self, v1, v2):
        if (v1, v2) in self.arestas:
            self.arestas.remove((v1, v2))
        elif (v2, v1) in self.arestas:
            self.arestas.remove((v2, v1))

    def grau_vertices(self):
        for v in self.vertices:
            grau = sum(1 for (a, b) in self.arestas if a == v or b == v)
            print(f'{v}: {grau}')

    def existe_aresta(self, v1, v2):
        return (v1, v2) in self.arestas or (v2, v1) in self.arestas

    def vizinhos(self, v):
        viz = []
        for (a, b) in self.arestas:
            if a == v:
                viz.append(b)
            if b == v:
                viz.append(a)
        return viz

    def bfs(self, inicio):
        visitados = set()
        fila = deque()
        ordem = []

        visitados.add(inicio)
        fila.append(inicio)

        while fila:
            atual = fila.popleft()
            ordem.append(atual)

            for viz in self.vizinhos(atual):
                if viz not in visitados:
                    visitados.add(viz)
                    fila.append(viz)

        return ordem

    def eh_conexo(self):
        if not self.vertices:
            return True

        visitados = set(self.bfs(self.vertices[0]))
        return len(visitados) == len(self.vertices)
    
    def componentes_conexos(self):
        nao_visitados = set(self.vertices)
        componentes = []

        while nao_visitados:
            inicio = next(iter(nao_visitados))
            comp = set(self.bfs(inicio))
            componentes.append(comp)
            nao_visitados -= comp

        return componentes

    def menor_caminho(self, inicio, destino):
        fila = deque([
            {'vertice': inicio, 'caminho': [inicio]}
        ])

        visitados = set()

        while fila:
            atual = fila.popleft()
            v = atual['vertice']
            caminho = atual['caminho']

            if v == destino:
                return caminho  

            visitados.add(v)

            for viz in self.vizinhos(v):

              
                viz_na_fila = any(item['vertice'] == viz for item in fila)

                if not viz_na_fila and viz not in visitados:
                    fila.append({
                        'vertice': viz,
                        'caminho': caminho + [viz]
                    })

        return [] 
