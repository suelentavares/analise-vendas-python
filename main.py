# Anáalise Gráfica dinâmica en penas 4 linhas de código em python

import pandas as pd
import plotly.express as px

# 1. Carregar os dados
tabela = pd.read_csv("vendas_distribuicao.csv")

# 2. Limpar espaços em branco dos nomes das colunas
tabela.columns = tabela.columns.str.strip()


grafico = px.sunburst(
    tabela, 
    path=["Continente", "País"], 
    values="vendas (Milhões)", 
    color="Continente",
    title="Divisão de vendas Globais"
)
grafico.update_traces(textinfo="label+percent entry")

grafico.show()