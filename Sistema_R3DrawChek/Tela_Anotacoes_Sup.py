import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class AnotacoesProjeto(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Define o título da janela e seu tamanho
        self.title("Anotações de Projeto")
        self.geometry("800x600")

        # Cria os campos do formulário
        self.create_form()

    def create_form(self):
        # Cria um frame para o formulário
        form_frame = ttk.Frame(self, padding="10")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título em negrito no centro acima de todos os campos
        title_label = ttk.Label(form_frame, text="Anotações de Projeto", font=('Helvetica', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))
        
        # Campo Data de Análise do Projeto
        analysis_date_label = ttk.Label(form_frame, text="Data de Análise do Projeto:")
        analysis_date_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.analysis_date_entry = DateEntry(form_frame, width=20, background='darkblue',
                                             foreground='white', borderwidth=2)
        self.analysis_date_entry.grid(row=2, column=0, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Prazo de Correção
        correction_deadline_label = ttk.Label(form_frame, text="Prazo de Correção:")
        correction_deadline_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.correction_deadline_entry = DateEntry(form_frame, width=20, background='darkblue',
                                                   foreground='white', borderwidth=2)
        self.correction_deadline_entry.grid(row=4, column=0, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Norma ou Regulamento Violado
        violated_norm_label = ttk.Label(form_frame, text="Norma ou Regulamento Violado:")
        violated_norm_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.violated_norm_text = tk.Text(form_frame, width=60, height=4)
        self.violated_norm_text.grid(row=6, column=0, columnspan=2, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Número do Projeto
        project_number_label = ttk.Label(form_frame, text="Número do Projeto:")
        project_number_label.grid(row=5, column=2, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.project_number_entry = ttk.Entry(form_frame, width=20)
        self.project_number_entry.grid(row=6, column=2, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Escopo
        scope_label = ttk.Label(form_frame, text="Escopo:")
        scope_label.grid(row=7, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.scope_entry = ttk.Entry(form_frame, width=50)
        self.scope_entry.grid(row=8, column=0, columnspan=2, sticky=tk.W, padx=5, pady=(0, 5))

        # Campo Observações do Revisor do Projeto
        reviewer_observations_label = ttk.Label(form_frame, text="Observações do Revisor do Projeto:")
        reviewer_observations_label.grid(row=9, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        
        self.reviewer_observations_text = tk.Text(form_frame, width=60, height=4)
        self.reviewer_observations_text.grid(row=10, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(0, 5))

        # Botão Gravar
        save_button = tk.Button(form_frame, text="Gravar", command=self.save_notes,
                                bg="blue", fg="white", borderwidth=2, relief="raised",
                                font=('Helvetica', 10, 'bold'))
        save_button.grid(row=11, column=2, sticky=tk.E, padx=5, pady=20)
        
        # Estilo personalizado para o botão
        save_button.configure(highlightbackground="#ffffff", highlightthickness=2, bd=0, padx=10, pady=5)
        save_button.bind("<Enter>", self.on_enter)
        save_button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(bg="darkblue")

    def on_leave(self, event):
        event.widget.config(bg="blue")

    def save_notes(self):
        # Lógica para salvar as anotações pode ser implementada aqui
        analysis_date = self.analysis_date_entry.get()
        correction_deadline = self.correction_deadline_entry.get()
        violated_norm = self.violated_norm_text.get("1.0", tk.END).strip()
        project_number = self.project_number_entry.get()
        scope = self.scope_entry.get()
        reviewer_observations = self.reviewer_observations_text.get("1.0", tk.END).strip()
        
        print(f"Salvando Anotações:\nData de Análise do Projeto: {analysis_date}\nPrazo de Correção: {correction_deadline}\nNorma ou Regulamento Violado: {violated_norm}\nNúmero do Projeto: {project_number}\nEscopo: {scope}\nObservações do Revisor: {reviewer_observations}")

if __name__ == "__main__":
    app = AnotacoesProjeto()
    app.mainloop()
