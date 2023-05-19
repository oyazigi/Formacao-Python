import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "financial_examples.xlsx"
#abrindo arquivo
df = pd.read_excel(excel_file_path)
#mudando nome da coluna
df = df.rename(columns={'Businees Unit': 'Business Unit'})
#Mostrando primeiros 10 registros
print(df.head(10))
#Mostrando tamanho da tabela
print(df.shape)
#Verificando quanto o ramo de software faturou em janeiro
software_jan_data = df.loc[df['Business Unit'] == 'Software', ['Account', 'Jan']]
account_sum = software_jan_data.groupby('Account')['Jan'].sum()
print(account_sum)
#Calculando quanto foram as vendas por setor no mes de novembro
software_nov_data = df.loc[df['Account'] == 'Sales', ['Business Unit', 'Nov']]
account_sum = software_nov_data.groupby('Business Unit')['Nov'].sum()
print(account_sum)
#Mostrando um gráfico personalizado com os dados da última análise
ax = account_sum.plot(kind='bar')
ax.set_title("Vendas por setor no mês de novembro!")
ax.set_xlabel("Setor")
ax.set_ylabel("Soma das vendas")
ax.patch.set_facecolor('black')
ax.legend(loc='upper right')
plt.show()