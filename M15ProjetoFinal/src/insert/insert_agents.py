import sqlite3

def insert_agents():
    # List of agents and their roles
    agents = [
        ('Brimstone', 'Controller'), ('Viper', 'Controller'), ('Omen', 'Controller'),
        ('Killjoy', 'Sentinel'), ('Cypher', 'Sentinel'), ('Sova', 'Initiator'),
        ('Sage', 'Sentinel'), ('Phoenix', 'Duelist'), ('Jett', 'Duelist'),
        ('Reyna', 'Duelist'), ('Raze', 'Duelist'), ('Breach', 'Initiator'),
        ('Skye', 'Initiator'), ('Yoru', 'Duelist'), ('Astra', 'Controller'),
        ('Kay/O', 'Initiator'), ('Chamber', 'Sentinel'), ('Neon', 'Duelist'),
        ('Fade', 'Initiator'), ('Harbor', 'Controller'), ('Gekko', 'Initiator'),
        ('Deadlock', 'Sentinel'), ('Iso', 'Duelist'), ('Clove', 'Controller'),
        ('Vyse', 'Sentinel'), ('Tejo', 'Initiator')
    ]

    # Connect to the database
    conexao = sqlite3.connect('valorant.db')
    cursor = conexao.cursor()

    # Insert each agent using a loop
    cursor.executemany("INSERT INTO agent (agent, role) VALUES (?, ?)", agents)

    # Commit changes and close the connection
    conexao.commit()
    conexao.close()
