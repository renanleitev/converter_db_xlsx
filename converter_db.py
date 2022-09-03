import sys
import pandas as pd
import sqlite3
import os
from converter import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Novo(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        # Importando as funções
        super().__init__(parent)
        super().setupUi(self)
        super().retranslateUi(self)
        # Clicando nos botões
        self.escolherDB.clicked.connect(self.abrir_arquivo)
        self.escolherExcel.clicked.connect(self.abrir_arquivo)
        self.converter.clicked.connect(self.converter_arquivo)
        self.encerrarApp.clicked.connect(self.sair)

    def abrir_arquivo(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir arquivo',
            r'C:\Users',
            options=QFileDialog.DontUseNativeDialog
        )
        try:
            if arquivo.endswith('.xlsx') or arquivo.endswith('.db'):
                self.nomeArquivo.setText(arquivo)
            else:
                self.nomeArquivo.setText('Arquivo inválido.')
        except Exception as e:
            self.nomeArquivo.setText(f'Ocorreu o seguinte erro: {e}')
        self.arquivo = arquivo

    def converter_arquivo(self):
        try:
            if self.arquivo.endswith('.xlsx'):
                # Obtendo o nome da base de dados
                nome_db = os.path.basename(self.arquivo).replace('.xlsx', '')
                # Criando a base de dados
                con = sqlite3.connect(f'{nome_db}.db')
                # Abrindo o arquivo Excel
                wb=pd.ExcelFile(self.arquivo) # noqa
                # Inserindo valores na base de dados
                for sheet in wb.sheet_names:
                    df=pd.read_excel(self.arquivo, sheet_name=sheet) # noqa
                    df.to_sql(sheet, con, index=False, if_exists="replace")
                # Salvando as atualizações
                con.commit()
                con.close()
                path = os.path.abspath(f'{nome_db}.db')
                self.msgSucesso.setText(f'Base de dados salva em: {path}')
            elif self.arquivo.endswith('.db'):
                # Criando o arquivo Excel
                filepath = self.arquivo.replace('.db', '.xlsx') # noqa
                # Conectando na base de dados
                con = sqlite3.connect(self.arquivo) # noqa
                # Iniciando o processo de escrita no Excel
                writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
                # Obter o nome das tabelas na base de dados e salvando os dados
                df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", con) # noqa
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
                        writer.sheets[sheet_name].set_column(col_idx, col_idx, column_length) # noqa
                # Salvando o arquivo
                writer.save()
                self.msgSucesso.setText(f'Planilha salva em: {filepath}')
        except Exception as e:
            self.msgSucesso.setText(f'Ocorreu o seguinte erro: {e}')

    def sair(self):
        self.close()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
