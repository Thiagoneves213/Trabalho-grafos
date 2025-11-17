from Atv1E2_implementada import GrafoListaArestas

# Criar grafo
g = GrafoListaArestas()

# Inserir vértices
for v in ["A", "B", "C", "D", "E", "F", "G"]:
    g.inserir_vertice(v)

# Inserir arestas
g.inserir_aresta("A", "B")
g.inserir_aresta("A", "C")
g.inserir_aresta("B", "D")
g.inserir_aresta("C", "D")
g.inserir_aresta("C", "E")
g.inserir_aresta("D", "F")
g.inserir_aresta("E", "F")
g.inserir_aresta("F", "G")

print("BFS começando em A:")
print(g.bfs("A"))

print("\nMenor caminho de A até F:")
print(g.menor_caminho("A", "F"))

print("\nMenor caminho de B até E:")
print(g.menor_caminho("B", "E"))

print("\nMenor caminho de A até G:")
print(g.menor_caminho("A", "G"))

print("\nGrafo é conexo?")
print(g.eh_conexo())

print("\nComponentes conexos:")
print(g.componentes_conexos())

