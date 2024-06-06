
# PROJETO CALCULADORA 🧮
 [![NPM](https://img.shields.io/npm/l/react)](https://github.com/Wiizzi/projeto_calculadora/blob/main/LICENSE) 

# Sobre o projeto

O projeto consiste em uma calculadora básica desenvolvida utilizando a biblioteca Tkinter do Python. A interface gráfica permite realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) [Calculadora](https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v0.2.py).

## Layout SOFTWARE 🏠
A interface da calculadora é composta por um display e uma grade de botões. O display mostra a entrada do usuário e o resultado das operações. Os botões permitem ao usuário inserir números, operações e calcular o resultado.
![Calculadora Janela](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_janela.png)

![Calculadora Tela Cheia](https://github.com/Wiizzi/projeto_calculadora/blob/main/assets/calculadora_tela_cheia.png)

### Display 
- Widget: Label
- Variável de texto: resultado_var (tipo StringVar)
- Fonte: Arial, tamanho 20
- Atributos: anchor="e" (alinhamento à direita)

### Botões 
Os botões são organizados em uma grade 4x5 (4 colunas e 5 linhas) e possuem as seguintes características:

- Fonte: Arial, tamanho 16
- Comandos: Cada botão possui um comando associado que chama a - função on_button_click passando o texto do botão como argumento.

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
    <td>1</td>
    <td>0</td>
    <td>7</td>
    <td>Número</td>
    <td>Inserir número 7</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
    <td>8</td>
    <td>Número</td>
    <td>Inserir número 8</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>9</td>
    <td>Número</td>
    <td>Inserir número 9</td>
  </tr>
  <tr>
    <td>1</td>
    <td>3</td>
    <td>/</td>
    <td>Operador</td>
    <td>Divisão</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0</td>
    <td>4</td>
    <td>Número</td>
    <td>Inserir número 4</td>
  </tr>
  <tr>
    <td>2</td>
    <td>1</td>
    <td>5</td>
    <td>Número</td>
    <td>Inserir número 5</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2</td>
    <td>6</td>
    <td>Número</td>
    <td>Inserir número 6</td>
  </tr>
  <tr>
    <td>2</td>
    <td>3</td>
    <td>*</td>
    <td>Operador</td>
    <td>Multiplicação</td>
  </tr>
  <tr>
    <td>3</td>
    <td>0</td>
    <td>1</td>
    <td>Número</td>
    <td>Inserir número 1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>1</td>
    <td>2</td>
    <td>Número</td>
    <td>Inserir número 2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>3</td>
    <td>Número</td>
    <td>Inserir número 3</td>
  </tr>
  <tr>
    <td>3</td>
    <td>3</td>
    <td>-</td>
    <td>Operador</td>
    <td>Subtração</td>
  </tr>
  <tr>
    <td>4</td>
    <td>0</td>
    <td>0</td>
    <td>Número</td>
    <td>Inserir número 0</td>
  </tr>
  <tr>
    <td>4</td>
    <td>1</td>
    <td>.</td>
    <td>Ponto</td>
    <td>Inserir ponto decimal</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2</td>
    <td>=</td>
    <td>Igual</td>
    <td>Calcular resultado</td>
  </tr>
  <tr>
    <td>4</td>
    <td>3</td>
    <td>+</td>
    <td>Operador</td>
    <td>Adição</td>
  </tr>
</table>

# Tecnologias utilizadas e editor de codigo
- Python
- Tkinter
- VScode
---

## Funcionalidades
### Função 'on_button_click'
- Parâmetros: text (texto do botão clicado)
- Lógica:
    - Se o botão clicado for =, a expressão no display é avaliada utilizando a função eval(). Se a avaliação falhar, o display mostrará "Erro".
    - Para outros botões, o texto do botão é adicionado à expressão atual no display.

## Configuração da grade 🪟
Para assegurar que os botões se expandam proporcionalmente ao redimensionar a janela:

* Linhas: master.grid_rowconfigure(i, weight=1) para i de 0 a 4
* Colunas: master.grid_columnconfigure(i, weight=1) para i de 0 a 3

  ---

# Como executar o projeto! 
![RunGIF](https://github.com/Wiizzi/projeto_calculadora/assets/139828978/fa0f6fca-b219-4b5d-9f83-bd121c429cbe)



- 1 Clone o repositório.
- 2 Execute o script Python.

```bash
# clonar repositório
git clone https://github.com/Wiizzi/projeto_calculadora/blob/main/calculadora_v0.2.py

# executar a calculadora_v0.2.py

import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("400x400")

        self.resultado_var = tk.StringVar()
        self.resultado_label = tk.Label(master, textvariable=self.resultado_var, font=('Arial', 20), anchor="e")
        self.resultado_label.grid(row=0, column=0, columnspan=4, sticky="ew")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Erro")
        else:
            current_text = self.resultado_var.get()
            if current_text == "Erro":
                self.resultado_var.set("")
            self.resultado_var.set(current_text + text)

def main():
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()

```

# Autor

Gabriel Coelho Alves
- [Conecte-se comigo no LinkedIn!](https://www.linkedin.com/in/gabriel-coelho-alves/)


