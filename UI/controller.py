import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._ddAnni = None


    def handleCreaGrafo(self,e):
        annoI = self._view._ddAnno1.value
        annoF = self._view._ddAnno2.value

        self._model.buildGraph(annoI, annoF)
        nodi, archi = self._model.getDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!", color = "red"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero archi: {archi}"))
        self._view.update_page()



    def handleDettagli(self, e):
        listaF, nc, nodiOrdinati = self._model.getOutput()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Archi di peso maggiore:", color="red"))
        for el in listaF:
            self._view.txt_result.controls.append(ft.Text(f"{el[0]} - {el[1]} ({el[2]} piloti condivisi)"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nc} componenti connesse", color="red"))
        self._view.txt_result.controls.append(ft.Text(f"Componente più grande ({len(nodiOrdinati)} nodi)", color="red"))
        for el in nodiOrdinati:
            self._view.txt_result.controls.append(ft.Text(f"{el}"))
        self._view.txt_result.controls.append(ft.Text("Componente connessa in ordine decrescente:", color="red"))
        for el in nodiOrdinati:
            self._view.txt_result.controls.append(ft.Text(f"{el}"))
        self._view.update_page()



    def handleCerca(self, e):
        pass

    def fillDDAnni(self):
        allAnni = self._model.getAllAnni()
        ddAnni = list(map(lambda y: ft.dropdown.Option(data=y, key=y, on_click=self._choiceAnni), allAnni))
        self._view._ddAnno1.options = ddAnni
        self._view._ddAnno2.options = ddAnni

    def _choiceAnni(self, e):
        self._ddAnni = e.control.data
        print(self._ddAnni)

