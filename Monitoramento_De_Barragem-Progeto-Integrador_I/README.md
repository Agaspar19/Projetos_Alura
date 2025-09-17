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

