import sqlite3

def create_tables():
    # Conectar à base de dados
    # Não precisamos do querie CREATE DATABASE porque com o sqlite3, a função connect() vai se ligar ao ficheiro dentro dos parenteses e se o ficheiro n existir, vai cria-lo
    conexao = sqlite3.connect('valorant.db')
    
    # "cursor" serve para escrever comandos de sql
    cursor = conexao.cursor()   
    
    cursor.execute("DROP TABLE agent")
    cursor.execute("DROP TABLE team")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agent (
        id_agent INTEGER PRIMARY KEY AUTOINCREMENT,       
        agent TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS team (
        id_agent INTEGER,       
        agent TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')
    
    # Confirmar alterações e fechar a conexão
    conexao.commit()
    conexao.close()