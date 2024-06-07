# PROJETO CALCULADORA 🧮
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Wiizzi/projeto_calculadora/blob/main/LICENSE) 

![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 
# Sobre o projeto

O projeto consiste em uma calculadora básica desenvolvida utilizando a biblioteca Tkinter do Python. A interface gráfica permite realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) [Calculadora](https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v1.8.pyw).

## Layout SOFTWARE 🏠
A interface da calculadora é composta por um display e uma grade de botões. O display mostra a entrada do usuário e o resultado das operações. Os botões permitem ao usuário inserir números, operações e calcular o resultado.

 ![Calculadora Janela](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_janela.png)

 ![Calculadora Tela Cheia](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_tela_cheia.png)
 
---
# Nova versão: Aba histórico de cálculo
![Historico_janela](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/janela_historico.png)

### Display 
- Widget: Entry
- Variável de texto: resultado_var (tipo StringVar)
- Fonte: Arial, tamanho ajustável
- Cor de fundo: #1a1a1a
- Cor do texto: #ffd700
- Atributos: justify="right", bd=0, highlightbackground="#1a1a1a", highlightcolor="#1a1a1a", insertbackground="#ffd700"

### Botões 
Os botões são organizados em uma grade 4x5 (4 colunas e 5 linhas) e possuem as seguintes características:

- Fonte: Arial, tamanho ajustável
- Cor de fundo: #363636
- Cor do texto: #ffd700
- Cor de fundo ativa: #ffd700
- Cor do texto ativo: #363636
- Comandos: Cada botão possui um comando associado que chama a função atualizar_exibicao passando o texto do botão como argumento.

## Distribuição dos botões:

<h2>Tabela de Botões da Calculadora</h2>

<p>A tabela abaixo descreve a disposição dos botões na interface.</p>

<table>
  <tr>
    <th>Linha</th>
    <th>Coluna</th>
    <th>Texto</th>
    <th>Tipo</th>
    <th>Função</th>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>7</td>
    <td>Número</td>
    <td>Inserir número 7</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1</td>
    <td>8</td>
    <td>Número</td>
    <td>Inserir número 8</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2</td>
    <td>9</td>
    <td>Número</td>
    <td>Inserir número 9</td>
  </tr>
  <tr>
    <td>2</td>
    <td>3</td>
    <td>/</td>
    <td>Operador</td>
    <td>Divisão</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0</td>
    <td>4</td>
    <td>Número</td>
    <td>Inserir número 4</td>
  </tr>
  <tr>
    <td>3</td>
    <td>1</td>
    <td>5</td>
    <td>Número</td>
    <td>Inserir número 5</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>6</td>
    <td>Número</td>
    <td>Inserir número 6</td>
  </tr>
  <tr>
    <td>3</td>
    <td>3</td>
    <td>*</td>
    <td>Operador</td>
    <td>Multiplicação</td>
  </tr>
  <tr>
    <td>4</td>
    <td>0</td>
    <td>1</td>
    <td>Número</td>
    <td>Inserir número 1</td>
  </tr>
  <tr>
    <td>4</td>
    <td>1</td>
    <td>2</td>
    <td>Número</td>
    <td>Inserir número 2</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2</td>
    <td>3</td>
    <td>Número</td>
    <td>Inserir número 3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>-</td>
    <td>Operador</td>
    <td>Subtração</td>
  </tr>
  <tr>
    <td>5</td>
    <td>0</td>
    <td>0</td>
    <td>Número</td>
    <td>Inserir número 0</td>
  </tr>
  <tr>
    <td>5</td>
    <td>1</td>
    <td>.</td>
    <td>Ponto</td>
    <td>Inserir ponto decimal</td>
  </tr>
  <tr>
    <td>5</td>
    <td>3</td>
    <td>+</td>
    <td>Operador</td>
    <td>Adição</td>
  </tr>
  <tr>
    <td>6</td>
    <td>0</td>
    <td>Limpar</td>
    <td>Função</td>
    <td>Limpar display</td>
  </tr>
  <tr>
    <td>6</td>
    <td>1</td>
    <td>=</td>
    <td>Função</td>
    <td>Calcular resultado</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2</td>
    <td>←</td>
    <td>Função</td>
    <td>Apagar último caractere</td>
  </tr>
  <tr>
    <td>0</td>
    <td>3</td>
    <td>Histórico</td>
    <td>Função</td>
    <td>Abrir histórico de cálculos</td>
  </tr>
