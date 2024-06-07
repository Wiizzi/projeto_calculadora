import tkinter as tk
from tkinter import Toplevel
from datetime import datetime

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x450")
        master.config(bg="#1a1a1a")  # Cor de fundo preto

        self.resultado_var = tk.StringVar()
        self.resultado_entry = tk.Entry(master, textvariable=self.resultado_var, font=('Arial', 24), justify="right", bd=0, bg="#1a1a1a", fg="#ffd700", highlightbackground="#1a1a1a", highlightcolor="#1a1a1a", insertbackground="#ffd700")
        self.resultado_entry.grid(row=1, column=0, columnspan=4, sticky="ew", pady=10)

        self.historico_resultados = []

        botoes = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 3),
            ('Limpar', 6, 0), ('=', 6, 1),
            ('←', 6, 2), ('Histórico', 0, 3)  # Botão para abrir o histórico em uma nova janela
        ]

        self.botoes = []

        for (texto, linha, coluna) in botoes:
            botao = tk.Button(master, text=texto, font=('Arial', 16), command=lambda t=texto: self.atualizar_exibicao(t), bd=0, bg="#363636", fg="#ffd700", activebackground="#ffd700", activeforeground="#363636")
            botao.grid(row=linha, column=coluna, sticky="nsew", pady=5, padx=5)
            self.botoes.append(botao)
            if texto not in ['Limpar', '=', '←', 'Histórico']:
                master.bind(texto, lambda event, t=texto: self.atualizar_exibicao(t))  # Associa teclas numéricas e operacionais ao método de atualização
        # Associa a tecla "Enter" à função de cálculo
        master.bind("<Return>", lambda event: self.atualizar_exibicao('='))
        # Bloqueia o número "0" no início da expressão
        master.bind("<Key>", self.bloquear_zero)
        # Associa a tecla Backspace à função de exclusão do último caractere
        master.bind("<BackSpace>", self.apagar_ultimo_caractere)

        for i in range(7):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        self.primeiro_numero_digitado = False
        self.resultado_bloqueado = False  # Variável para controlar se o resultado está bloqueado
        self.atualizar_tamanho_fonte()

    def atualizar_tamanho_fonte(self):
        largura = self.master.winfo_width()
        tamanho_fonte = int(largura / 20)  # Altere esse valor conforme necessário
        self.resultado_entry.config(font=('Arial', tamanho_fonte))
        for botao in self.botoes:
            botao.config(font=('Arial', int(tamanho_fonte * 0.6)))  # Ajuste conforme necessário

    def bloquear_zero(self, event):
        if event.char == '0' and not self.primeiro_numero_digitado:
            if self.resultado_var.get() == '' or self.resultado_var.get() == '0':
                self.resultado_entry.focus_set()
                return 'break'
        self.primeiro_numero_digitado = True

    def atualizar_exibicao(self, texto):
        if texto == 'Limpar':
            self.resultado_var.set('')
            self.primeiro_numero_digitado = False
            self.resultado_bloqueado = False  # Desbloqueia o resultado ao limpar
        elif texto == '=':
            self.calcular()
            self.resultado_bloqueado = False  # Desbloqueia o resultado após o cálculo
        elif texto == '←':  # Se o botão Backspace for clicado, apaga o último caractere
            self.apagar_ultimo_caractere()
        elif texto == 'Histórico':
            self.mostrar_historico()
        elif self.resultado_var.get() == "Erro":
            self.resultado_var.set(texto)
        else:
            if not self.resultado_bloqueado:  # Verifica se o resultado está bloqueado
                # Concatena o texto atual com o texto novo
                self.resultado_var.set(self.resultado_var.get() + texto)

    def apagar_ultimo_caractere(self, event=None):
        self.resultado_var.set(self.resultado_var.get()[:-1])

    def calcular(self):
        expressao = self.resultado_var.get()
        try:
            resultado = eval(expressao)
            if resultado == int(resultado):
                resultado = int(resultado)
            self.resultado_var.set(resultado)
            now = datetime.now()
            hora_calculo = now.strftime("%H:%M:%S")
            self.historico_resultados.append({'expressao': expressao, 'resultado': resultado, 'hora': hora_calculo})  # Adiciona a expressão, o resultado e a hora do cálculo ao histórico
        except Exception as e:
            self.resultado_var.set("Erro")

    def mostrar_historico(self):
        # Cria uma nova janela pop-up para exibir o histórico
        historico_window = Toplevel(self.master)
        historico_window.title("Histórico")
        historico_window.geometry("500x300")

        # Cria um widget de frame para conter o histórico
        historico_frame = tk.Frame(historico_window, bg="#1a1a1a")
        historico_frame.pack(expand=True, fill='both')

        # Adiciona o título "Conta Efetuada" acima do histórico de cálculos
        titulo_conta_label = tk.Label(historico_frame, text="Conta Efetuada", font=('Arial', 12, 'bold'), bg="#1a1a1a", fg="#ffffff")
        titulo_conta_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        # Adiciona o título "Hora do Registro" acima do registro da hora do cálculo
        titulo_hora_label = tk.Label(historico_frame, text="Hora do Registro", font=('Arial', 12, 'bold'), bg="#1a1a1a", fg="#ffffff")
        titulo_hora_label.grid(row=0, column=3, padx=10, pady=5)

        # Adiciona cada item do histórico ao frame com a formatação desejada
        for index, item in enumerate(self.historico_resultados, start=1):
            expressao = item['expressao']
            resultado = item['resultado']
            hora = item['hora']
            # Adiciona expressão centralizada e resultado vermelho à linha
            expressao_label = tk.Label(historico_frame, text=expressao, font=('Arial', 14), bg="#1a1a1a", fg="#ffffff")
            expressao_label.grid(row=index, column=0, padx=5, pady=5)
            resultado_label = tk.Label(historico_frame, text="=" + str(resultado), font=('Arial', 14, 'bold'), bg="#1a1a1a", fg="red")
            resultado_label.grid(row=index, column=1, padx=5, pady=5)
            hora_label = tk.Label(historico_frame, text=hora, font=('Arial', 14), bg="#1a1a1a", fg="yellow")
            hora_label.grid(row=index, column=3, padx=10, pady=5, sticky='e')

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.bind("<Configure>", lambda event: app.atualizar_tamanho_fonte())  # Atualiza o tamanho da fonte quando a janela é redimensionada
    root.mainloop()

if __name__ == "__main__":
    main()