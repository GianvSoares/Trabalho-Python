from tkinter import *

janelaVendedor = Tk()
janelaVendedor.geometry("580x240")
janelaVendedor.title("Vendedor")  

barraMenu = Menu(janelaVendedor)
janelaVendedor.config(menu = barraMenu)
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
subMenu3.add_command(label="Cód.Vendedor")
subMenu3.add_command(label="Nome do Vendedor")
subMenu3.add_command(label="Por Data de Admissão")
subMenu3.add_command(label="Telefone")
subMenu3.add_command(label="Endereço")
subMenu3.add_command(label="CPF")
subMenu3.add_command(label="RG")

frameCampos = Frame(janelaVendedor)

separator1 = Frame(janelaVendedor,height=2, bd=1, relief=RAISED)
separator2 = Frame(janelaVendedor,height=2, bd=1, relief=RAISED)

labelTitulo = Label(text = "REGISTRO DE VENDEDORES")

labelCód = Label(frameCampos,text = "Código do Vendedor:")
entryCód = Entry(frameCampos,width=7)
labelCód.grid(column=0, row=0)
entryCód.grid(columnspan=5,column=1,row=0,sticky=W)

labelNome = Label(frameCampos, text = "Nome do Vendedor:")
entryNome = Entry(frameCampos,width=35)
labelNome.grid(column=0, row=1,sticky=E)
entryNome.grid(column=1,row=1,sticky=W)

labelData = Label(frameCampos, text = "Data de Admissão:")
entryData = Entry(frameCampos, width=11)
labelData.grid(column=0, row=2,sticky=E)
entryData.grid(column=1,row=2,sticky=W)

labelTelefone = Label(frameCampos,text = "Telefone:")
entryTelefone = Entry(frameCampos,width=18)
labelTelefone.grid(column = 0, row=3,sticky=E)
entryTelefone.grid(column = 1, row=3,sticky=W)

labelEndereço = Label(frameCampos,text = "Endereço:")
entryEndereço = Entry(frameCampos,width=26)
labelEndereço.grid(column = 0, row=4,sticky=E)
entryEndereço.grid(column = 1, row=4,sticky=W)

labelNum = Label(frameCampos,text = "Nº:")
entryNum = Entry(frameCampos,width=6)
labelNum.grid(column = 0, row=5,sticky=E)
entryNum.grid(column = 1, row=5,sticky=W)

labelCPF = Label(frameCampos,text = "CPF:",)
entryCPF = Entry(frameCampos,width=17)
labelCPF.grid(column=0, row =6,sticky=E)
entryCPF.grid(column=1, row =6,sticky=W)

labelRG = Label(frameCampos,text="RG:")
entryRG = Entry(frameCampos,width=25)
labelRG.grid(column=0, row =7,sticky=E)
entryRG.grid(column=1, row =7,sticky=W)

botNovo = Button(text = "Novo")
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

janelaVendedor.mainloop
