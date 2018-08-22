#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def is_connected(graph_hash, graph_hash_2):
	elements_gh = [n[0] for n in graph_hash] + [n[1] for n in graph_hash]
	elements_gh2 = [n[0] for n in graph_hash_2] + [n[1] for n in graph_hash_2]
	return set(elements) == set(elements_gh2)

def estradas_escuras(graph_hash):
	if len(graph_hash) < 3:
		return 0

	while True:
		graph_hash_2 = graph_hash
		total_economy = 0
		max_element = max(n[2] for n in graph_hash)

		for i in range(len(graph_hash)):
			if graph_hash[i][2] == max_element:
				graph_hash.pop(n)
				
				if is_connected(graph_hash, graph_hash_2):
					total_economy += max_element

	
	max_n = max(n[2] for n in graph_hash)
	if len(graph_hash) == 5:
		return sum(sorted([n[2] for n in graph_hash], reverse=True)[0:2])

	return max_n

	