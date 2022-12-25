import PySimpleGUI as sg
import mysql_cfg as db

#--------------------------------------------------------------------------------------------------------------

# TELA INICIAL COM OPÇOES DE SUB TELAS CADASTRO DE PRODUTOS, REMOVER PRODUTOS, ATUALIZAR ESTOQUE, DISPONIVEL EM ESTOQUE 
def inicialMenu():
    sg.theme('Dark Grey 13')
    layout_inicial= [
        [sg.Button('Cadastrar Produto',key='cadastrarproduto',size=(20,2),border_width=5,pad=(2,10))],
        [sg.Button("Remover Produto",key='removerproduto',size=(20,2),border_width=5,pad=(2,10))],
        [sg.Button("Atualizar Estoque",key='atualizarestoque',size=(20,2),border_width=5,pad=(2,10))],
        [sg.Button("Disponivel em Estoque",key='disponivelestoque',size=(20,2),border_width=5,pad=(2,10))],
        [sg.Text()]
    ]
    # Output imprimir para o usuario os dados
    layout_output= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text()],
        [sg.Text('   BEM VINDO AO SISTEMA DE CONTROLE DE ESTOQUE',font='2',text_color='red')],
        [sg.Text()],
        [sg.Text('   Este é um sistema simples para auxiliar no controle do seus estoque',font='5')],
        [sg.Text('   Sistema integrado com Banco de dados para maior segurança dos seus registros',font='5')],
        [sg.Text('   Tambem podemos deixar esse banco de dados em um servidor para multiplos usuarios',font='5')],
        [sg.Text('   consigam acessar e alterar simultaneamente seu estoque .',font='5')],
        [sg.Text('   Dev Adrian R',font='3',text_color='green')],
        [sg.Text()]
    ]
    layout = [  # Cadastro de produto c/ output
        [sg.Column(layout_inicial),sg.VerticalSeparator(),sg.Column(layout_output)]
        ]
    return sg.Window('Tela Inicial', layout,margins=(10,10),finalize=True)

# TELA DE CADASTRO DE PRODUTOS
def cadastroMenu():
    sg.theme('Dark Grey 13')
    layout_cadastroA= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text()],
        [sg.Text('Preencha os campos abaixo para adicionar um novo produto aoo seu estoque')],
        [sg.Text('Informe o codigo do produto',font='3')],
        [sg.Text('Codigo:  '), sg.Input(key='cod',size=(25,1))],
        [sg.Text()],
        [sg.Text('Informe o nome do produto',font='3')],
        [sg.Text('Nome Produto:  '), sg.Input(key='nomep',size=(25,1))],
        [sg.Text()],
        [sg.Text('Informe a quantidade deste produto',font='3')],
        [sg.Text('Quantidade:  '), sg.Input(key='qts',size=(25,1))],
        [sg.Text()],
        [sg.Button('Cadastrar',font=5,pad=(10,10),button_color='green'),sg.Button('Voltar',font=5,button_color='red')]
    ]
    # Output imprimir para o usuario os dados
    layout_output= [
        [sg.Text('PRODUTOS CADASTRADOS')],
        [sg.Output(size=(70,25))]
    ]
    layout = [  # Cadastro de produto c/ output
        [sg.Column(layout_cadastroA),sg.VerticalSeparator(),sg.Column(layout_output)]
        ]
    return sg.Window('CADASTRAR PRODUTOS', layout,margins=(10,10),finalize=True)

# TELA DE REMOVER PRODUTOS
def removerMenu():
    sg.theme('Dark Grey 13')
    layout_cadastroA= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text()],
        [sg.Text()],
        [sg.Text('Preencha os campos abaixo para excluir um produto do seu estoque')],
        [sg.Text()],
        [sg.Text('Informe o codigo do produto que deseja excluir',font='3')],
        [sg.Text()],
        [sg.Text('Codigo:  '), sg.Input(key='cod',size=(25,1))],
        [sg.Text()],
        [sg.Button('Remover',font=5,pad=(10,10),button_color='green'),sg.Button('Voltar',font=5,button_color='red')]
    ]
    # Output imprimir para o usuario os dados
    layout_output= [
        [sg.Text('PRODUTOS DISPONIVEIS EM ESTOQUE')],
        [sg.Output(size=(70,25))]
    ]
    layout = [  # Cadastro de produto c/ output
        [sg.Column(layout_cadastroA),sg.VerticalSeparator(),sg.Column(layout_output)]
        ]
    return sg.Window('REMOVER PRODUTOS', layout,margins=(10,10),finalize=True)

