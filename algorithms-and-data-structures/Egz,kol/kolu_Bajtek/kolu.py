from kolutesty import runtests

def projects(N, L):
	G = [[] for _ in range(N)]
	for p, q in L:
		G[q].append(p) #q umożliwia zrobienie p

	# toposort
	visited = [False] * N
	ordered = []
	def dfs(v):
		if visited[v]: return
		visited[v] = True
		for u in G[v]:
			dfs(u)
		ordered.append(v)
	for v in range(N):
		dfs(v)
	ordered = ordered[::-1] #toposort

	fin = [1] * N
	for v in ordered:
		for u in G[v]:
			fin[u] = max(fin[u], fin[v] + 1)

	return max(fin)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
