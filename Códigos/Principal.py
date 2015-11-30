# coding=UTF-8
import random

class Reader:
	def read_graph_file(self,file_name):
		graph_list = []
		graph = []
		with open(file_name) as lines:
			graph_size = lines.readline().split()
			for line in lines:
				if line.replace('\r','') != '\n':			
					graph.append(line.rstrip().split()[::-1])
				else:
					graph_list.append(graph)
					graph = []
		return graph_list,graph_size					
			
class MVCA:
	def generate_subgraph(self,list_node,list_edges,list_label):
		C = [] # Set of used labels
		H = list_label # Subgraph of G
		line = 1
		column = 1
		
		while self.is_connected(H):
			for label_line in list_label:
				for label in label_line:
					label = int(label)
					if self.is_label_new(label,C):
						print 'O valor não está na lista de usados'
					
	def is_connected(self,H):
		return True
					
	def generate_new_graph(self,lenght):
		column = lenght - 1
		line = lenght - 1
		new_list = []
		index = 0
		for line in range(0, line): 
			new_list.append([])
			for j in range(0, column):
				new_list[index].append(lenght + 1) # Default value: there isn't a edge
			column = column - 1
			index = index + 1
		return new_list
		
	def is_label_new(self,label,list_used):
		if len(list_used) < 1:
			return True
		else:
			for label_used in list_used:
				if label == label_used:
					return False
		return True

class GeneticAlgorithm:
	def crossover(self,subgraph_a,subgraph_b):
		S = list(set(subgraph_a) | set(subgraph_b))
		print S
		
	def union(self,subgraph_x,subgraph_y,lenght):
		line_count = 0
		column_count = 0
		for line in subgraph_x:
			for column_value in line:
				print column_value
				print lenght
				if column_value == lenght:
					auxiliar_y = subgraph_y[line_count]
					auxiliar_x = subgraph_x[line_count]
					auxiliar_x[column_count - 1] = 10
				column_count = column_count + 1
			line_count = line_count + 1
		return subgraph_x
					

genetic = GeneticAlgorithm()
a = [[1,2,3],[4,4,4]]
b = [[1,2,3],[1,2,3]]
sub = genetic.union(a,b,4)
print sub
"""
reader = Reader()
mvca = MVCA()
graph_list,graph_size = reader.read_graph_file('HDGraph20_20.txt')
list_node = range(0,int(graph_size[0])) 
list_label = graph_list[0] 
list_edge = []
mvca.generate_subgraph(list_node,list_edge,list_label)
"""
