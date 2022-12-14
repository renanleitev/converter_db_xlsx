import pandas as pd
import sqlite3
# Criando o arquivo Excel (alterar o caminho e o nome do arquivo)
filepath = r'C:\Users\caminho_do_arquivo\nome_do_arquivo_em_excel.xlsx' # noqa
# Conectando na base de dados (alterar o caminho e o nome do arquivo)
databasepath = r'C:\Users\caminho_da_base_de_dados\nome_da_base_de_dados.db'
con = sqlite3.connect(databasepath) # noqa
# Iniciando o processo de escrita no Excel
writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
# Obtendo o nome das tabelas na base de dados e salvando os dados
df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", con)
for table_name in df['name']:
    sheet_name = table_name
    SQL = "select * from " + sheet_name
    dft = pd.read_sql(SQL, con)
    # Escrevendo no Excel
    dft.to_excel(writer, sheet_name=sheet_name, index=False)
    # Ajustando o tamanho das colunas
    for column in dft:
        column_length = max(dft[column].astype(str).map(len).max(), len(column)) # noqa
        col_idx = dft.columns.get_loc(column)
        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_length)
print('Excel criado com sucesso.')
# Salvando o arquivo
writer.save()
