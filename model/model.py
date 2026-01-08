from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.lista_stati = []
        self.lista_avvistamenti = []
        self.dizionario_confinanti = {}
        self.dizionario_stati = {}
        self.g = nx.Graph()

        self.forma = ""
        self.anno = ""

        #self.load_dizionario_stati()

        #self.load_vicini()

    def get_anni(self):
        self.lista_anni = DAO.get_anni()

    def get_forme(self):
        self.lista_forme = DAO.get_forme()

    def get_nodi(self):
        self.lista_stati = DAO.get_stati()

    def load_vicini(self):
        lista_tuple = DAO.get_vicini()

        for tupla in lista_tuple:
            if tupla[0] not in self.dizionario_confinanti.keys():
                self.dizionario_confinanti[tupla[0]] = [tupla[1]]
            else:
                if tupla[1] not in self.dizionario_confinanti[tupla[0]]:
                    self.dizionario_confinanti[tupla[0]].append(tupla[1])

        print(self.dizionario_confinanti)

    def load_dizionario_stati(self):
        for stato in self.lista_stati:
            self.dizionario_stati[stato.id] = stato

    def build_grafo(self):
        """for stato in self.lista_stati:
            for key in self.dizionario_confinanti.keys():
                if stato.id == key:
                    for vicino in self.dizionario_confinanti[key]:
                        if esiste_arco(key,vicino):
                            pass
                        else:
                            stato_vicino = associa_stato_a_id(vicino)
                            self.g.add_edge(stato,vicino)"""

        self.dizionario_confinanti = {}
        self.dizionario_stati = {}

        self.g.clear()

        self.get_nodi()
        self.load_dizionario_stati()
        self.load_vicini()
        self.g.add_nodes_from(self.lista_stati)

        self.lista_archi = DAO.get_edges(str(self.forma),str(self.anno))

        for arco in self.lista_archi:
            st1 = self.dizionario_stati[arco[0]]
            st2 = self.dizionario_stati[arco[1]]
            if self.g.has_edge(st1,st2) or self.g.has_edge(st2,st1):
                #self.g[st1][st2]['weight'] += arco[2] #grafo semplice non orientato
                pass
            else:
                self.g.add_edge(st1,st2,weight=arco[2])

        print(self.g)