import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class CadastroNormas(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Define o título da janela e seu tamanho
        self.title("Cadastro de Normas Regulamentadoras")
        self.geometry("800x600")

        # Cria os campos do formulário
        self.create_form()

    def create_form(self):
        # Cria um frame para o formulário
        form_frame = ttk.Frame(self, padding="10")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título em negrito no centro acima de todos os campos
        title_label = ttk.Label(form_frame, text="Norma Regulamentadora", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # Frame para Data de Publicação no canto superior direito
        date_frame = ttk.Frame(form_frame)
        date_frame.grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)

        # Campo Data de Publicação
        publication_date_label = ttk.Label(date_frame, text="Data de Publicação:")
        publication_date_label.pack(side=tk.TOP, anchor=tk.E, padx=5, pady=(5, 0))
        
        self.publication_date_entry = DateEntry(date_frame, width=20, background='darkblue',
                                                foreground='white', borderwidth=2)
        self.publication_date_entry.pack(side=tk.TOP, anchor=tk.E, padx=5, pady=(0, 5))

        # Campo Nome da Norma
        norm_name_label = ttk.Label(form_frame, text="Nome da Norma:")
        norm_name_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.norm_name_entry = ttk.Entry(form_frame, width=50)
        self.norm_name_entry.grid(row=3, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Número da Norma
        norm_number_label = ttk.Label(form_frame, text="Número da Norma:")
        norm_number_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.norm_number_entry = ttk.Entry(form_frame, width=50)
        self.norm_number_entry.grid(row=5, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Escopo
        scope_label = ttk.Label(form_frame, text="Escopo:")
        scope_label.grid(row=6, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.scope_entry = ttk.Entry(form_frame, width=50)
        self.scope_entry.grid(row=7, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Descrição da Norma Regulamentadora
        description_label = ttk.Label(form_frame, text="Descrição da Norma Regulamentadora:")
        description_label.grid(row=8, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.description_text = tk.Text(form_frame, width=60, height=4)
        self.description_text.grid(row=9, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Observações da Norma Regulamentadora
        observations_label = ttk.Label(form_frame, text="Observações da Norma Regulamentadora:")
        observations_label.grid(row=10, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.observations_text = tk.Text(form_frame, width=60, height=4)
        self.observations_text.grid(row=11, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Botão Gravar
        save_button = tk.Button(form_frame, text="Gravar", command=self.save_norm,
                                bg="blue", fg="white", borderwidth=2, relief="raised",
                                font=('Helvetica', 10, 'bold'))
        save_button.grid(row=12, column=2, sticky=tk.E, padx=5, pady=20)
        
        # Estilo personalizado para o botão
        save_button.configure(highlightbackground="#ffffff", highlightthickness=2, bd=0, padx=10, pady=5)
        save_button.bind("<Enter>", self.on_enter)
        save_button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(bg="darkblue")

    def on_leave(self, event):
        event.widget.config(bg="blue")

    def save_norm(self):
        # Lógica para salvar a norma pode ser implementada aqui
        publication_date = self.publication_date_entry.get()
        norm_name = self.norm_name_entry.get()
        norm_number = self.norm_number_entry.get()
        scope = self.scope_entry.get()
        description = self.description_text.get("1.0", tk.END).strip()
        observations = self.observations_text.get("1.0", tk.END).strip()
        
        print(f"Salvando Norma:\nData de Publicação: {publication_date}\nNome: {norm_name}\nNúmero: {norm_number}\nEscopo: {scope}\nDescrição: {description}\nObservações: {observations}")

if __name__ == "__main__":
    app = CadastroNormas()
    app.mainloop()
