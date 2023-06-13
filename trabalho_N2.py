import pandas as pd
import plotly.express as px
import numpy as np

# Inserindo o conjunto de dados
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                      header=None,
                      names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Calculando a média, mediana, moda, desvio padrão, variação e coeficiente de variação
media = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()
mediana = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].median()
moda = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mode()
desvio_padrao = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].std()
variacao = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].var()
coeficiente_variacao = iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].std() / iris_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].mean()

# Exibindo informações estatísticas do arquivo inserido acima
print(f"\nMédias:\n{media}")
print(f"\nMedianas:\n{mediana}")
print(f"\nModas:\n{moda}")
print(f"\nDesvios padrão:\n{desvio_padrao}")
print(f"\nVariâncias:\n{variacao}")
print(f"\nCoeficientes de variação:\n{coeficiente_variacao}")

# Criando gráficos interativos usando a biblioteca Plotly
grafico_media = px.bar(media, title='Médias', labels={'value': 'Valor', 'index': 'Atributo'})
grafico_mediana = px.bar(mediana, title='Medianas', labels={'value': 'Valor', 'index': 'Atributo'})
grafico_moda = px.bar(moda, title='Modas', labels={'value': 'Valor', 'index': 'Atributo'})
grafico_desvio_padrao = px.bar(desvio_padrao, title='Desvios Padrão', labels={'value': 'Valor', 'index': 'Atributo'})
grafico_variacao = px.bar(variacao, title='Variações', labels={'value': 'Valor', 'index': 'Atributo'})
grafico_coeficiente_variacao = px.scatter(x=media, y=desvio_padrao, title='Coeficiente de Variação', labels={'x': 'Média', 'y': 'Desvio Padrão'})

# Exibindo os gráficos do Dashboard interativo
grafico_media.show()
grafico_mediana.show()
grafico_moda.show()
grafico_desvio_padrao.show()
grafico_variacao.show()
grafico_coeficiente_variacao.show()
