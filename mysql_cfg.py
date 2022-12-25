import mysql.connector as mysql


conexao = mysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="estoque"
)

cursor = conexao.cursor()

name_tabela = 'produtos'

# Cria a tabela 

#cursor.execute(f"CREATE TABLE {name_tabela} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), telefone VARCHAR(100))")

#cursor.execute("SHOW TABLES") # exite as tabelas existenta 

# adiciona no banco de dados

def add(codigo,nome,quantidade): # add(nome,email,telefone)
    inserir = f"INSERT INTO {name_tabela} (codigo,nome,quantidade) VALUE(%s,%s,%s)"
    dados = (codigo,nome,quantidade)
    cursor.execute(inserir,dados)
    conexao.commit()
    #print(f'Adicionado {codigo} - {nome} - {quantidade}')

# remover um valor passando como parametro nome da coluna e a chave de pesquina 

def rem(nomecoluna,valor): # rem(coluna,valor)
    remover = f"DELETE FROM {name_tabela} WHERE {nomecoluna} = '{valor}'"
    cursor.execute(remover)
    conexao.commit()
    print(f'Excluido codigo: {valor} do tabela {nomecoluna}')

# atualizar tabela conforme parametros

def update(nomecoluna,valor,valor2): # update(coluna,novo valor,antigo valor)
    atualizar = f"UPDATE {name_tabela} SET {nomecoluna} = '{valor}' WHERE codigo = '{valor2}'"
    cursor.execute(atualizar)
    conexao.commit()
    print(f'Atualizado {nomecoluna} do codigo {valor2 } para {valor}')

# RETORNA A OS VALORES DA TABELA (REGISTRO)
def select():
    buscar = f'SELECT * FROM {name_tabela}'
    cursor.execute(buscar)
    result = cursor.fetchall()
    return result
    