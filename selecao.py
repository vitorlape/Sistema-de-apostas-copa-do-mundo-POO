import PySimpleGUI as sg
import os
import random

class selecao:

    def __init__(self, nome_arquivo):
        linhas = open(nome_arquivo, 'r').readlines()
        
        linhas = [linha[:-1] for linha in linhas]

        print(linhas)

        self.país = ' '.join(linhas[0].split(' ')[1:])
            
        self.jogadores = []

        i = 2
        while linhas[i].split(' ')[0] != 'Texto:':
            self.jogadores.append(linhas[i])
            i += 1

        self.texto = ' '.join(linhas[i].split(' ')[1:])
        i += 1

        while i < len(linhas):
            self.texto += linhas[i]
    
    def get_gui(self):
        linha1 = [sg.Text(self.país)]
        linha2 = [sg.Text('Elenco:')]
        linha3 = [sg.Column([[sg.Text(jogador)] for jogador in self.jogadores], scrollable = True, vertical_scroll_only = True)]
        linha4 = [sg.Text(self.texto, size = (60, None))]
        gui = [linha1, linha2, linha3, linha4]

        return gui


if __name__ == '__main__':
    arquivos = os.listdir('./arquivos')
    layout1 = selecao(f'./arquivos/{random.choice(arquivos)}').get_gui()
    layout2 = selecao(f'./arquivos/{random.choice(arquivos)}').get_gui()

    layout = [[sg.Column(layout1, vertical_alignment = 'top'), sg.Column(layout2, vertical_alignment = 'top')]]

    window = sg.Window('Teste', layout)

    while True:
        event, value = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break

    window.close()