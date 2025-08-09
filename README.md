modelos preditivos 
📌 Visão Geral
Este projeto tem como objetivo prever quais clientes possuem maior probabilidade de cancelar os serviços da empresa (Telecom X).
A previsão antecipada da evasão permite ações estratégicas de retenção, aumentando a receita e reduzindo perdas.

🎯 Objetivos do Desafio

Preparar os dados para a modelagem (tratamento, encoding, normalização).

Realizar análise de correlação e seleção de variáveis.

Treinar dois modelos de classificação.

Avaliar o desempenho dos modelos com métricas.

Interpretar os resultados, incluindo a importância das variáveis.

Criar uma conclusão estratégica apontando os principais fatores que influenciam a evasão.

🛠️ Tecnologias Utilizadas

Jupyter Notebook para exploração e análise

Random Forest & Logistic Regression para modelagem
📈 Resultados
Foram treinados dois modelos principais:

Modelo	Accuracy	Precision	Recall	F1	ROC AUC
Logistic Regression	0.746	0.612	0.319	0.420	0.747
Random Forest	0.734	0.539	0.398	0.458	0.744

Top 5 variáveis mais importantes (Random Forest):

Tipo de serviço telefônico e múltiplas linhas

Tipo de internet e segurança online

Streaming de TV e filmes

Forma de pagamento

Tempo de contrato

📌 Conclusões Estratégicas

Clientes com planos mensais e pagamento eletrônico apresentaram maior chance de evasão.

O uso de múltiplos serviços (TV, internet, telefone) tende a reduzir a evasão.

Recomenda-se programas de fidelidade e descontos para planos anuais.
