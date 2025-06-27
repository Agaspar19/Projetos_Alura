# Challenge-telecom-x
Telecom X - Análise de Evasão de Clientes (Churn Analysis)
📋 Descrição do Projeto
Este projeto tem como objetivo analisar o fenômeno de evasão de clientes (churn) da empresa Telecom X. Com um alto índice de cancelamentos, a empresa deseja entender os fatores que influenciam a perda de clientes para desenvolver estratégias que aumentem a retenção.

A análise utiliza dados reais disponibilizados pela empresa e abrange desde a extração e tratamento dos dados até a exploração visual e estatística das principais variáveis relacionadas ao churn.

🛠 Tecnologias Utilizadas
Python 3.x

Bibliotecas: pandas, requests, matplotlib, seaborn

Jupyter Notebook ou Google Colab para desenvolvimento interativo

⚙️ Funcionalidades do Projeto
Extração dos Dados:

Importação dos dados brutos da API ou arquivos locais JSON e Markdown (dicionário de dados).

Tratamento e Limpeza:

Expansão de colunas aninhadas (campos em formato JSON/dicionário).

Conversão de variáveis categóricas para formatos numéricos quando necessário.

Identificação e tratamento de valores ausentes e duplicados.

Análise Exploratória de Dados (EDA):

Inspeção da estrutura e tipos das variáveis.

Visualizações estratégicas para entender o comportamento do churn e variáveis relacionadas.

Cruzamento de variáveis categóricas e numéricas para identificar padrões.

Identificação de Variáveis Relevantes:

Seleção de variáveis que influenciam diretamente o churn, como tipo de contrato, tempo de permanência, serviços contratados e indicadores de satisfação.

📁 Estrutura dos Arquivos
TelecomX_Data.json: Dados principais da base com informações dos clientes.

TelecomX_dicionario.md: Dicionário de dados com descrição das variáveis.

TelecomX_EDA.ipynb: Notebook contendo o código para importação, tratamento e análise exploratória dos dados.

README.md: Documentação do projeto.

🚀 Como executar o projeto
Clone o repositório ou faça download dos arquivos TelecomX_Data.json e TelecomX_dicionario.md.

Abra o notebook TelecomX_EDA.ipynb em um ambiente Jupyter ou Google Colab.

Execute as células sequencialmente para carregar os dados, realizar a limpeza, explorar as variáveis e gerar gráficos.

📊 Resultados Esperados
Compreensão clara das principais características dos clientes que cancelam o serviço.

Insights visuais e estatísticos que possam orientar a criação de modelos preditivos de churn.

Identificação de possíveis ações para melhorar a retenção de clientes.