</table>

# Tecnologias utilizadas e editor de código
- Python
- Tkinter
- VScode
---

## Funcionalidades
### Função 'atualizar_exibicao'
- Parâmetros: texto (texto do botão clicado)
- Lógica:
    - Se o botão clicado for '=', a expressão no display é avaliada utilizando a função eval(). Se a avaliação falhar, o display mostrará "Erro".
    - Se o botão clicado for '←', o último caractere da expressão é removido.
    - Se o botão clicado for 'Limpar', o display é limpo.
    - Se o botão clicado for 'Histórico', uma nova janela com o histórico de cálculos é aberta.
    - Para outros botões, o texto do botão é adicionado à expressão atual no display.

### Função 'calcular'
- Lógica:
    - Avalia a expressão matemática no display.
    - Adiciona a expressão, o resultado e a hora do cálculo ao histórico.
    - Se a avaliação falhar, o display mostrará "Erro".

### Função 'mostrar_historico'
- Lógica:
    - Abre uma nova janela mostrando o histórico de cálculos.
    - Cada item no histórico é mostrado com a expressão, o resultado e a hora do cálculo.

## Configuração da grade 🪟
Para assegurar que os botões se expandam proporcionalmente ao redimensionar a janela:

* Linhas: master.grid_rowconfigure(i, weight=1) para i de 0 a 6
* Colunas: master.grid_columnconfigure(i, weight=1) para i de 0 a 3

  ---

