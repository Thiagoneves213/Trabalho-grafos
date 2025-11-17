from Atv1E2_implementada import GrafoListaArestas

g = GrafoListaArestas()
g.inserir_vertice('A')
g.inserir_vertice('B')
g.inserir_vertice('C')
g.inserir_vertice('D')

g.inserir_aresta('A', 'B')
g.inserir_aresta('B', 'C')
g.inserir_aresta('A', 'D')

print("BFS começando em A:", g.bfs('A'))
print("Grafo é conexo?", g.eh_conexo())
print("Componentes conexos:", g.componentes_conexos())
print("Menor caminho A -> C:", g.menor_caminho('A', 'C'))