# TELA DE ATUALIZAR PRODUTOS
def atualizarMenu():
    sg.theme('Dark Grey 13')
    list = ['Adicionar valor','Remover valor','Alterar valor']
    layout_cadastroA= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text()],
        [sg.Text('Preencha os campos abaixo para Alterar a quantidade em estoque')],
        [sg.Text()],
        [sg.Text('Informe o codigo do produto que deseja alterar',font='3')],
        [sg.Text('Codigo:  '), sg.Input(key='cod',size=(25,1))],
        [sg.Text()],
        [sg.Text('Escolha a operação que deseja realizar',font='3')],
        [sg.OptionMenu(list,default_value='Adicionar valor',key='menu')],
        [sg.Text()],
        [sg.Text('Informe a quantidade que deseja atualizar',font='3')],
        [sg.Text('Quantidade:  '), sg.Input(key='qts',size=(25,1))],
        [sg.Button('Atualizar',font=5,pad=(10,10),button_color='green'),sg.Button('Voltar',font=5,button_color='red')]
    ]
    # Output imprimir para o usuario os dados
    layout_output= [
        [sg.Text('ESTOQUE ATUAL')],
        [sg.Output(size=(70,25))]
    ]
    layout = [  # Cadastro de produto c/ output
        [sg.Column(layout_cadastroA),sg.VerticalSeparator(),sg.Column(layout_output)]
        ]
    return sg.Window('ATUALIZAR PRODUTOS', layout,margins=(10,10),finalize=True)

# TELA DE ATUALIZAR PRODUTOS
def EstoqueMenu():
    sg.theme('Dark Grey 13')
    layout_cadastroA= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text('INFORMAÇÕES',font=3,pad=5)],
        [sg.Text('Neste opção voce consegue visualizar todos Produtos Disponiveis em seu estoque')],
        [sg.Text('facilitando o controle de seus produtos e agilizando a gestao do seu negocio !')],
        [sg.Text()],
        [sg.Text('OBJETIVO DO PROJETO',font=3,pad=5)],
        [sg.Text('Nosso projeto tem como Objetivo ajudar pequenos e quandes negocios a terem um controle')],
        [sg.Text('mais facil e rapido sobre seu estoque, sabemos que vender um produto que voce nao tem')],
        [sg.Text('a pronta entrega gera um grande stress, nosso objetivo e auxiliar voce comerciante nesta questao')],
        [sg.Text()],
        [sg.Text('Esperamos de coração conseguir ajudar e atender sua necessidades com esse projeto gratis e simples')],
        [sg.Text('Caso voce tenha dificuldade com o uso ficamos a disposição para auxilia-los.')],
        [sg.Text('Tambem aceitamos novos desafios, que tal ter um sistema Unico e somente para sua empresa ?')],
        [sg.Text('Podemos fazer um sistema complexo para atender todas suas necessidades e demandas facilitando sua rotina')],
        [sg.Text()],
        [sg.Text('CREDITOS',font=3,pad=5)],
        [sg.Text('Creditos ao Criador / Dev: Adrian R. (Pezao XD)')],
        [sg.Button('Doacoes',font=5,pad=(10,10),button_color='green'),sg.Button('Voltar',font=5,button_color='red')]
    ]
    # Output imprimir para o usuario os dados
    layout_output= [
        [sg.Text('ESTOQUE ATUAL')],
        [sg.Output(size=(70,40))]
    ]
    layout = [  # Cadastro de produto c/ output
        [sg.Column(layout_cadastroA),sg.VerticalSeparator(),sg.Column(layout_output)]
        ]
    return sg.Window('DISPONIVEL EM ESTOQUE', layout,margins=(10,10),finalize=True)

# TELA NOTIFY
def Notify():
    sg.theme('Dark Grey 13')
    layout_inicial= [
        [sg.Image('logo.png',pad=(2,4))],
        [sg.Text()],
        [sg.Text('AJUDA PARA O CAFEZINHO RSRSRS',font='2',text_color='green')],
        [sg.Text()],
        [sg.Text('Não cobramos nada pelo uso deste programa e nem pelo suporte caso necessario')],
        [sg.Text('Porem aceitamos Doações como forma de agradecimento pelo tempo e esforços aqui investidos')],
        [sg.Text('Não importa o valor toda quantia é bem vinda, essa doação serve como incentivo para nosso trabalho')],
        [sg.Text('São muitas horas sem dormir e longas madrugadas viradas em busca de conhecimento para melhoras nossos projetos')],
        [sg.Text('Caso queira contribuir com nossa bebedeira tambem aceitamos aquele wisky / voska rsrsrs')],
        [sg.Text()],
        [sg.Text('Pix: adrianritidasilva18@gmail.com',font=3,text_color='red')],
        [sg.Button('Voltar',font=5,button_color='red')],
        [sg.Text()]
    ]
    return sg.Window('AJUDE UM DEV ', layout_inicial,margins=(10,10),finalize=True)

def verifCod(cod): # Verifica se o codigo do produto já existe no banco de dados (Evita duplicidade e bugs)
    result = db.select()
    codExistente = False
    for x in result:
        if int(cod) == int(x[0]):
            codExistente = True
    return codExistente

