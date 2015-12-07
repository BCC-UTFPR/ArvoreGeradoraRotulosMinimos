def exists_not_connected(self,label_list):
	if len(label_list) > 0:
		return True
	else:
		return False

class Chromosome:	
	def chromosome(self,graph,size):
		print 'Iniciando processo pra gerar indivíduo (cromossomo)...'

		# Inicializando valores
		line = 0
		column = 0
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		node_list = []
		node_list.extend([i for i in range(1,size)])
		label_list = []
		label_list.extend([i for i in range(1,size)])
		label_list_used = []
		
		# Enquanto existir vértices não conectados
		while(exists_not_connected(node_list)):
			current_label = random.choice(label_list) # Escolhe um rótulo aleatório
			label_list.remove(current_label) # Retira o rótulo da lista de rótulos a serem usados
			label_list_used.append(current_label) # Coloca o rótulo na lista de rótulos já usados
			
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column) 
					if label_column == current_label: # Se algum valor da linha do vértice for igual o rótulo
						adjacency_list[line].append(column + 1) # Adiciona o vértice da coluna a lista do vértice da linha
					column = column + 1
				column = 0
				line = line + 1
			line = 0
			column = 0
			for each_list in adjacency_list:
				for each_value in each_list: # Para cada valor na lista de adjacência
					if each_value in node_list: node_list.remove(each_value) # Se o valor ainda não foi removido (ainda está na lista de nós), o remove.
		
		for i,each_list in enumerate(adjacency_list):
			for j,each_value in enumerate(each_list):
				adjacency_list[i][j] = size - each_value 
		
		# O algoritmo termina quando todos os nós são removidos da lista de nós, ou seja, quando todos os nós estão conectados.
		print 'Indivíduo gerado com sucesso! (Subgrafo)'
		print 'Lista de adjacência: '
		for i,each in enumerate(adjacency_list):
			each.sort()
			print str(i) + ' -> ' + str(each)
		label_list_used.sort()
		print 'Rótulos usados: ' + str(label_list_used)
		print '\n'	
		return label_list_used # Retorno os rótulos usados no cromossomo

class Crossover:
	# Algoritmo de crossover
	def crossover(self,S,graph,graph_size): # Recebe a concatenação do cromossomo a e do b em S
		print 'Iniciando processo de crossover...'

		frequency = []
		frequency.extend([0 for i in range(0,len(S))])
		
		for position,each_label in enumerate(S):
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == each_label:						
						frequency[position] = frequency[position] + 1 # Define a frequência de cada rótulo em S
						
		print 'Rótulos: ' + str(S)
		print 'Frequência/Rótulo: ' + str(frequency)
		print 'Quantidade de rótulos usados: ' + str(len(S))
		print '\n'
		
		# Inicializa os valores
		node_list = []
		node_list.extend([i for i in range(1,size)])
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		line = 0
		column = 0
		label_used = []
		
		while(exists_not_connected(node_list)):
			maximum_index, maximum_value = max(enumerate(frequency), key=operator.itemgetter(1)) 
			frequency[maximum_index] = 0
			current_label = S[maximum_index] # Escolhe o maior valor de S
			label_used.append(current_label)
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == current_label:
						adjacency_list[line].append(column + 1) # Cria uma lista de adjacência a partir do maior rótulo no momento
					column = column + 1
				column = 0
				line = line + 1
			line = 0
			column = 0
		
			for each_list in adjacency_list:
				for each_value in each_list:
					if each_value in node_list: node_list.remove(each_value) # Verifica se todos os nós estão conectados
		
		for i,each_list in enumerate(adjacency_list):
			for j,each_value in enumerate(each_list):
				adjacency_list[i][j] = size - each_value
				
		print 'Foi gerado um novo subgrafo (t) com sucesso.'
		print 'Lista de adjacência: '
		for i,each in enumerate(adjacency_list):
			each.sort()
			print str(i) + ' -> ' + str(each)
			
		label_used.sort()
		print 'Rótulos utilizados em (t): ' + str(label_used)
		print 'Quantidade de rótulos (após crossover): ' + str(len(label_used))
		print '\n'
		return label_used # Retorna todos os rótulos de (t)

class Mutation:		
	# Algoritmo de mutação	
	def mutation(self,s,graph,size): # Recebe o subgrafo (t) de crossover(...) e armazena em (s)
		print 'Iniciando processo de mutação...'
		
		label_not_used = []
		label_not_used.extend([i for i in range(1,size)])
		
		print '(s): ' + str(s)
		
		while True: # Percorre a lista de rótulos
			current_label = random.choice(label_not_used)
			if not current_label in s: # Adiciona um rótulo que ainda não pertence ao (s)
				print 'Adicionado o rótulo ' + str(current_label) + ' em (s).'
				s.append(current_label)
				s.sort()
				break
		print '(s) (após adicionar o rótulo): ' + str(s)
		
		frequency = []
		frequency.extend([0 for i in range(0,len(S))])
		for position,each_label in enumerate(S):
			for label_line in graph:
				for label_column in label_line:
					label_column = int(label_column)
					if label_column == each_label:						
						frequency[position] = frequency[position] + 1 # Cria uma lista de frequência para todos os rótulos de (s) (inclusive o novo rótulo adicionado)
		print 'Frequência/Rótulo: ' + str(frequency)
		print '\n'

		# Inicializa os valores
		tamanho_lista = len(s)
		node_list = []
		node_list.extend([i for i in range(1,size)])
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		line = 0
		column = 0
		
		for i in range(0,tamanho_lista):
			adjacency_list = []
			adjacency_list.extend([[] for i in range(size - 1)])
			node_list = []
			node_list.extend([i for i in range(1,size)])

			frequency_index = frequency.index(min(frequency))
			node_removed = s[frequency_index]
			frequency.pop(frequency_index)
			s.pop(frequency_index)
			
			print 'Rótulos (s): ' + str(s)
			print 'Lista de nós: ' + str(node_list)
			print 'Frequência/Rótulo: ' + str(frequency)
			print 'Freq. index: ' + str(frequency_index)
			print 'Tentando remover o rótulo ' + str(node_removed)

			for label in s:
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
			
			# Se não sobraram mais elementos mesmo após remover o rótulo, len(node_list) não é maior que que zero
			if not exists_not_connected(node_list):
				print 'O nó ' + str(node_removed) + ' foi removido da lista de rótulos'
				print '\n'
				
			else:
				print 'O nó ' + str(node_removed) + ' não pode ser removido. Devolvendo ele a lista de rótulos'
				print '\n'
				frequency.insert(frequency_index, 10000)
				s.insert(frequency_index,node_removed)
				s.sort()

		# Cria uma lista de adjacência pros rótulos que sobraram
		adjacency_list = []
		adjacency_list.extend([[] for i in range(size - 1)])
		column = 0
		line = 0
		
		for label in s:
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
			
		for i,each_list in enumerate(adjacency_list):
			for j,each_value in enumerate(each_list):
				adjacency_list[i][j] = size - each_value
		
		node_used = []
		node_used.extend(i for i in range(1,size))		
		new_adjacency_list = []
		new_adjacency_list.extend([[] for i in range(size - 1)])

		for line,each_list in enumerate(adjacency_list):
			for column,each_value in enumerate(each_list):
				for node in node_used:
					if each_value == node:						
						node_used.remove(node)
						new_adjacency_list[line].append(each_value) 
							
		for i,each in enumerate(new_adjacency_list):
				each.sort()
				print str(i) + ' -> ' + str(each)
		s.sort()
		print 'Rótulos usados: ' + str(s)
		return s
