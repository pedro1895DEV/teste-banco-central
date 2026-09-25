import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as px
import numpy as np

with pd.ExcelFile('exercicio-excel.xlsx') as xls:
    adesao = pd.read_excel(xls, sheet_name=0)
    formacao_professores = pd.read_excel(xls, sheet_name='Formação - Professores')
    formacao_gestores = pd.read_excel(xls, sheet_name='Formação - Gestores')
    estudantes = pd.read_excel(xls, sheet_name='Estudantes e Turmas')

# Escolas com alunos cadastrados (> 0)
escolas_com_alunos = estudantes[estudantes['Alunos cadastrados'] > 0]['Cod Escola'].unique()

# Escolas com professores ou gestores que iniciaram formação (data de início preenchida)
escolas_com_professores = formacao_professores[formacao_professores['Data de início da formação'].notna()]['Cod Escola'].unique()
escolas_com_gestores = formacao_gestores[formacao_gestores['Data de início da formação'].notna()]['Cod Escola'].unique()

#  Escolas que aderiram ao programa a partir de 28/05/2021
filtro_adesao = (adesao['Escola aderiu?'] == 'Sim') & (adesao['Data de adesão da escola'] >= '2021-05-28')

# Une os dois grupos (professores OU gestores que iniciaram formação)
escolas_com_profissionais = set(escolas_com_professores) | set(escolas_com_gestores)
escolas_aderiram = adesao[filtro_adesao]
tem_profissionais = escolas_aderiram['Cod Escola'].isin(escolas_com_profissionais)
tem_alunos = escolas_aderiram['Cod Escola'].isin(escolas_com_alunos)

# Escolas inativas: Aderiram ao programa, mas NÃO têm alunos e NÃO têm profissionais em formação
filtro_inativas = (~tem_alunos) & (~tem_profissionais)

# Escolas que não têm estudantes cadastrados, mas têm profissionais que iniciaram a formação
filtro_apenas_profissionais = ((~tem_alunos) & (tem_profissionais))

# Escolas que têm estudantes cadastrados, mas não têm profissionais que iniciaram a formação
filtro_apenas_estudantes = ((tem_alunos) & (~tem_profissionais))

# Escolas que têm estudantes cadastrados E profissionais que iniciaram a formação
filtro_estudantes_e_profissionais = ((tem_alunos) & (tem_profissionais))

# Escolas que têm estudantes cadastrados OU profissionais que iniciaram a formação
filtro_estudantes_ou_profissionais = ((tem_alunos) | (tem_profissionais))

escolas_inativas = escolas_aderiram[filtro_inativas]
escolas_apenas_profissionais = escolas_aderiram[filtro_apenas_profissionais]
escolas_apenas_estudantes = escolas_aderiram[filtro_apenas_estudantes]
escolas_estudantes_e_profissionais = escolas_aderiram[filtro_estudantes_e_profissionais]
escolas_estudantes_ou_profissionais = escolas_aderiram[filtro_estudantes_ou_profissionais]
total_inativas = escolas_inativas['Cod Escola'].nunique()
print(f'Número de escolas distintas que aderiram ao programa: {escolas_aderiram["Cod Escola"].nunique()}')
print(f'Número de escolas inativas: {total_inativas}')
print(f'Número de escolas que não têm estudantes cadastrados, mas têm profissionais que iniciaram a formação: {escolas_apenas_profissionais["Cod Escola"].nunique()}')
print(f'Número de escolas que têm estudantes cadastrados, mas não têm profissionais que iniciaram a formação: {escolas_apenas_estudantes["Cod Escola"].nunique()}')
print(f'Número de escolas que têm estudantes cadastrados E profissionais que iniciaram a formação: {escolas_estudantes_e_profissionais["Cod Escola"].nunique()}')
print(f'Número de escolas que têm estudantes cadastrados OU profissionais que iniciaram a formação: {escolas_estudantes_ou_profissionais["Cod Escola"].nunique()}')

# Cada um dos blocos comentados abaixo pode ser descomentado para exibir a distribuição por Estado das escolas em cada categoria. 

# escolas_inativas_por_estado = escolas_inativas.groupby('Estado')['Cod Escola'].nunique()
# print('Distribuição por Estado das escolas inativas:')
# print(escolas_inativas_por_estado)

# escolas_apenas_profissionais_por_estado = escolas_apenas_profissionais.groupby('Estado')['Cod Escola'].nunique()
# print('Distribuição por Estado das escolas que não têm estudantes cadastrados, mas têm profissionais que iniciaram a formação:')
# print(escolas_apenas_profissionais_por_estado)

# escolas_apenas_estudantes_por_estado = escolas_apenas_estudantes.groupby('Estado')['Cod Escola'].nunique()
# print('Distribuição por Estado das escolas que têm estudantes cadastrados, mas não têm profissionais que iniciaram a formação:')
# print(escolas_apenas_estudantes_por_estado)

# escolas_estudantes_e_profissionais_por_estado = escolas_estudantes_e_profissionais.groupby('Estado')['Cod Escola'].nunique()
# print('Distribuição por Estado das escolas que têm estudantes cadastrados E profissionais que iniciaram a formação:')
# print(escolas_estudantes_e_profissionais_por_estado)

# escolas_estudantes_ou_profissionais_por_estado = escolas_estudantes_ou_profissionais.groupby('Estado')['Cod Escola'].nunique()
# print('Distribuição por Estado das escolas que têm estudantes cadastrados OU profissionais que iniciaram a formação:')
# print(escolas_estudantes_ou_profissionais_por_estado)

plt.figure(figsize=(10, 6))
plt.grid(axis='y', linestyle='--', alpha=0.5)

dados_grafico = pd.Series({
    'Inativas': total_inativas,
    'Apenas Profissionais': escolas_apenas_profissionais["Cod Escola"].nunique(),
    'Apenas Estudantes': escolas_apenas_estudantes["Cod Escola"].nunique(),
    'Estudantes e Profissionais': escolas_estudantes_e_profissionais["Cod Escola"].nunique(),
    'Estudantes ou Profissionais': escolas_estudantes_ou_profissionais["Cod Escola"].nunique()
}).sort_values(ascending=False)

plt.bar(dados_grafico.index, dados_grafico.values, color='steelblue')
plt.xlabel('Categoria')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo')
plt.xticks(rotation=45)
plt.tight_layout()

plt.figure(figsize=(12, 6))
plt.grid(axis='y', linestyle='--', alpha=0.5)

dados_grafico_inativas = (
    escolas_inativas.groupby('Estado')['Cod Escola']
    .nunique()
    .sort_values(ascending=False)
)

plt.bar(dados_grafico_inativas.index, dados_grafico_inativas.values, color='crimson')
plt.xlabel('Estado')
plt.ylabel('Número de Escolas Inativas')
plt.title('Distribuição de Escolas Inativas por Estado')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()