import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()

        self._idMapC = {}
        for el in DAO.getAllCostruttori():
            self._idMapC[el.constructorId] = el


    def getAllAnni(self):
        return DAO.getAllYears()

    def buildGraph(self, annoI, annoF):
        self._grafo.clear()
        costruttori = DAO.getCostruttori(annoI, annoF)
        for el in costruttori:
            self._grafo.add_node(self._idMapC[el])
        myEdges = DAO.getAllEdges(annoI, annoF)
        for el in myEdges:
            self._grafo.add_edge(self._idMapC[el[0]], self._idMapC[el[1]], weight = el[2])

    def getDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getOutput(self):
        lista = sorted(self._grafo.edges(data=True), key=lambda x: x[2]["weight"], reverse=True)
        listaF = lista[:3]
        risultato = []
        for u, v, data in listaF:
            peso = data.get('weight')
            risultato.append((u, v, peso))
        nC = nx.number_connected_components(self._grafo)
        massimo = max(nx.connected_components(self._grafo), key=len)
        subgraph = self._grafo.subgraph(massimo).copy()
        nodiOrdinati = sorted(subgraph.nodes(), key=lambda x: self._grafo.degree(x), reverse = True)
        return risultato, nC, nodiOrdinati


