from tkinter import *

janelaProduto = Tk()
janelaProduto.geometry("550x145")
janelaProduto.title("Produtos")

barraMenu = Menu(janelaProduto)
janelaProduto.config(menu = barraMenu)
subMenu = Menu(barraMenu)
barraMenu.add_cascade(label="Arquivo",menu=subMenu)
subMenu.add_command(label="Novo")
subMenu.add_command(label="Editar")
subMenu.add_command(label="Salvar")
subMenu.add_command(label="Ultimos Registros")
subMenu2 = Menu(barraMenu)
barraMenu.add_cascade(label="Editar",menu=subMenu2)
subMenu2.add_command(label="Desfazer")
subMenu2.add_command(label="Refazer")
subMenu3 = Menu(barraMenu)
barraMenu.add_cascade(label="Cadastrar",menu=subMenu3)
subMenu3.add_command(label="Código do Produto")
subMenu3.add_command(label="Produtos")
subMenu3.add_command(label="Quantidade em Estoque")


frameCampos = Frame(janelaProduto)

separator1 = Frame(janelaProduto,height=2, bd=1, relief=SUNKEN)
separator2 = Frame(janelaProduto,height=2, bd=1, relief=SUNKEN)

labelTitulo = Label(text = "PRODUTOS")

labelCód = Label(frameCampos,text = "Código do Produto:")
entryCód = Entry(frameCampos,width=10)

labelCód.grid(column=0, row=0)
entryCód.grid(column=1,row=0,sticky=W)

labelDescricao = Label(frameCampos,text = "Descrição:")
entryDescricao = Entry(frameCampos,width=20)

labelQuantidade = Label(frameCampos,text = "Quantidade:")
entryQuantidade = Entry(frameCampos,width=5)

labelValor = Label(frameCampos,text = "Valor:")
entryValor = Entry(frameCampos,width=12)

botNovo = Button(text = "Novo")
botRegistrar = Button(text = "Registrar")
botAlterar = Button(text = "Alterar")
botExcluir = Button(text = "Excluir")

labelDescricao.grid(column=0, row=1,sticky=E)
entryDescricao.grid(column=1,row=1,sticky=W)

labelQuantidade.grid(column = 0, row=2,sticky=E)
entryQuantidade.grid(column = 1, row=2,sticky=W)

labelValor.grid(column = 3, row=1)
entryValor.grid(column = 4, row=1)


labelTitulo.pack()
separator1.pack(fill=X, padx=5, pady=5)
frameCampos.pack()

separator2.pack(fill=X, padx=5, pady=5)
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaProduto.mainloop
