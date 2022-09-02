# Base de Dados: https://docs.python.org/3/library/sqlite3.html
import sqlite3
# Criando a base de dados
conexao = sqlite3.connect('nome_da_base_de_dados.db')
# Conectando à base de dados
cursor = conexao.cursor()
# Inserindo valores (diferença entre datas)
cursor.execute("UPDATE NOME_DA_TABELA SET COLUNA_DA_TABELA_COM_DIFERENÇA_DIAS = JULIANDAY('now') - JULIANDAY(COLUNA_DA_TABELA_COM_DATA)") # noqa
# Para salvar as alterações:
conexao.commit()
# Para encerrar as alterações:
conexao.close()
