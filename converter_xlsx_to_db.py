import sqlite3
import pandas as pd

con = sqlite3.connect("laura.db")
# Editar o caminho do arquivo
wb=pd.ExcelFile(r'C:\caminho_do_arquivo\arquivo_excel.xlsx') # noqa
for sheet in wb.sheet_names:
        df=pd.read_excel(r'C:\caminho_do_arquivo\arquivo_excel.xlsx', sheet_name=sheet) # noqa
        df.to_sql(sheet, con, index=False, if_exists="replace")
con.commit()
con.close()
print('Excel convertido em banco de dados com sucesso.')
