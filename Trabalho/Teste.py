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
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
		try:
			weight = current_weight + graph.distances[(min_node,edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node
		except KeyError,e:
			continue

  return visited,path

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
		if len(line) > 1:
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
		if len(line) > 1:
			node_from = int(line[0])
			node_to = int(line[1])
			graph.add_edge(node_from,node_to,abs(round(node_to - node_from)))

	print 'Caminho mínimo: '
	print(shortest_path(graph,362,9456))
