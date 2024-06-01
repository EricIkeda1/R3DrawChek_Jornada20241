import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Define o título da janela e seu tamanho
        self.title("R3 DrawCheck - V1.0.0")
        self.geometry("1200x800")

        # Cria o menu superior
        self.create_menu()

        # Cria a barra de busca
        self.create_search_bar()

        # Cria os frames principais
        self.create_frames()

        # Cria o rodapé
        self.create_footer()

    def create_menu(self):
        # Cria a barra de menus
        menubar = Menu(self)
        
        # Adiciona o menu "Arquivo"
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Novo")
        file_menu.add_command(label="Abrir")
        file_menu.add_command(label="Salvar")
        file_menu.add_command(label="Salvar como...")
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.quit)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        
        # Adiciona o menu "Editar"
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Desfazer")
        edit_menu.add_command(label="Refazer")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar")
        edit_menu.add_command(label="Copiar")
        edit_menu.add_command(label="Colar")
        menubar.add_cascade(label="Editar", menu=edit_menu)
        
        # Adiciona o menu "Ferramentas"
        tools_menu = Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Opções")
        menubar.add_cascade(label="Ferramentas", menu=tools_menu)
        
        # Adiciona a opção "Sair" diretamente na barra de menus
        menubar.add_command(label="Sair", command=self.quit)
        
        # Configura a janela principal para usar a barra de menus criada
        self.config(menu=menubar)

    def create_search_bar(self):
        # Cria um frame para a barra de busca
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Cria e adiciona o label "Buscar Projeto Número:" ao frame de busca
        search_label = ttk.Label(search_frame, text="Buscar Projeto Número:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Cria e adiciona a caixa de entrada (Entry) para a busca
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Cria e adiciona o botão "Buscar" ao frame de busca
        search_button = ttk.Button(search_frame, text="Buscar", command=self.search_project)
        search_button.pack(side=tk.LEFT, padx=(5, 0))

    def create_frames(self):
        # Cria um frame principal para organizar os frames internos
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Cria o frame da esquerda
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Adiciona um label e um canvas para o desenho original no frame da esquerda
        original_drawing_label = ttk.Label(left_frame, text="Desenho Original")
        original_drawing_label.pack(fill=tk.X)
        
        original_drawing_canvas = tk.Canvas(left_frame, width=200, height=300, bg="white")
        original_drawing_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Adiciona um label e um campo de texto para normas no frame da esquerda
        standards_label = ttk.Label(left_frame, text="Normas")
        standards_label.pack(fill=tk.X, pady=(10, 0))
        
        standards_text = tk.Text(left_frame, height=10)
        standards_text.pack(fill=tk.BOTH, expand=True)
        
        # Cria o frame central
        center_frame = ttk.Frame(main_frame)
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Adiciona um label e um canvas para o desenho em análise no frame central
        analysis_drawing_label = ttk.Label(center_frame, text="Desenho em Análise")
        analysis_drawing_label.pack(fill=tk.X)
        
        analysis_drawing_canvas = tk.Canvas(center_frame, bg="white")
        analysis_drawing_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Cria o frame da direita
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Adiciona um label e um campo de texto para os dados abstraídos no frame da direita
        abstracted_data_label = ttk.Label(right_frame, text="Dados Abstraídos")
        abstracted_data_label.pack(fill=tk.X)
        
        abstracted_data_text = tk.Text(right_frame)
        abstracted_data_text.pack(fill=tk.BOTH, expand=True)

    def create_footer(self):
        # Cria um frame para o rodapé
        footer_frame = ttk.Frame(self)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Adiciona um label com o título do sistema ao rodapé
        footer_label = ttk.Label(footer_frame, text="R3 DrawCheck - V1.0.0")
        footer_label.pack()

    def search_project(self):
        # Lógica de busca do projeto - pode ser personalizada conforme necessário
        project_number = self.search_entry.get()
        print(f"Buscando projeto número: {project_number}")

if __name__ == "__main__":
    # Inicializa e executa a aplicação
    app = Application()
    app.mainloop()
