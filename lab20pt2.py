'''
Continuando o exercício anterior, seu código deve conter as ações abaixo. Todos os campos devem ser criados no mesmo
DataFrame df:

Crie o campo Nota_MinMax com a transformação do campo Nota para numérico em uma escala de 0 a 1, utilizando o
MinMaxScaler.
Crie o campo N_Avaliações_MinMax com a transformação do campo N_Avaliações para numérico em uma escala de 0 a 1,
utilizando o MinMaxScaler.
Crie o campo Desconto_MinMax com a transformação do campo Desconto para numérico em uma escala de 0 a 1, utilizando o
MinMaxScaler.
Crie o campo Preço_MinMax com a transformação do campo Preço para numérico em uma escala de 0 a 1, utilizando o
MinMaxScaler.
Crie o campo Marca_Cod utilizando o método LabelEncoder para transformar o campo Marca em numérico.
Crie o campo Material_Cod utilizando o método LabelEncoder para transformar o campo Material em numérico.
Crie o campo Temporada_Cod utilizando o método LabelEncoder para transformar o campo Temporada em numérico.
'''
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')
unicos = df.nunique()
print('Analise de dados únicos:\n', unicos)

# Escreva seu código abaixo
scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

label_encoder = LabelEncoder()

df['Marca_Cod'] = label_encoder.fit_transform(df[['Marca']])
df['Material_Cod'] = label_encoder.fit_transform(df[['Material']])
df['Temporada_Cod'] = label_encoder.fit_transform(df[['Temporada']])