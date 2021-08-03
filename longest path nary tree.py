from collections import deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	
		def adjEdges(A):
			edges = {v: [] for v in range(len(A))}

			for i, n in enumerate(A):
				if n == -1:
					start = i
					continue
				edges[i].append(n)
				edges[n].append(i)
			return start, edges

		def BFS(edges, starting, flag):
			Q = deque()
			Q.appendleft((starting,0))
			visited = [False]*len(edges)
			visited[starting]=True
			while Q:
				node, d = Q.pop()
				neighb = edges[node]
				for n in neighb:
					if not visited[n]:
						Q.appendleft((n,d+1))
						visited[n]=True
			#last node will be the node with the largest distance from root node
			#i.e node
			if not flag:
				return node
			return d
		
		start, edges = adjEdges(A)
		return BFS(edges,BFS(edges, start,False), True)
