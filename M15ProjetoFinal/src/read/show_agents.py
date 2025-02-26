import sqlite3

def show_agents(team):
    # Conectar ao banco de dados
    conexao = sqlite3.connect("valorant.db")
    cursor = conexao.cursor()

    # Fetch all agents from the database
    cursor.execute(f'SELECT * FROM {team};')
    results = cursor.fetchall()
 
    # Display the results
    print("ID\tAgent\tRole")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")

    # Fechar a conexão
    conexao.close()