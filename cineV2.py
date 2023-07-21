import tkinter as tk
from tkinter import messagebox

class ReservaPoltronas:
    def __init__(self, root):
        self.root = root
        self.root.title("Reserva de Poltronas")
        self.filmes = ["Filme 1", "Filme 2"]
        self.num_poltronas = 40
        self.poltronas_ocupadas = {filme: set() for filme in self.filmes}

        self.criar_interface()

    def criar_interface(self):
        self.frame_poltronas = tk.Frame(self.root, padx=20, pady=20)
        self.frame_poltronas.pack()

        self.label_titulo = tk.Label(self.frame_poltronas, text="Selecione o filme:")
        self.label_titulo.grid(row=0, columnspan=2)

        self.filme_var = tk.StringVar(self.frame_poltronas)
        self.filme_var.set(self.filmes[0])
        self.menu_filmes = tk.OptionMenu(self.frame_poltronas, self.filme_var, *self.filmes, command=self.atualizar_poltronas)
        self.menu_filmes.grid(row=1, columnspan=2)

        self.botao_poltronas = []
        self.atualizar_poltronas()
        
    def atualizar_poltronas(self, *args):
        filme_selecionado = self.filme_var.get()
        for botao in self.botao_poltronas:
            botao.grid_forget()

        for i in range(self.num_poltronas):
            row, col = divmod(i, 10)
            cor = "red" if i in self.poltronas_ocupadas[filme_selecionado] else "green"
            botao = tk.Button(self.frame_poltronas, text=str(i+1), width=3, height=1, bg=cor, command=lambda idx=i: self.reservar_poltrona(idx))
            botao.grid(row=row+2, column=col)
            self.botao_poltronas.append(botao)

    def reservar_poltrona(self, idx):
        filme_selecionado = self.filme_var.get()
        if idx in self.poltronas_ocupadas[filme_selecionado]:
            messagebox.showerror("Erro", "Poltrona já está ocupada.")
        else:
            self.poltronas_ocupadas[filme_selecionado].add(idx)
            self.atualizar_poltronas()
            messagebox.showinfo("Sucesso", "Poltrona reservada com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    reserva = ReservaPoltronas(root)
    root.mainloop()
