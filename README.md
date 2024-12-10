# Monitoramento_De_Barragem-Progeto-Integrador_I

Este projeto é uma aplicação Python que utiliza `Tkinter` para criar uma interface gráfica que permite o processamento e a análise de dados de vazões. 
O trabalho foi desenvolvido no âmbito da disciplina Projeto Integrador I, contando com a colaboração de:

- André Pedro Gaspar
- Ducher Maliqui  Seidi
- Lucas José Garcia

# Funcionalidades

1. **Carregar Arquivo**: Importa arquivos CSV contendo dados de vazões.
2. **Exibir Tabela**: Mostra os dados em um formato tabular interativo.
3. **Calcular Métricas**:
   - Vazões médias, mínimas e máximas.
   - Médias mensais.
4. **Filtragem**:
   - Por período (intervalo de anos).
   - Por ano específico.
5. **Análise Visual**:
   - Geração de histogramas de médias mensais.
   - Curva de permanência de vazões.
6. **Exportação**:
   - Salvar dados processados em formato CSV.
          
# Requisitos
- Python 3.7 ou superior
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `tkinter`
 
# Importações necessárias para a interface gráfica e manipulação de dados
- import tkinter as tk
- from tkinter import Menu, filedialog, messagebox, ttk
- import pandas as pd
- import numpy as np
- from tkinter import Toplevel, Label, Entry, Button

# Explicação do código

   **Variável global para armazenar o DataFrame carregado**
      - planilha = None
      - df = None
   **Funções**
   
   - def abrir_arquivo():
  
       Abre um arquivo CSV de vazões, realiza o pré-processamento e exibe os dados em uma tabela.
       - Garante o tratamento de colunas específicas (ex.: preenchimento de NaN).
       - Identifica o período dos dados e informa ao usuário.
   
   - def exibir_tabela(df):
    
       Exibe os dados de um DataFrame em formato tabular interativo no Tkinter.
       - Permite rolagem horizontal e vertical.

   - def calcular_medias():
    
       - Calcula as médias gerais das colunas 'Media', 'Maxima' e 'Minima'.
       - Mostra os resultados ao usuário em uma caixa de mensagem.

   **Configuração principal da janela e menu**
        - root = tk.Tk()
        - root.title("Análise de Vazões")
        - root.geometry("800x600")

   **Configuração do menu principal**
       - menu_principal = Menu(root)
       - root.config(menu=menu_principal)

   **Menu Arquivo**
      - menu_arquivo = Menu(menu_principal, tearoff=0)
      - menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
      - menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
      - menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
      - menu_arquivo.add_separator()
      - menu_arquivo.add_command(label="Sair", command=root.quit)

   **Configuração de outros menus e widgets**
       - root.mainloop()

