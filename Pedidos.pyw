from tkinter import *

janelaPedidos = Tk()
janelaPedidos.geometry("580x230")
janelaPedidos.title("Pedidos")

barraMenu = Menu(janelaPedidos)
janelaPedidos.config(menu = barraMenu)
subMenu = Menu(barraMenu)
barraMenu.add_cascade(label="Arquivo",menu=subMenu)
subMenu.add_command(label="Novo")
subMenu.add_command(label="Abrir")
subMenu.add_command(label="Salvar")
subMenu2 = Menu(barraMenu)
barraMenu.add_cascade(label="Editar",menu=subMenu2)
subMenu2.add_command(label="Desfazer")
subMenu2.add_command(label="Refazer")
subMenu3 = Menu(barraMenu)
barraMenu.add_cascade(label="Pesquisar",menu=subMenu3)
subMenu3.add_command(label="Pedidos")
subMenu3.add_command(label="Últimos Pedidos")

frameCampos = Frame(janelaPedidos)

separator1 = Frame(janelaPedidos,height=2, bd=1, relief=RAISED)
separator2 = Frame(janelaPedidos,height=2, bd=1, relief=RAISED)

labelTitulo = Label(text = "CONTROLE DE PEDIDOS")

labelNumP = Label(frameCampos,text="Nº do Pedido:")
entryNumP = Entry(frameCampos,width=7)
labelNumP.grid(column=0,row=0,sticky=E)
entryNumP.grid(column=1,row=0,sticky=W)

labelCód = Label(frameCampos,text = "Cód.Produto:")
entryCód = Entry(frameCampos,width=7)
labelCód.grid(column=0, row=1,sticky=E)
entryCód.grid(column=1,row=1,sticky=W)

labelVend = Label(frameCampos,text="Vendedor:")
entryVend = Entry(frameCampos,width=15)
labelVend.grid(column=0,row=2,stick=E)
entryVend.grid(column=1,row=2,sticky=W)

labelClie = Label(frameCampos,text="Cliente:")
entryClie = Entry(frameCampos,width=15)
labelClie.grid(column=3,row=2,stick=E)
entryClie.grid(column=4,row=2,sticky=W)

labelData = Label(frameCampos,text= "Data do Pedido:")
entryData = Entry(frameCampos,width=9)
labelData.grid(column=0,row=3,sticky=W)
entryData.grid(column=1,row=3,sticky=W)

labelPrd = Label(frameCampos,text = "Produto:")
entryPrd = Entry(frameCampos,width=15)
labelPrd.grid(column=0,row=4,sticky=E)
entryPrd.grid(column=1,row=4,sticky=W)

labelQtd = Label(frameCampos,text="Quantidade:")
entryQtd = Entry(frameCampos,width=5)
labelQtd.grid(column=0, row=5,sticky=E)
entryQtd.grid(column=1,row=5,sticky=W)

labelVlr = Label(frameCampos,text = "Valor Final:")
entryVlr = Entry(frameCampos,width=8)
labelVlr.grid(column=0,row=6,sticky=E)
entryVlr.grid(column=1,row=6,sticky=W)

botNovo = Button(text = "Novo",)
botRegistrar = Button(text = "Registrar")
botAlterar = Button(text = "Alterar")
botExcluir = Button(text = "Excluir")

labelTitulo.pack()
separator1.pack(fill=X, padx=5, pady=5)

frameCampos.pack()

separator2.pack(fill=X, padx=5, pady=5)
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaPedidos.mainloop
