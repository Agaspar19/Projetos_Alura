import tkinter as tk
from tkinter import Menu, filedialog, messagebox, ttk
import pandas as pd
import numpy as np
from tkinter import Toplevel, Label, Entry, Button
# Variável global para armazenar o DataFrame
planilha = None
df=None
# Função para carregar o arquivo e exibir os dados na tabela
def abrir_arquivo():
    global planilha
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos CSV", "*.csv")], title="Selecione o arquivo de vazões"
        )
        if not file_path:
            return  # Usuário cancelou
        planilha = pd.read_csv(file_path, skiprows=15, encoding="latin-1", sep=";")
        print("Linhas/colunas:", planilha.shape)
        # Tratamento das variáveis
        colunas = [
            "Maxima",
            "Minima",
            "Media",
            "DiaMaxima",
            "DiaMinima",
            "MaximaStatus",
            "MinimaStatus",
            "MediaStatus",
            "MediaAnual",
            "MediaAnualStatus",
        ]
        if "Hora" in planilha.columns:
            planilha["Hora"] = pd.to_datetime(planilha["Hora"], errors="coerce").dt.time
        for coluna in colunas:
            if coluna in planilha.columns:
                planilha[coluna] = planilha[coluna].fillna(0).replace({",": "."}, regex=True).astype(np.float64)
        for i in range(1, 32):
            coluna_vazao = f"Vazao{i:02d}"
            coluna_vazao_status = f"Vazao{i:02d}Status"
            for coluna in [coluna_vazao, coluna_vazao_status]:
                if coluna in planilha.columns:
                    planilha[coluna] = planilha[coluna].fillna(0).replace({",": "."}, regex=True).astype(np.float64)
        inicio = pd.to_datetime(planilha["Data"]).min().strftime("%m/%d/%Y")
        fim = pd.to_datetime(planilha["Data"]).max().strftime("%m/%d/%Y")
        messagebox.showinfo("Período dos Dados", f"Dados de {inicio} até {fim}")
        exibir_tabela(planilha)
    except Exception as e:
        messagebox.showerror("Erro ao abrir o arquivo", str(e))
def exibir_tabela(df):
    # Limpar o conteúdo anterior
    for widget in frame_resultados.winfo_children():
        widget.destroy()
    # Formatar os dados para ter 3 casas decimais
    df_formatado = df.copy()
    for col in df_formatado.select_dtypes(include=[np.number]).columns:
        df_formatado[col] = df_formatado[col].round(3)
    # Criar um Frame para a tabela e as barras de rolagem
    tabela_frame = tk.Frame(frame_resultados)
    tabela_frame.pack(fill="both", expand=True)
    # Criar o Treeview
    tree = ttk.Treeview(
        tabela_frame,
        columns=list(df_formatado.columns),
        show="headings",
        selectmode="browse"
    )
    # Configurar cabeçalhos
    for col in df_formatado.columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")  # Ajustar largura padrão
    # Inserir os dados formatados
    for _, row in df_formatado.iterrows():
        tree.insert("", "end", values=list(row))
    # Adicionar barras de rolagem
    scrollbar_y = ttk.Scrollbar(tabela_frame, orient="vertical", command=tree.yview)
    scrollbar_x = ttk.Scrollbar(tabela_frame, orient="horizontal", command=tree.xview)
    # Vincular barras de rolagem ao Treeview
    tree.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)
    # Posicionar barras de rolagem
    scrollbar_y.pack(side="right", fill="y")
    scrollbar_x.pack(side="bottom", fill="x")
    # Posicionar Treeview
    tree.pack(fill="both", expand=True)
def calcular_medias():
    try:
        global df
        if df is None:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
            return
        # Garantir que as colunas 'Media', 'Maxima' e 'Minima' existem
        if 'Media' not in df.columns or 'Maxima' not in df.columns or 'Minima' not in df.columns:
            messagebox.showwarning("Aviso", "Colunas 'Media', 'Maxima' e/ou 'Minima' não encontradas!")
            return
        # Calcular as médias
        media_media = df['Media'].mean()
        media_maxima = df['Maxima'].mean()
        media_minima = df['Minima'].mean()
        # Exibir os resultados em uma mensagem
        messagebox.showinfo("Médias Calculadas", f"""
        Média das Médias: {media_media:.3f}
        Média das Máximas: {media_maxima:.3f}
        Média das Mínimas: {media_minima:.3f}
        """)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular as médias: {e}")
