# coding=UTF-8
import time
import MLST

class Reader:
	def read_graph_file(self,file_name):
		graph_list = []
		graph = []
		with open(file_name) as lines:
			graph_size = lines.readline().split()
			for line in lines:
				if line.replace('\r','') != '\n':			
					graph.append(line.rstrip().split())
				else:
					graph_list.append(graph)
					graph = []
		return graph_list,graph_size					
				
reader = Reader()
chromosome_class = MLST.Chromosome()
crossover_class = MLST.Crossover()
mutation_class = MLST.Mutation()
label_quantity = []
graph_list,graph_size = reader.read_graph_file('HDGraph50_50.txt')
size = int(graph_size[0])
time_list = []
time_total = time.clock()
for graph_position,graph in enumerate(graph_list):
	time_per_graph = time.clock()
	chromosome_a = chromosome_class.chromosome(graph,size)
	chromosome_b = chromosome_class.chromosome(graph,size)
	if chromosome_a and chromosome_b != None:
		label_used = list(set(chromosome_a) | set(chromosome_b))
		S = crossover_class.crossover(label_used,graph,size)
		S = mutation_class.mutation(S,graph,size)
		label_quantity.append(len(S))
		time_list.append(graph_position)
		time_list.append((time.clock() - time_per_graph)/60)

print 'Média'
print  reduce(lambda x, y: x + y, label_quantity)/len(label_quantity)
print 'Tempo de execução total: ' + str(time.clock() - time_total)

"""
print 'A melhor das soluções nos dá uma árvore geradora de rótulos mínimos utilizando a menor quantidade de rótulos possível.'
print 'Para isso, serão gerados diversos indivíduos, combinados até encontrarmos um conjunto de rótulos S de tamanho mínimo.'
print 'Isso irá custar um maior tempo de execução, sendo que pra grandes conjuntos, pode-se demorar horas e horas...'
decision = raw_input('Você terminou de ver o resultado para uma solução simples. Deseja ver a melhor das soluções (mais custosa)? S/N?' )

if decision == 'S':
	for graph_position,graph in enumerate(graph_list):
		chromosome_a = chromosome_class.chromosome(graph,size)
		chromosome_b = chromosome_class.chromosome(graph,size)
		if chromosome_a and chromosome_b != None:
			label_used = list(set(chromosome_a) | set(chromosome_b))
			S = crossover_class.crossover(label_used,graph,size)
			S = mutation_class.mutation(S,graph,size)
			raw_input('Este é o resultado do Grafo (' + str(graph_position + 1) + '). Aperte ENTER para prosseguir.')
"""
