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


