#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys
import heapq # Heap Queue

class Node:
	# Método construtor
    def __init__(self, node):
        self.id = node # ID da instância
        self.adjacent = {} # Define o dicionário de adjacentes como vazio
        self.distance = sys.maxint  # Define a distância como o máximo possível     
        self.visited = False # Define o nó como não visitado
        self.previous = None # Considera que ainda não há predecessores

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_previous(self, previous):
        self.previous = previous

	def get_previous(self):
		return self.previous
		
    def set_visited(self):
        self.visited = True

	def is_visited(self):
		if self.visited is True:
			return True
		else:
			return False
			
	# Dicionário: Vértice(Adjacente -> Peso)
    def add_weight(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_connections(self):
        return self.adjacent.keys()  
	
    def get_id(self):
        return self.id

class Graph:
    def __init__(self):
        self.nodes = {}
        self.number_of_nodes = 0

    def __iter__(self):
        return iter(self.nodes.values())

    def add_node(self, value):
        self.number_of_nodes = self.number_of_nodes + 1
        new_node = Node(value)
        self.nodes[value] = new_node
        return new_node

    def get_node(self, value):
        if value in self.nodes:
            return self.nodes[value]
        else:
			print 'Este nó não consta no dicionário de nós'
			return None

    def add_edge(self, node_from, node_to, cost):
		if cost is None:
			cost = 0
		if node_from not in self.nodes:
			self.add_node(node_from)
		if node_to not in self.nodes:
			self.add_node(node_to)
		self.nodes[node_from].add_weight(self.nodes[node_to], cost)
		self.nodes[node_to].add_weight(self.nodes[node_from], cost)

    def get_vertices(self):
        return self.nodes.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def read_file(file_name):
	print 'Fazendo a leitura do arquivo...'
	graph_file = open(file_name,'r')
	graph_line = graph_file.readlines()[4:] # Ignores the first four lines
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

def define_edges(graph,graph_line):
	print 'Definindo os vértices e pesos do grafo'
	for line in graph_line:
		line = line.split()
		node_from = int(line[0])
		node_to = int(line[1])
		graph.add_edge(node_from,node_to, abs(round(node_to - node_from)))
	print 'PRONTO!'
	return graph
		 
def menor_caminho(node,path):
    if node.previous:
		path.append(node.previous.get_id())
		shortest(node.previous, path)
    return path
    
def dijkstra(graph, start, target):
    start.set_distance(0) # É definida a distância do primeiro como zero
    Q = [(v.get_distance(),v) for v in graph] # Lista com a distância dos vértices não visitados
    heapq.heapify(Q) # Transforma a lista em um Heap

    while len(Q):
        vertex = heapq.heappop(Q) # Busca o vértice com a menor distância
        current = vertex[1]
        current.set_visited()
    
        # Para todos os adjacentes ao vértice atual
        for next in current.adjacent:
            # Se o vértice não foi visitado
            if not next.visited:
				distance = current.get_distance() + current.get_weight(next)
            
            if distance < next.get_distance():
                next.set_distance(distance)
                next.set_previous(current)
        
        # Reinicia os valores
        while len(Q):
            heapq.heappop(Q)
        Q = [(v.get_distance(),v) for v in graph if not v.visited]
        heapq.heapify(Q)

def remove_equal_nodes(node_list):
	list_auxiliar = []
	new_list = []
	for node in node_list:
		if node not in list_auxiliar:
			list_auxiliar.append(node)
			new_list.append(node)
	return new_list
	
def shortest_path(graph_line,start,target):
	node_current = start
	distancia = 0
	lista_distancias = []
	node_already_used = []
	
	for line in graph_line:
		line = line.split()
		node_already_used.append(node_current)
		print 'Nó atual ' + node_current
		if line[0] == node_current:
			if line[1] not in node_already_used:
				print 'Nó na sequência ' + line[1]
				if line[1] == target:
					distancia = distancia + abs(round(int(line[1]) - int(line[0])))
					node_already_used.append(target)
					node_already_used = remove_equal_nodes(node_already_used)
					print 'Caminho encontrado' + str(node_already_used)
					node_already_used.remove(start)
					node_already_used.remove(target)
					lista_distancias.append(distancia)
					break
				distancia = distancia + abs(round(int(line[1]) - int(line[0])))
				node_current = line[1]		
	print lista_distancias
	return lista_distancias
	
if __name__ == '__main__':
	graph_line = read_file('teste.txt')
	list_nodes = define_nodes(graph_line)
	graph = Graph()
	
	for node in list_nodes:
		vertex = graph.add_node(node)
		
	edges = define_edges(graph,graph_line)

	for node in graph:
		for node_connected in node.get_connections():
			node_id = node.get_id()
			node_connected_id = node_connected.get_id()
			print '(vértice: %s -> vértice: %s, weight: %3d)'  % (node_id, node_connected_id, node.get_weight(node_connected))

	print 'Primeiro vértice:' + str(list_nodes[0])
	print 'Segundo vértice:' + str(list_nodes[3])
	#dijkstra(graph,graph.get_node(list_nodes[0]),graph.get_node(list_nodes[3]))
	distance = shortest_path(graph_line,list_nodes[0],list_nodes[3])
	print distance
	#target = graph.get_node(list_nodes[3])
	#path = [target.get_id()]
	#menor_caminho(target, path)
	#print 'O menor caminho é: %s' %(path[::-1])
