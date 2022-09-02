import sqlite3
import pandas as pd


con = sqlite3.connect("laura.db")
wb=pd.ExcelFile(r'C:\Users\renan\Documents\Programação\VsCode\Acomp Processual - Renan.xlsx') # noqa
for sheet in wb.sheet_names:
        df=pd.read_excel(r'C:\Users\renan\Documents\Programação\VsCode\Acomp Processual - Renan.xlsx', sheet_name=sheet) # noqa
        df.to_sql(sheet, con, index=False, if_exists="replace")
con.commit()
con.close()

print('ok')
