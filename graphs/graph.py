class Graph:

    def __int__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, value):
        if value in self.graph:
            return
        self.graph[value] = {}

    def add_edge(self, start, end, weight=1):
        self.add_vertex(start)
        self.add_vertex(end)

        if end not in self.graph[start]:
            self.graph[start][end] = weight

        if not self.directed and start not in self.graph[end]:
            self.graph[end][start] = weight

    def bfs(self, start):
        visited, current = set([start]), [start]
        while current:
            vertex = current.pop(0)
            for edge in self.graph[vertex]:
                if edge not in visited:
                    visited.add(edge)
                    current.append(edge)

    def dfs(self, value, visited=None):
        if visited is None:
            visited = set()

        visited.add(value)
        for edge in self.graph[value]:
            if edge not in visited:
                self.dfs(edge, visited)

    def dfs_iterative(self, start):
        visited, current = set([start]), [start]
        while current:
            vertex = current.pop()
            for edge in self.graph[vertex]:
                if edge not in visited:
                    visited.add(edge)
                    current.append(edge)

