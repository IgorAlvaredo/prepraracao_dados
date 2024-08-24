import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

dados_pessoas = []

for i in range(10000):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'
    nivel_educacao = random.choice(['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', 'Pós-Graduação',
                                    'Mestrado', 'Doutorado'])
    salario = random.randint(1500, 30000)
    numero_filhos = random.randint(0, 4)
    estado_civil = random.choice(['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)', None])
    area_atuacao = random.choice(['Tecnologia', 'Saúde', 'Educação', 'Engenharia', 'Administração', 'Marketing', None])

    if i % 43 == 0:
        cpf = None

    if i % 73 == 0:
        estado = None
        endereco = None

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais,
        'nivel_educacao': nivel_educacao,
        'salario': salario,
        'numero_filhos': numero_filhos,
        'estado_civil':estado_civil,
        'area_atuacao': area_atuacao
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.width', None)

print(df_pessoas.to_string())  # head() tail()

df_pessoas.to_csv('clientes-v2.csv')