# Como executar o projeto! 
![RunGIF](https://github.com/Wiizzi/projeto_calculadora/assets/139828978/fa0f6fca-b219-4b5d-9f83-bd121c429cbe)



- 1 Clone o repositório.
- 2 Execute o script Python.

```bash
# clonar repositório
git clone https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v1.8.pyw

# executar a calculadora_v1.8.pyw

import tkinter as tk
from tkinter import Toplevel
from datetime import datetime

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x450")
        master.config(bg="#1a

1a1a")  # Cor de fundo preto

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
```

# Autor
Gabriel Coelho Alves
- [Conecte-se comigo no LinkedIn!](https://www.linkedin.com/in/gabriel-coelho-alves/)
---
![KakashiNarutoGIF](https://github.com/Wiizzi/projeto_calculadora/assets/139828978/f8e0d504-bca3-48b3-9e94-c524ddf7979a)

![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 
# English

# CALCULATOR PROJECT 🧮
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Wiizzi/projeto_calculadora/blob/main/LICENSE) 

![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 
# About the project

The project consists of a basic calculator developed using the Tkinter library in Python. The graphical interface allows performing basic mathematical operations (addition, subtraction, multiplication, and division) [Calculator](https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v1.8.pyw).

## SOFTWARE Layout 🏠
The calculator interface consists of a display and a grid of buttons. The display shows user input and the results of operations. The buttons allow the user to input numbers, operations, and calculate results.

 ![Calculator Window](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_janela.png)

 ![Calculator Full Screen](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_tela_cheia.png)
 
---
# New version: Calculation history tab
![History_window](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/janela_historico.png)

### Display 
- Widget: Entry
- Text variable: resultado_var (type StringVar)
- Font: Arial, adjustable size
- Background color: #1a1a1a
- Text color: #ffd700
- Attributes: justify="right", bd=0, highlightbackground="#1a1a1a", highlightcolor="#1a1a1a", insertbackground="#ffd700"

### Buttons 
The buttons are organized in a 4x5 grid (4 columns and 5 rows) and have the following characteristics:

- Font: Arial, adjustable size
- Background color: #363636
- Text color: #ffd700
- Active background color: #ffd700
- Active text color: #363636
- Commands: Each button has an associated command that calls the `update_display` function passing the button's text as an argument.

## Buttons distribution:

<h2>Calculator Buttons Table</h2>

<p>The table below describes the button layout in the interface.</p>

<table>
  <tr>
    <th>Row</th>
    <th>Column</th>
    <th>Text</th>
    <th>Type</th>
    <th>Function</th>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>7</td>
    <td>Number</td>
    <td>Insert number 7</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1</td>
    <td>8</td>
    <td>Number</td>
    <td>Insert number 8</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2</td>
    <td>9</td>
    <td>Number</td>
    <td>Insert number 9</td>
  </tr>
  <tr>
    <td>2</td>
    <td>3</td>
    <td>/</td>
    <td>Operator</td>
    <td>Division</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0</td>
    <td>4</td>
    <td>Number</td>
    <td>Insert number 4</td>
  </tr>
  <tr>
    <td>3</td>
    <td>1</td>
    <td>5</td>
    <td>Number</td>
    <td>Insert number 5</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>6</td>
    <td>Number</td>
    <td>Insert number 6</td>
  </tr>
  <tr>
    <td>3</td>
    <td>3</td>
    <td>*</td>
    <td>Operator</td>
    <td>Multiplication</td>
  </tr>
  <tr>
    <td>4</td>
    <td>0</td>
    <td>1</td>
    <td>Number</td>
    <td>Insert number 1</td>
  </tr>
  <tr>
    <td>4</td>
    <td>1</td>
    <td>2</td>
    <td>Number</td>
    <td>Insert number 2</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2</td>
    <td>3</td>
    <td>Number</td>
    <td>Insert number 3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>-</td>
    <td>Operator</td>
    <td>Subtraction</td>
  </tr>
  <tr>
    <td>5</td>
    <td>0</td>
    <td>0</td>
    <td>Number</td>
    <td>Insert number 0</td>
  </tr>
  <tr>
    <td>5</td>
    <td>1</td>
    <td>.</td>
    <td>Point</td>
    <td>Insert decimal point</td>
  </tr>
  <tr>
    <td>5</td>
    <td>3</td>
    <td>+</td>
    <td>Operator</td>
    <td>Addition</td>
  </tr>
  <tr>
    <td>6</td>
    <td>0</td>
    <td>Clear</td>
    <td>Function</td>
    <td>Clear display</td>
  </tr>
  <tr>
    <td>6</td>
    <td>1</td>
    <td>=</td>
    <td>Function</td>
    <td>Calculate result</td>
  </tr>
  <tr>
    <td>6</td>
    <td>2</td>
    <td>←</td>
    <td>Function</td>
    <td>Delete last character</td>
  </tr>
  <tr>
    <td>0</td>
    <td>3</td>
    <td>History</td>
    <td>Function</td>
    <td>Open calculation history</td>
  </tr>
</table>

# Technologies used and code editor
- Python
- Tkinter
- VScode
---

## Features
### 'update_display' Function
- Parameters: text (clicked button text)
- Logic:
    - If the clicked button is '=', evaluate the expression in the display using the `eval()` function. If evaluation fails, the display will show "Error".
    - If the clicked button is '←', remove the last character from the expression.
    - If the clicked button is 'Clear', clear the display.
    - If the clicked button is 'History', open a new window with the calculation history.
    - For other buttons, append the button text to the current expression in the display.

### 'calculate' Function
- Logic:
    - Evaluate the mathematical expression in the display.
    - Add the expression, result, and calculation time to the history.
    - If evaluation fails, the display will show "Error".

### 'show_history' Function
- Logic:
    - Opens a new window displaying the calculation history.
    - Each item in the history is shown with the expression, result, and calculation time.

## Grid configuration 🪟
To ensure that buttons expand proportionally when resizing the window:

* Rows: `master.grid_rowconfigure(i, weight=1)` for i from 0 to 6
* Columns: `master.grid_columnconfigure(i, weight=1)` for i from 0 to 3

  ---

# How to run the project! 
![RunGIF](https://github.com/Wiizzi/projeto_calculadora/assets/139828978/fa0f6fca-b219-4b5d-9f83-bd121c429cbe)

- 1 Clone the repository.
- 2 Run the Python script.

```bash
# clone repository
git clone https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v1.8.pyw

# run calculadora_v1.8.pyw
```
![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188) 

# Author
Gabriel Coelho Alves

- Connect with me on LinkedIn!
![line](https://github.com/bylickilabs/bylickilabs/assets/109308073/bfd77a60-d426-4470-b417-fdbab0166188)
![KakashiNarutoGIF](https://github.com/Wiizzi/projeto_calculadora/assets/139828978/f8e0d504-bca3-48b3-9e94-c524ddf7979a)


