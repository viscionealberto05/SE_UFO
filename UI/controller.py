from pickletools import string1

import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare i dropdown """
        self._model.get_anni()

        for anno in self._model.lista_anni:
            self._view.dd_year.options.append(ft.dropdown.Option(anno))
        self._view.page.update()

        self._model.get_forme()

        for forma in self._model.lista_forme:
            self._view.dd_shape.options.append(ft.dropdown.Option(forma))


    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        self._model.forma = self._view.dd_shape.value
        self._model.anno = self._view.dd_year.value

        self._model.build_grafo()

        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Arco con {len(self._model.g.nodes)} nodi e {len(self._model.g.edges)} archi"))

        for key in self._model.dizionario_confinanti.keys():
            st1 = self._model.dizionario_stati[key]
            peso_tot = 0
            for value in self._model.dizionario_confinanti[key]:
                #st1 = self._model.dizionario_stati[key]
                st2 = self._model.dizionario_stati[value]
                if self._model.g.has_edge(st1, st2):
                    peso_arco = self._model.g[st1][st2]["weight"]
                    peso_tot += float(peso_arco)
                else:
                    pass
            self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Nodo {st1} ha peso: {peso_tot}"))

        self._view.page.update()


    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # TODO
