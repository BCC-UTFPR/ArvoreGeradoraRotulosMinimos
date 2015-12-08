#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from collections import defaultdict, deque

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

def dijsktra(graph, initial):
  visited = {initial: 0} # É definida a distância do primeiro como zero
  path = {} # Cria um novo dicionário para armazenar o caminho

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None # Define o nó mínimo como indefinido
    for node in nodes:
      if node in visited: # Se o nó está na lista de visitados
        if min_node is None: # Se ainda não existe um nó definido como mínimo
          min_node = node # Nó mínimo recebe o próprio nó
        elif visited[node] < visited[min_node]: # Se a lista de visitados[nó] < lista de visitado[nó_mínimo]
          min_node = node # Nó mínimo recebe o próprio nó

    if min_node is None: # Se, após tentar definir um nó mínimo, ele ainda for indefinido, para a execução.
      break

    nodes.remove(min_node) # Remove o nó mínimo da lista de nós (já foi visitado)
    current_weight = visited[min_node] # O peso atual recebe o valor do nó mínimo na lista de visitados

    for edge in graph.edges[min_node]: # Para cada aresta presente no dicionário do nó mínimo
		try:
			weight = current_weight + graph.distances[(min_node, edge)] # Peso = peso_atual + distância (nó mínimo,aresta do nó vistiado)
		except KeyError,e:
		  print 'I got a KeyError - reason "%s"' % str(e)
		if edge not in visited or weight < visited[edge]: # Se a aresta não está entre os visitados ou o peso for menor que a do visitado
			visited[edge] = weight # Aresta do visitado recebe peso
			path[edge] = min_node # Caminho recebe o vértice mínimo
	return visited, path

def read_file(file_name):
	print 'Fazendo a leitura do arquivo...'
	graph_file = open(file_name,'r')
	graph_line = graph_file.readlines()[4:] # Ignora as quatro primeiras linhas
	print 'PRONTO!'
	return graph_line

def define_nodes(graph_line):
	print 'Carregando os nós do arquivo...'
	list_nodes = []
	for line in graph_line:
		line = line.split()
		if line[0] not in list_nodes:
			list_nodes.append(line[0])
		if line[1] not in list_nodes:
			list_nodes.append(line[1])
	list_nodes.sort()
	print 'PRONTO!'
	return list_nodes

def shortest_path(graph, origin, destination):
    visited, paths = dijsktra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
      
if __name__ == '__main__':
	graph_line = read_file('xaa')
	list_nodes = define_nodes(graph_line)
	graph = Graph()
	
	for node in list_nodes:
		vertex = graph.add_node(int(node))
		
	for line in graph_line:
		line = line.split()
		node_from = int(line[0])
		node_to = int(line[1])
		graph.add_edge(node_from,node_to,abs(round(node_to - node_from)))
	
	#print 'Nós do grafo:'
	#print graph.nodes
	#print 'Arestas do grafo:'
	#print graph.edges
	#print 'Distâncias do grafo: '
	#print graph.distances
	
	print 'Caminho mínimo: '
	print(shortest_path(graph,0, 1))