def verifCod2(cod): # Verifica se o codigo do produto já existe no banco de dados (Evita duplicidade e bugs)
    result = db.select()
    codExistente = False
    valoratual = None
    for x in result:
        if int(cod) == int(x[0]):
            codExistente = True
            valoratual = x[2]
    return codExistente,valoratual

def disponivelEstoque():
    result = db.select()
    for p in result:
        print(f"Codigo: {p[0]} | Produto: {p[1]} | Quantidade: {p[2]}")
    
'''
    janela1 = Menu inicial
    janela2 = Cadastro de produtos
    Janela3 = Remover Produtos
    Janela4 = Atualizar Estoque
    janela5 = Disponivel em Estoque

'''
# Criar janelas

janela1, janela2, janela3, janela4, janela5, notify = inicialMenu(), None, None, None, None, None


while True:
    window, eventos, valores = sg.read_all_windows()

    # EVENTO PARA BREKAR O LOOP E ENCERRAR O PRODGRAMA

    if eventos == sg.WINDOW_CLOSED or eventos == 'Cancelar' or eventos == 'Sair':
        break
    # ABRE A JANELA DE CADASTRO E ESCONDE A JANELA MENUINICIAL

    if window == janela1 and eventos == 'cadastrarproduto':
        janela1.hide()
        janela2 = cadastroMenu()
    # ABRE A JANELA DE REMOVER PRODUTO E ESCONDE A JANELA MENUINICIAL

    if window == janela1 and eventos == 'removerproduto':
        janela1.hide()
        janela3 = removerMenu()
        disponivelEstoque()

    # ABRE A JANELA DE ATUALIZAR ESTOQUE E ESCONDE A JANELA MENUINICIAL

    if window == janela1 and eventos == 'atualizarestoque':
        janela1.hide()
        janela4 = atualizarMenu()
        disponivelEstoque()
    # ABRE A JANELA DE DISPONIVEL EM ESTOQUE E ESCONDE A JANELA MENUINICIAL

    if window == janela1 and eventos == 'disponivelestoque':
        janela1.hide()
        janela5 = EstoqueMenu()
        disponivelEstoque()
    # FECHA A TELA ATUAL E RETORNA AO MENU INICIAL

    if eventos == 'Voltar':
        if window == janela2:
            janela2.hide()
        elif window == janela3:
            janela3.hide()
        elif window == janela4:
            janela4.hide()
        elif window == janela5:
            janela5.hide()
        elif window == notify:
            notify.hide()
            continue
        janela1.un_hide()

    if window == janela2 and eventos == 'Cadastrar':
        #Verifica se o evento for vazio passa ela para var como None

        cod = valores['cod'] or None
        nomep = valores['nomep'].upper() or None
        qts = valores['qts'] or None

        # Verifica se todos campos foram preenchidos
        if cod != None and nomep != None and qts != None:
            codExistente = verifCod(cod)
            if codExistente == True:
                sg.popup('O codigo informado já esta sendo usando em outro Produto')
            if codExistente == False:
                registro = f"Adicionado - Codigo: {cod}  |  Produto: {nomep}  |  Quantidade: {qts}"
                print(registro)
                db.add(cod,nomep,qts)

                #ADICIONAR A FUNCAO QUE SALVA O HISTORICO DE AÇOES REALZIADAS
        else:
            sg.popup('Para continuar você precisa preencher todos os campos')

    if window == janela3 and eventos == 'Remover':
        cod = valores['cod'] or None
        if cod != None:
            codExistente = verifCod(cod)
            if codExistente == True:
                db.rem('codigo',cod)
            else:
                sg.popup('O codigo informado não esta cadastrado em seu Estoque ')
        else:
            sg.popup('Preencha o campo CODIGO para conseguir deletar um Produto')
    
    if window == janela4 and eventos == 'Atualizar':
        cod = valores['cod'] or None
        qts = valores['qts'] or None
        opmenu = valores['menu']
        if cod != None and qts != None:
            codExistente, atualvalor = verifCod2(cod)
            atualvalor = int(atualvalor)
            cod,qts = int(cod), int(qts)
            if codExistente == True:
                if opmenu == 'Alterar valor':
                    db.update('quantidade',qts,cod)
                elif opmenu == 'Adicionar valor':
                    qts = atualvalor + qts
                    db.update('quantidade',qts,cod)
                elif opmenu == 'Remover valor':
                    if atualvalor < qts:
                        sg.popup('Você não pode Remover mais unidades doque voce tem disponivel em estoque')
                    if atualvalor >= qts:
                        qts = atualvalor - qts
                        db.update('quantidade',qts,cod)
            else:
                sg.popup('O codigo informado não esta cadastrado em seu Estoque ')
        else:
            sg.popup('Preencha o campo CODIGO e QUANTIADE para conseguir Atualizar a quantidade de um Produto')
        
    if window == janela5 and eventos == 'Doacoes':        
        notify = Notify()