def vazoes_minimas():
    try:
        global df
        if df is None:
            global planilha
            if planilha is None:
                messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
                return
            # Calculando o valor mínimo em cada linha nas colunas de Vazões (Vazao01 a Vazao31)
            planilha['Minima'] = planilha.loc[:, "Vazao01":"Vazao31"].min(axis=1)
            # Selecionar colunas relevantes
            colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Minima']
            dados_minimos = planilha[colunas_relevantes].copy()
            # Converter a coluna 'Data' para exibir apenas a data (remover a hora)
            dados_minimos['Data'] = pd.to_datetime(dados_minimos['Data']).dt.strftime('%m/%d/%Y')
            # Exibir na tabela
            exibir_tabela(dados_minimos)
            # Exibe uma mensagem de conclusão
            messagebox.showinfo("Sucesso", "Coluna 'Minima' preenchida com os valores mínimos das vazões!")
            return
        # Calculando o valor mínimo em cada linha nas colunas de Vazões (Vazao01 a Vazao31)
        df['Minima'] = df.loc[:, "Vazao01":"Vazao31"].min(axis=1)
        # Selecionar colunas relevantes
        colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Minima']
        dados_minimos = df[colunas_relevantes].copy()
        # Converter a coluna 'Data' para exibir apenas a data (remover a hora)
        dados_minimos['Data'] = pd.to_datetime(dados_minimos['Data']).dt.strftime('%m/%d/%Y')
        # Exibir na tabela
        exibir_tabela(dados_minimos)
        # Exibe uma mensagem de conclusão
        messagebox.showinfo("Sucesso", "Coluna 'Minima' preenchida!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular vazões mínimas: {e}")
def vazoes_maximas():
    try:
        global df
        if df is None:
            global planilha
            if planilha is None:
                messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
                return
            # Calculando o valor mínimo em cada linha nas colunas de Vazões (Vazao01 a Vazao31)
            planilha['Maxima'] = planilha.loc[:, "Vazao01":"Vazao31"].min(axis=1)
            # Selecionar colunas relevantes
            colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Maxima']
            dados_maximos = planilha[colunas_relevantes].copy()
            # Converter a coluna 'Data' para exibir apenas a data (remover a hora)
            dados_maximos['Data'] = pd.to_datetime(dados_maximos['Data']).dt.strftime('%m/%d/%Y')
            # Exibir na tabela
            exibir_tabela(dados_maximos)
            # Exibe uma mensagem de conclusão
            messagebox.showinfo("Sucesso", "Coluna 'Maxima' preenchida !!")
            return
        # Calculando o valor máximo em cada linha nas colunas de Vazões (Vazao01 a Vazao31)
        df['Maxima'] = df.loc[:, "Vazao01":"Vazao31"].max(axis=1)
        # Atualiza a exibição na tabela
        colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Maxima']
        dados_maximos = df[colunas_relevantes].copy()
        dados_maximos['Data'] = pd.to_datetime(dados_maximos['Data']).dt.strftime('%m/%d/%Y')
        # Exibir na tabela
        exibir_tabela(dados_maximos)
        # Exibe uma mensagem de conclusão
        messagebox.showinfo("Sucesso", "Coluna 'Maxima' preenchida!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular vazões máximas: {e}")
def vazoes_medias():
    try:
        global df
        if df is None:
            global planilha
            if planilha is None:
                messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
                return
            # Calculando o valor mínimo em cada linha nas colunas de Vazões (Vazao01 a Vazao31)
            planilha['Media'] = planilha.loc[:, "Vazao01":"Vazao31"].min(axis=1)
            # Selecionar colunas relevantes
            colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Media']
            dados_medios = planilha[colunas_relevantes].copy()
            # Converter a coluna 'Data' para exibir apenas a data (remover a hora)
            dados_medios['Data'] = pd.to_datetime(dados_medios['Data']).dt.strftime('%m/%d/%Y')
            # Exibir na tabela
            exibir_tabela(dados_medios)
            # Exibe uma mensagem de conclusão
            messagebox.showinfo("Sucesso", "Coluna 'Media' preenchida !")
            return
        # Calculando a média das vazões (colunas 17 a 46) e atribuindo à coluna 'Media'
        df['Media'] = df.iloc[:, 16:46].mean(axis=1)
        df['MediaStatus'] = df.iloc[:, 46:76].mean(axis=1)

        # Atualiza a exibição na tabela
        # Selecionar colunas relevantes
        colunas_relevantes = ['EstacaoCodigo', 'NivelConsistencia', 'Data', 'Media']
        dados_medios = df[colunas_relevantes].copy()
        dados_medios['Data'] = pd.to_datetime(dados_medios['Data']).dt.strftime('%m/%d/%Y')
        # Exibir na tabela
        exibir_tabela(dados_medios)

        # Exibe uma mensagem de conclusão
        messagebox.showinfo("Sucesso", "Médias das vazões calculadas com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular vazões médias: {e}")
