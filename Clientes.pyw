from tkinter import *

janelaClientes = Tk()
janelaClientes.geometry("595x200")
janelaClientes.title("Clientes") 

barraMenu = Menu(janelaClientes)
janelaClientes.config(menu = barraMenu)
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
barraMenu.add_cascade(label="Consultar",menu=subMenu3)
subMenu3.add_command(label="Nome do Cliente")
subMenu3.add_command(label="Telefone")
subMenu3.add_command(label="Endereço")
subMenu3.add_command(label="Bairro")
subMenu3.add_command(label="CPF")

frameCampos = Frame(janelaClientes)

separator1 = Frame(janelaClientes,height=2, bd=1, relief=RAISED)
separator2 = Frame(janelaClientes,height=2, bd=1, relief=RAISED)

labelTitulo = Label(text = "CADASTRO DE CLIENTES")

labelCód = Label(frameCampos,text = "Código do Cliente:")
entryCód = Entry(frameCampos,width=5)

labelNome = Label(frameCampos,text = "Nome do Cliente:")
entryNome = Entry(frameCampos,width=38)

labelEndereço = Label(frameCampos,text = "Endereço:")
entryEndereço = Entry(frameCampos,width=30)

labelCidade = Label(frameCampos,text = "Cidade:")
entryCidade = Entry(frameCampos,width=22)

labelBairro = Label(frameCampos,text = "Bairro:")
entryBairro = Entry(frameCampos,width=15)

labelTelefone = Label(frameCampos,text = "Telefone:")
entryTelefone = Entry(frameCampos,width=15)

labelNum = Label(frameCampos,text = "Nº:")
entryNum = Entry(frameCampos,width=6)

labelCPF = Label(frameCampos,text = "CPF:")
entryCPF = Entry(frameCampos,width=14)

botNovo = Button(text = "Novo")
botRegistrar = Button(text = "Cadastrar")
botExcluir = Button(text = "Excluir")

labelCód.grid(column=2, row=1)
entryCód.grid(column=3,row=1,sticky=W)

labelNome.grid(column=0, row=1,sticky=E)
entryNome.grid(column=1,row=1,sticky=W)

labelEndereço.grid(column = 0, row=2,sticky=E)
entryEndereço.grid(column = 1, row=2,sticky=W)

labelCidade.grid(column=0,row=3,sticky=E)
entryCidade.grid(column=1,row=3,sticky=W)

labelBairro.grid(column = 0, row=4,sticky=E)
entryBairro.grid(column = 1, row=4,sticky=W)

labelNum.grid(column = 1, row=2,sticky=E)
entryNum.grid(column = 2, row=2,sticky=W)

labelTelefone.grid(column = 0, row=5,sticky=E)
entryTelefone.grid(column = 1, row=5,sticky=W)

labelCPF.grid(column=0, row =6,sticky=E)
entryCPF.grid(column=1, row =6,sticky=W)

labelTitulo.pack()
separator1.pack(fill=X, padx=5, pady=5)

frameCampos.pack()

separator2.pack(fill=X, padx=5, pady=5)
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaClientes.mainloop()
