# Base de Dados: https://docs.python.org/3/library/sqlite3.html
import sqlite3
# Criando a base de dados
conexao = sqlite3.connect('laura.db')
# Conectando à base de dados
cursor = conexao.cursor()
# Para exibir os valores selecionados
# for row in cursor.execute("SELECT CLIENTE, PROCESSO, ANDAMENTO FROM ADV_ANDRESSA"): # noqa
#     print(row)
# Inserindo valores (atualizando os dias parados)
cursor.execute("UPDATE ADV_LAURA SET DIAS_PARADOS = JULIANDAY('now') - JULIANDAY(ÚLTIMA_MOVIMENTAÇÃO)") # noqa
cursor.execute("UPDATE ADV_ANDRESSA SET DIAS_PARADOS = JULIANDAY('now') - JULIANDAY(ÚLTIMA_MOVIMENTAÇÃO)") # noqa
# cursor.execute("UPDATE ADV_ALVES_PASSOS SET DIAS_PARADOS = JULIANDAY('now') - JULIANDAY(ÚLTIMA_MOVIMENTAÇÃO)") # noqa
# Para salvar as alterações:
conexao.commit()
# Para encerrar as alterações:
conexao.close()
