# Algoritmul lui Tarjan pentru componente tare conexe (SCC)
# Autor: [numele tău]
# Limbaj: Python 3

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.index = [None] * n
        self.lowlink = [None] * n
        self.on_stack = [False] * n
        self.stack = []
        self.index_counter = 0
        self.components = []

    def add_edge(self, u, v):
        """Adaugă muchie orientată u -> v"""
        self.adj[u].append(v)

    def tarjan(self):
        """Determină toate componentele tare conexe"""
        for v in range(self.n):
            if self.index[v] is None:
                self._strongconnect(v)
        return self.components

    def _strongconnect(self, v):
        self.index[v] = self.index_counter
        self.lowlink[v] = self.index_counter
        self.index_counter += 1
        self.stack.append(v)
        self.on_stack[v] = True

        for w in self.adj[v]:
            if self.index[w] is None:
                self._strongconnect(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.on_stack[w]:
                self.lowlink[v] = min(self.lowlink[v], self.index[w])

        if self.lowlink[v] == self.index[v]:
            component = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                component.append(w)
                if w == v:
                    break
            self.components.append(component)


# ------------------ Exemplu de test ------------------

if __name__ == "__main__":
    g = Graph(8)

    edges = [
        (0, 1), (1, 2), (2, 0),
        (3, 1), (3, 2), (3, 4),
        (4, 5), (5, 6), (6, 4),
        (6, 7)
    ]
    for u, v in edges:
        g.add_edge(u, v)

    components = g.tarjan()

    print("Componentele tare conexe sunt:")
    for i, comp in enumerate(components, start=1):
        print(f"Componenta {i}: {comp}")