def salvar_arquivo():
    try:
        global planilha
        if planilha is None:
            messagebox.showwarning("Aviso", "Nenhum arquivo foi carregado!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")], title="Salvar arquivo"
        )
        if not file_path:
            return  # Usuário cancelou

        planilha.to_csv(file_path, index=False, sep=";", encoding="latin-1")
        messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro ao salvar arquivo", str(e))
def curva_permanencia():
    global df
    try:
        #global planilha
        if df is None:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
            return
        colunas_vazao = [f"Vazao{i:02d}" for i in range(1, 32)]
        if not set(colunas_vazao).issubset(df.columns):
            messagebox.showerror("Erro", "Colunas de vazões não encontradas!")
            return
        vazoes = df.loc[:, colunas_vazao].values.flatten()
        vazoes = vazoes[vazoes > 0]  # Remover zeros ou valores ausentes
        vazoes.sort()
        # Frequência acumulada
        probabilidade = np.linspace(1, 0, len(vazoes))
        # Plotar gráfico
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))
        plt.plot(vazoes, probabilidade * 100)
        plt.xlabel("Vazão")
        plt.ylabel("Probabilidade (%)")
        plt.title("Curva de Permanência")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar curva de permanência: {e}")
def histograma():
    global df
    try:
        if df is None:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
            return
        # Garantir que a coluna 'Data' esteja no formato datetime
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
        # Extrair o mês e calcular a média mensal
        df['Mes'] = df['Data'].dt.month
        medias_mensais = df.groupby('Mes')['Media'].mean()
        # Plotar o histograma
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))
        medias_mensais.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Média Mensal das Vazões')
        plt.xlabel('Mês')
        plt.ylabel('Vazão Média (m³/s)')
        plt.xticks(ticks=range(12), labels=[
            "Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
            "Jul", "Ago", "Set", "Out", "Nov", "Dez"
        ], rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar histograma: {e}")

def calcular_vazao():
    print("Calcular Vazão selecionado.")
def calcular_volume():
    print("Calcular Volume selecionado.")
def calcular_area():
    print("Calcular Área selecionado.")
def filtrar_periodo():
    global df
    try:
        global planilha
        if planilha is None:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
            return
        # Garantir que a coluna 'Data' esteja no formato datetime
        planilha['Data'] = pd.to_datetime(planilha['Data'], errors='coerce')
        # Extraindo o ano da coluna 'Data'
        planilha['Ano'] = planilha['Data'].dt.year
        # Abrir uma janela para inserir o período
        def aplicar_periodo():
            global df
            try:
                # Obter os anos inseridos
                ano_inicial = int(entry_ano_inicial.get())
                ano_final = int(entry_ano_final.get())
                # Filtrar os dados com base no intervalo de anos
                dados_periodo = planilha[(planilha['Ano'] >= ano_inicial) & (planilha['Ano'] <= ano_final)]
                df = dados_periodo
                if not df.empty:
                    # Adicionar uma coluna formatada com apenas a data
                    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
                    # Atualizar a tabela com os dados do período
                    exibir_tabela(df)
                else:
                    messagebox.showinfo("Sem dados", f"Não há dados disponíveis para o período de {ano_inicial} a {ano_final}.")

                janela_periodo.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores válidos para o ano.")

        # Criar a janela para o período
        janela_periodo = Toplevel(root)
        janela_periodo.title("Filtrar por Período")
        janela_periodo.geometry("400x200")

        Label(janela_periodo, text="Ano Inicial:").grid(row=0, column=0, padx=10, pady=10)
        entry_ano_inicial = Entry(janela_periodo, width=10)
        entry_ano_inicial.grid(row=0, column=1, padx=10, pady=10)

        Label(janela_periodo, text="Ano Final:").grid(row=1, column=0, padx=10, pady=10)
        entry_ano_final = Entry(janela_periodo, width=10)
        entry_ano_final.grid(row=1, column=1, padx=10, pady=10)

        Button(janela_periodo, text="Aplicar", command=aplicar_periodo).grid(row=2, column=0, columnspan=2, pady=20)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao filtrar por período: {e}")
def filtrar_ano():
    global df
    try:
        global planilha
        if planilha is None:
            messagebox.showwarning("Aviso", "Carregue um arquivo primeiro!")
            return
        # Garantir que a coluna 'Data' esteja no formato datetime
        planilha['Data'] = pd.to_datetime(planilha['Data'], errors='coerce')
        # Extraindo o ano da coluna 'Data'
        planilha['Ano'] = planilha['Data'].dt.year
        # Abrir uma janela para inserir o ano desejado
        def aplicar_ano():
            global df
            try:
                ano_desejado = int(entry_ano.get())
                # Filtrar os dados pelo ano desejado
                dados_ano = planilha[planilha['Ano'] == ano_desejado]
                df = dados_ano
                if not df.empty:
                    # Adicionar uma coluna para exibir apenas a data formatada
                    df['Data'] = df['Data'].dt.strftime('%d/%m/%Y')
                    # Atualizar a tabela com os dados do ano
                    exibir_tabela(df)

                else:
                    messagebox.showinfo("Sem dados", f"Não há dados disponíveis para o ano {ano_desejado}.")

                janela_ano.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um ano válido.")

        # Criar a janela para o ano
        janela_ano = Toplevel(root)
        janela_ano.title("Filtrar por Ano")
        janela_ano.geometry("300x150")

        Label(janela_ano, text="Ano:").grid(row=0, column=0, padx=10, pady=10)
        entry_ano = Entry(janela_ano, width=10)
        entry_ano.grid(row=0, column=1, padx=10, pady=10)

        Button(janela_ano, text="Aplicar", command=aplicar_ano).grid(row=1, column=0, columnspan=2, pady=10)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao filtrar por ano: {e}")
def reset():
    global df
    global planilha
    try:
        df = planilha
        # Converter a coluna 'Data' para exibir apenas a data (remover a hora)
        planilha['Data'] = pd.to_datetime(planilha['Data']).dt.strftime('%m/%d/%Y')
        exibir_tabela(planilha)
    except ValueError:
        pass

root = tk.Tk()
root.title("SCAH")
root.geometry("800x600")

menu_bar = Menu(root)

menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_vazoes = Menu(menu_bar, tearoff=0)
menu_vazoes.add_command(label="Vazões Mínimas", command=vazoes_minimas)
menu_vazoes.add_command(label="Vazões Máximas", command=vazoes_maximas)
menu_vazoes.add_command(label="Vazões Médias", command=vazoes_medias)
menu_vazoes.add_command(label="Curva de Permanência", command=curva_permanencia)
menu_vazoes.add_command(label="Histograma", command=histograma)
menu_bar.add_cascade(label="Vazões", menu=menu_vazoes)

menu_ferramentas = Menu(menu_bar, tearoff=0)
menu_ferramentas.add_command(label="Calcular Volume", command=calcular_volume)
menu_ferramentas.add_command(label="Calcular Área", command=calcular_area)
menu_bar.add_cascade(label="Ferramentas", menu=menu_ferramentas)
menu_ferramentas.add_cascade(label="Calcular Médias",command=calcular_medias)

menu_filtrar = Menu(menu_bar, tearoff=0)
menu_filtrar.add_command(label="Período", command=filtrar_periodo)
menu_filtrar.add_command(label="1 Ano", command=filtrar_ano)
menu_bar.add_cascade(label="Filtrar", menu=menu_filtrar)

btn_reset = tk.Button(root, text="Resetar Variáveis", command=reset, bg="red", fg="white")
btn_reset.pack(pady=10)

root.config(menu=menu_bar)

frame_resultados = tk.Frame(root, bd=1, relief="solid")
frame_resultados.pack(fill="both", expand=True, padx=20, pady=10)

root.mainloop()