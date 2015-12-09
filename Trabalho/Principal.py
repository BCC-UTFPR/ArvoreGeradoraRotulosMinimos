#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from collections import defaultdict,deque
from colorama import Fore, Back, Style

def ler_arquivo(nome_do_arquivo):
	print Fore.WHITE + 'Fazendo a leitura do arquivo...'
	arquivo = open(nome_do_arquivo,'r')
	arquivo = arquivo.readlines()
	print Fore.GREEN + 'PRONTO!'
	return arquivo

def gerar_vertices(arquivo):
	print Fore.WHITE + 'Carregando os nós do arquivo...'
	lista_de_vertices = []
	for linha in arquivo:
		linha = linha.split()
		if len(linha) > 1:
			if linha[0] not in lista_de_vertices:
				lista_de_vertices.append(linha[0])
			if linha[1] not in lista_de_vertices:
				lista_de_vertices.append(linha[1])
	lista_de_vertices.sort()
	print Fore.GREEN + 'PRONTO!'
	return lista_de_vertices

class Grafo:
  def __init__(self):
    self.vertices = set()
    self.arestas = defaultdict(list)
    self.distancias = {}

  def adiciona_vertice(self, vertice):
    self.vertices.add(vertice)

  def adiciona_aresta(self, de_vertice, para_vertice, distancia):
    self.arestas[de_vertice].append(para_vertice)
    self.arestas[para_vertice].append(de_vertice)
    self.distancias[(de_vertice, para_vertice)] = distancia

def shortest_path(grafo, origem, destino):
	visitados, caminho = dijsktra(grafo, origem)
	caminho_final = deque()
	vertice_destino = caminho[destino]
    
	while vertice_destino != origem:
		caminho_final.appendleft(vertice_destino)
		vertice_destino = caminho[vertice_destino]
		
	caminho_final.appendleft(origem)
	caminho_final.append(destino)
	
	return visitados[destino], list(caminho_final)
	
def dijsktra(grafo, vertice_inicial):
	visitados = {vertice_inicial: 0}
	caminho = {}
	vertices = set(grafo.vertices)

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

		for vertice_conectado in grafo.arestas[vertice_minimo]:
			try:
				peso = peso_vertice_minimo + grafo.distancias[(vertice_minimo,vertice_conectado)]
				if vertice_conectado not in visitados or peso < visitados[vertice_conectado]:
					visitados[vertice_conectado] = peso
					caminho[vertice_conectado] = vertice_minimo
			except KeyError,e:
				continue
				
	return visitados,caminho
     
if __name__ == '__main__':

	arquivo = ler_arquivo('rotas-cem-mil.txt')
	vertices = gerar_vertices(arquivo)
	grafo = Grafo()
	
	for vertice in vertices:
		grafo.adiciona_vertice(int(vertice))
		
	for linha in arquivo:
		linha = linha.split()
		if len(linha) > 1:
			vertice_de = int(linha[0])
			vertice_para = int(linha[1])
			grafo.adiciona_aresta(vertice_de,vertice_para,abs(round(vertice_para - vertice_de)))

	while(True):
		print Fore.WHITE + 'Caminho mínimo: '
		vertice_de = raw_input('Digite a cidade inicial: ')
		vertice_para = raw_input('Digite a cidade final: ')
		print(Fore.GREEN + str(shortest_path(grafo,int(vertice_de),int(vertice_para))))
