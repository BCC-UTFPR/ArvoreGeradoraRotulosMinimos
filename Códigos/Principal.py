# coding=UTF-8
import random
import operator

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
			
class MLST:
	def exists_not_connected(self,label_list):
		if len(label_list) > 0:
			return True
		else:
			return False
			
	def generate_chromosome(self,graph,size):
		print 'Iniciando processo pra gerar indivíduo (cromossomo)...'

		line = 0
		column = 0
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		node_list = []
		node_list.extend([i for i in range(1,size)])
		label_list = []
		label_list.extend([i for i in range(1,size)])
		label_list_used = []
		
		
		while(self.exists_not_connected(node_list)):
			current_label = random.choice(label_list)
			label_list.remove(current_label)
			label_list_used.append(current_label)
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == current_label:
						adjacency_list[line].append(column + 1)
					column = column + 1
				column = 0
				line = line + 1
			line = 0
			column = 0
			for each_list in adjacency_list:
				for each_value in each_list:
					if each_value in node_list: node_list.remove(each_value)
		
		print 'Indivíduo gerado com sucesso! (Subgrafo)'
		print 'Lista de adjacência: '
		for i,each in enumerate(adjacency_list):
			each.sort()
			print str(i + 1) + ' -> ' + str(each)
		print '\n'	
		return label_list_used

	def crossover(self,S,graph,graph_size):
		print 'Iniciando processo de crossover...'

		frequency = []
		frequency.extend([0 for i in range(0,len(S))])
		
		for position,each_label in enumerate(S):
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == each_label:						
						frequency[position] = frequency[position] + 1
						
		print 'Rótulos: ' + str(S)
		print 'Frequência/Rótulo: ' + str(frequency)
		print 'Quantidade de rótulos usados: ' + str(len(S))
		print '\n'
		
		node_list = []
		node_list.extend([i for i in range(1,size)])
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		line = 0
		column = 0
		label_used = []
		
		while(self.exists_not_connected(node_list)):
			maximum_index, maximum_value = max(enumerate(frequency), key=operator.itemgetter(1))
			frequency[maximum_index] = 0
			current_label = S[maximum_index]
			label_used.append(current_label)
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == current_label:
						adjacency_list[line].append(column + 1)
					column = column + 1
				column = 0
				line = line + 1
			line = 0
			column = 0
			for each_list in adjacency_list:
				for each_value in each_list:
					if each_value in node_list: node_list.remove(each_value)
		
		print 'Foi gerado um novo subgrafo (t) com sucesso.'
		print 'Lista de adjacência: '

		for i,each in enumerate(adjacency_list):
			print str(i + 1) + ' -> ' + str(each)
		label_used.sort()
		print 'Rótulos utilizados em (t): ' + str(label_used)
		print 'Quantidade de rótulos (após crossover): ' + str(len(label_used))
		print '\n'
		return label_used
		
	def mutation(self,S,graph,size):
		print 'Iniciando processo de mutação...'
		label_not_used = []
		label_not_used.extend([i for i in range(1,size)])
		T = []
		
		flag = 0
		while flag == 0:
			current_label = random.choice(label_not_used)
			if not current_label in S:
				print 'Adicionado o rótulo ' + str(current_label) + ' em T.'
				S.append(current_label)
				S.sort()
				flag = 1
		
		frequency = []
		frequency.extend([0 for i in range(0,len(S))])
		for position,each_label in enumerate(S):
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == each_label:						
						frequency[position] = frequency[position] + 1
		
		print 'T: ' + str(S)
		print 'Frequência (T): ' + str(frequency)
		print '\n'
		
		node_list = []
		node_list.extend([i for i in range(1,size)])
		T = S
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		line = 0
		column = 0
		
		while(self.exists_not_connected(node_list)):
			frequency_index = frequency.index(min(frequency))
			node_removed = T[frequency_index]
			T.remove(node_removed)
			print 'T Atual: ' + str(T)
			print T
			for label in T:
				for label_line in graph:
					for label_column in label_line:
						label_column = int(label_column)
						if label_column == label:
							adjacency_list[line].append(column + 1)
						column = column + 1
					column = 0
					line = line + 1
				line = 0
				column = 0
				
			for each_list in adjacency_list:
				for each_value in each_list:
					if each_value in node_list: node_list.remove(each_value)	
			
			if not self.exists_not_connected(node_list):
				T.append(node_removed)
				break
		
		for each in adjacency_list:
			pass

		
	
reader = Reader()
mlst = MLST()
graph_list,graph_size = reader.read_graph_file('HDGraph20_20.txt')
size = int(graph_size[0]) # Size = 20
graph = graph_list[0] 

chromosome_a = mlst.generate_chromosome(graph,size)
chromosome_b = mlst.generate_chromosome(graph,size)
label_used = list(set(chromosome_a) | set(chromosome_b))
S = mlst.crossover(label_used,graph,size)
S = mlst.mutation(S,graph,size)
