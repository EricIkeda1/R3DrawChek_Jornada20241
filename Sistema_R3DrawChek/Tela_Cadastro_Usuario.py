from tkinter import *

root = Tk()
#tela de cadastro de supervisores in
class Application():
    def __init__(self):
        self.root = root
        self.tela()# tela principal para cadastro de supervisores
        self.frames_da_tela()#chamando a funcao frames da tela
        self.criando_botoes()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Supervisores")
        self.root.configure(background='#1e3743')#pode ser uma imagem  
        self.root.geometry("700x500")#altura da
        self.root.resizable(True,True)
        self.root.maxsize(width = 900, height = 700)#largura da tela
        self.root.minsize(width = 400, height = 300)
        
    def frames_da_tela(self):#estão com responsividade
        self.frame_1 = Frame(self.root, bd= 4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3) #cor da borda
        self.frame_1.place(relx= 0.02, rely = 0.02, relwidth= 0.96, relheight= 0.46)#comeco lado esquerdo, e comeco de baixo        
        self.frame_2 = Frame(self.root, bd= 4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=3) #cor da borda        
        self.frame_2.place(relx= 0.02, rely = 0.5, relwidth= 0.96, relheight= 0.46)#comeco lado esquerdo, e comeco de baixo
        
    def criando_botoes(self):
        #criando botao limpar
        self.bt_limpar = Button(self.frame_1, text = "Limpar" )#dentro do frame 1
        self.bt_limpar.place(relx= 0.2, rely = 0.1, relwidth = 0.1, relheight= 0.15)
        #criando botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar")#dentro do frame 1
        self.bt_buscar.place(relx= 0.3, rely = 0.1, relwidth = 0.1, relheight= 0.15)
        #criando botao novo
        self.bt_novo = Button(self.frame_1, text="Novo")#dentro do frame 1
        self.bt_novo.place(relx= 0.6, rely = 0.1, relwidth = 0.1, relheight= 0.15)
        #criando botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar")#dentro do frame 1
        self.bt_alterar.place(relx= 0.7, rely = 0.1, relwidth = 0.1, relheight= 0.15)     
        #criando botao apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar")#dentro do frame 1
        self.bt_apagar.place(relx= 0.8, rely = 0.1, relwidth = 0.1, relheight= 0.15)   
        
        ##criando as labes e entradas
        self.lb.codigo = Label(self.frame_1, text = "Código")
        self.codigo.place(relx= 0.8, rely = 0.1, relwidth = 0.1, relheight= 0.15)  
        
Application()