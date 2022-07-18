from PySimpleGUI import PySimpleGUI as sg
from Usuario import Usuario
from Sistema import Sistema
from Selecao import Selecao
from Estadios import Estadios
from ApostaDoJogo import ApostaDoJogo
from Janela import Janela
import os
import time
from pygame import mixer


class Janela:

    def janela_login(self):
        layout = [
            [sg.Image(filename="./fotos/BETUSP.png", size=(1280, 720))],
            [sg.Text('Usuário'), sg.Input(key='user', size=(20, 1))],
            [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
            [sg.Button('Registrar', font='Verdana 14 italic bold underline'),
             sg.Button('Entrar', font='Verdana 14 italic bold underline')],
        ]

        return sg.Window('Login', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    def janela_usuario_ja_registrado(self):
        layout = [
            [sg.Text('Nome de usuário já registrado.')],
            [sg.Text('Tente outro.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    def janela_usuario_nao_registrado(self):
        layout = [
            [sg.Text('Nome de usuário não encontrado.')],
            [sg.Text('Registre ele para acessar o sistema.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso2')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    def janela_senha_incorreta(self):
        layout = [
            [sg.Text('Senha incorreta.')],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltarDoAviso3')]
        ]

        return sg.Window('Aviso', layout=layout, finalize=True, font='Verdana 14 italic bold',
                         element_justification='c')

    def janela_tabela(self):
        layout = [
            [sg.Image(filename="./fotos/grupos.png", size=(1280, 650))],
            [sg.Button('Grupo A', key='1', size=(11, 3)),
             sg.Button('Grupo B', key='2', size=(11, 3)),
             sg.Button('Grupo C', key='3', size=(11, 3)),
             sg.Button('Grupo D', key='4', size=(11, 3)),
             sg.Button('Grupo E', key='5', size=(11, 3)),
             sg.Button('Grupo F', key='6', size=(11, 3)),
             sg.Button('Grupo G', key='7', size=(11, 3)),
             sg.Button('Grupo H', key='8', size=(11, 3))],
            [sg.Button('Voltar', font='Verdana 12 italic bold underline', key='voltar2')]
        ]

        return sg.Window('Tabela', layout=layout, element_justification='c', font='Verdana 12 italic bold',
                         finalize=True)

    def janela_jogo(self, grupo):
        image = './fotos/bandeiras/grupo'

        vals = [['1', '2', '3', '4'], ['1', '3', '4', '2'], ['2', '3', '4', '1']]
        aposta = [['0', '0', '1', '1'], ['2', '2', '3', '3'], ['4', '4', '5', '5']]
        bets = [['0', '1'], ['2', '3'], ['4', '5']]
        tab = [0, 0, 0]

        for i in range(3):
            tab[i] = [
                [sg.Button('Estádio', key='estadio1' + str(i)),
                 sg.Button('',
                           image_filename=image + grupo + '/' + 'sel' + vals[i][0] + '.png', image_size=(200, 133),
                           image_subsample=2, border_width=0, key='time' + vals[i][0]),
                 sg.Input(key='aposta0' + aposta[i][0], size=(2, 1),font='Verdana 20 bold '),
                 sg.Text('x'),
                 sg.Input(key='aposta1' + aposta[i][1], size=(2, 1),font='Verdana 20 bold '),
                 sg.Button('',
                                   image_filename=image + grupo + '/' + 'sel' + vals[i][1] + '.png',
                                   image_size=(200, 133),
                                   image_subsample=2, border_width=0, key='time' + vals[i][1]),
                 sg.Text('R$'),
                 sg.Input(key='bet' + bets[i][0], size=(5, 1),font='Verdana 20 bold ')],
                [sg.Button('Estádio', key='estadio2' + str(i)),
                 sg.Button('',
                           image_filename=image + grupo + '/' + 'sel' + vals[i][2] + '.png', image_size=(200, 133),
                           image_subsample=2, border_width=0, key='time' + vals[i][2]),
                 sg.Input(key='aposta0' + aposta[i][2], size=(2, 1),font='Verdana 20 bold '),
                 sg.Text('x'),
                 sg.Input(key='aposta1' + aposta[i][3], size=(2, 1),font='Verdana 20 bold '),
                 sg.ReadFormButton('',
                                   image_filename=image + grupo + '/' + 'sel' + vals[i][3] + '.png',
                                   image_size=(200, 133),
                                   image_subsample=2, border_width=0, key='time' + vals[i][3]),
                 sg.Text('R$'),
                 sg.Input(key='bet' + bets[i][1], size=(5, 1),font='Verdana 20 bold ')]
            ]

        layout = [
            [sg.TabGroup([[
                sg.Tab('Primeira rodada', tab[0]),
                sg.Tab('Segunda Rodada', tab[1]),
                sg.Tab('Terceira Rodada', tab[2])]])],
            [sg.Button('Voltar', key='voltar3'), sg.Button('Apostar', key='apostar')]
        ]

        return sg.Window('Jogos do Grupo ' + grupo, layout=layout, finalize=True, element_justification='c',
                         font='Verdana 12 bold ')

    def janela_estadio(self, id_do_jogo):
        self.estagio = Estadios()
        return self.estagio.GUI(id_do_jogo);

    def janela_selecao(self, grupo, event):
        mixer.init()
        mixer.music.load(f'./hinos/grupo{grupo}/hino{event[4]}.mp3')  # cada grupo é um arquivo de 0 a 7 dentro os arquivos tem nome hino<i>.mp3 com i de 0 a 3
        nome_arquivo = f'./textos/selecoes/grupo{grupo}/text{event[4]}.txt'
        layout_info = Selecao(nome_arquivo).GUI()
        layout = [
            [sg.Image(f'./fotos/selecoes/grupo{grupo}/fot{event[4]}.png'),
             sg.Column(layout_info, vertical_alignment='top')],
            [sg.Text('Clique aqui para tocar o hino do país ->',font='Verdana 12 italic bold'),
            sg.Button('Play >',key='play',font='Verdana 10 underline'),
            sg.Button('Pause | |',key='pause',font='Verdana 10 underline')],
            [sg.Button('Voltar', key='voltar6')]
        ]

        return sg.Window('Seleção', layout=layout, finalize=True, element_justification='c')


if __name__ == '__main__':

    sg.theme('DarkRed')

    J = Janela()
    janela = 8 * [None]
    janela[0] = J.janela_login()

    grupo = '1'
    apostas = 48 * [None]

    for i in range(0, 48):
        apostas[i] = ApostaDoJogo(i)

    sistema = Sistema()
    usuario = Usuario()

    musica_tocando = 0

    while True:

        window, event, values = sg.read_all_windows()
        print(event)

        if window and event == sg.WIN_CLOSED:
            break

        if window == janela[1] and event == 'voltar2':
            janela[1].hide()
            janela[0].un_hide()

        if window == janela[2] and event == 'voltar3':
            janela[2].hide()
            janela[1].un_hide()

        if window == janela[3] and event == 'voltar4':
            janela[3].hide()
            janela[2].un_hide()

        if window == janela[0]:

            usuario.nome = str(values['user'])
            usuario.senha = str(values['senha'])
            usuario.saldo = 0

            if event == 'Entrar' and not sistema.usuario_registrado(usuario):

                janela[0].hide()
                janela[6] = J.janela_usuario_nao_registrado()

            elif event == 'Entrar' and not sistema.login_valido(usuario):

                janela[0].hide()
                janela[7] = J.janela_senha_incorreta()

            elif event == 'Entrar' and sistema.login_valido(usuario):

                janela[0].hide()
                janela[1] = J.janela_tabela()

            elif event == 'Registrar' and not sistema.usuario_registrado(usuario):

                usuario.ind = int(time.time())
                sistema.registrar_usuario(usuario)

            elif event == 'Registrar' and sistema.usuario_registrado(usuario):

                janela[0].hide()
                janela[5] = J.janela_usuario_ja_registrado()

        if window == janela[1] and event != 'voltar2':
            janela[1].hide()
            grupo = event
            janela[2] = J.janela_jogo(grupo)

        if window == janela[2] and event == 'apostar' or 'time' in event or 'estadio' in event:

            jogo = int(grupo) - 1
            num_do_jogo = int(jogo * 6)

            if event == 'apostar':
                print("aposta realizada")

                for i in range(6):
                    palpites = [values['aposta0' + str(i)], values['aposta1' + str(i)]]
                    valor_aposta = values['bet' + str(i)]
                    if (palpites[0].isdigit() and palpites[
                        1].isdigit() and valor_aposta.isdigit()):  # esse if impede que insira apostas inválidas
                        apostas[num_do_jogo].definir_aposta(palpites[0], palpites[1], valor_aposta)

                    num_do_jogo += 1

            sistema.escreve_recibo(usuario, apostas)

            if 'time' in event:
                janela[2].hide()
                janela[3] = J.janela_selecao(grupo, event)

            if 'estadio1' in event:
                if event[8] == '0':
                    pass
                elif event[8] == '1':
                    num_do_jogo = num_do_jogo + 2
                else:
                    num_do_jogo = num_do_jogo + 4

                print(num_do_jogo)
                janela[2].hide()
                janela[4] = J.janela_estadio(num_do_jogo)

            if 'estadio2' in event:
                if event[8] == '0':
                    num_do_jogo = num_do_jogo + 1
                elif event[8] == '1':
                    num_do_jogo = num_do_jogo + 3
                else:
                    num_do_jogo = num_do_jogo + 5

                print(num_do_jogo)
                janela[2].hide()
                janela[4] = J.janela_estadio(num_do_jogo)

        if window == janela[3] and event == 'play':
            mixer.music.play()
            musica_tocando = 1

        if window == janela[3] and event == 'pause':

            if (musica_tocando == 0):
                mixer.music.unpause()
                musica_tocando = 1

            elif (musica_tocando):
                mixer.music.pause()
                musica_tocando = 0

        if window == janela[3] and event == 'voltar6':
            janela[3].hide()
            janela[2].un_hide()

        if window == janela[4] and event == 'voltar5':
            janela[4].hide()
            janela[2].un_hide()

        if window == janela[5] and event == 'voltarDoAviso':
            janela[5].hide()
            janela[0].un_hide()

        if window == janela[6] and event == 'voltarDoAviso2':
            janela[6].hide()
            janela[0].un_hide()

        if window == janela[7] and event == 'voltarDoAviso3':
            janela[7].hide()
            janela[0].un_hide()
