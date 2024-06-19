from tkinter import *

root = Tk()

# Tela de cadastro de supervisores
class Application():
    def __init__(self):
        self.root = root
        self.tela()  # Tela principal para cadastro de supervisores
        self.frames_da_tela()  # Chamando a função frames da tela
        self.criando_botoes()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Supervisores")
        self.root.configure(background='#1e3743')  # Pode ser uma imagem  
        self.root.geometry("700x500")  # Altura da
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)  # Largura da tela
        self.root.minsize(width=400, height=300)
        
    def frames_da_tela(self):  # Estão com responsividade
        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)  # Cor da borda
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)  # Começo lado esquerdo, e começo de baixo        
        self.frame_2 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3)  # Cor da borda        
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)  # Começo lado esquerdo, e começo de baixo
        
    def criando_botoes(self):
        # Criando botões
        self.bt_limpar = Button(self.frame_1, text="Limpar")  # Dentro do frame 1
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text="Buscar")  # Dentro do frame 1
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text="Novo")  # Dentro do frame 1
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text="Alterar")  # Dentro do frame 1
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text="Apagar")  # Dentro do frame 1
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Criando labels e entradas
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.15)

Application()
