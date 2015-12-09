#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from collections import defaultdict,deque
from colorama import Fore, Back, Style

def read_file(file_name):
	print Fore.WHITE + 'Fazendo a leitura do arquivo...'
	graph_file = open(file_name,'r')
	graph_line = graph_file.readlines()
	print Fore.GREEN + 'PRONTO!'
	return graph_line

def define_nodes(graph_line):
	print Fore.WHITE + 'Carregando os nós do arquivo...'
	list_nodes = []
	for line in graph_line:
		line = line.split()
		if len(line) > 1:
			if line[0] not in list_nodes:
				list_nodes.append(line[0])
			if line[1] not in list_nodes:
				list_nodes.append(line[1])
	list_nodes.sort()
	print Fore.GREEN + 'PRONTO!'
	return list_nodes

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
	
def dijsktra(graph, initial):
	visitados = {initial: 0}
	caminho = {}
	vertices = set(graph.nodes)

	while vertices: 
		vertice_minimo = None
		
		for vertice in vertices:
			if vertice in visitados:
				if vertice_minimo is None:
					vertice_minimo = vertice
				elif visitados[vertice] < visitados[vertice_minimo]:
					vertice_minimo = vertice

		if vertice_minimo is None:
			break

		vertices.remove(vertice_minimo)
		peso_vertice_minimo = visitados[vertice_minimo]

		for vertice_conectado in graph.edges[vertice_minimo]:
			try:
				peso = peso_vertice_minimo + graph.distances[(vertice_minimo,vertice_conectado)]
				if vertice_conectado not in visitados or peso < visitados[vertice_conectado]:
					visitados[vertice_conectado] = peso
					caminho[vertice_conectado] = vertice_minimo
			except KeyError,e:
				continue
				
	return visitados,caminho
     
if __name__ == '__main__':

	graph_line = read_file('rotas-cem-mil.txt')
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

	while(True):
		print Fore.WHITE + 'Caminho mínimo: '
		x = raw_input('Digite um valor para x:')
		y = raw_input('Digite um valor para y:')
		print(Fore.GREEN + str(shortest_path(graph,int(x),int(y))))
