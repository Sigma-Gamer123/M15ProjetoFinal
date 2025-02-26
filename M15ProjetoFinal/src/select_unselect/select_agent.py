import sqlite3

def select_agent(agent):
    # Connect to the database
    conexao = sqlite3.connect('valorant.db')
    cursor = conexao.cursor()

    try:
        # Step 1: Select the row from the source table
        cursor.execute('SELECT * FROM agent WHERE id_agent = ?', (agent))
        row = cursor.fetchone()
        
        if row is None:
            print("No agent found with the given ID.")
            return
        
        # Step 2: Insert the row into the destination table
        cursor.execute('''
            INSERT INTO team (id_agent, agent, role)
            VALUES (?, ?, ?)
        ''', (row[0], row[1], row[2]))  # Adjust indices based on your table structure
        
        # Step 3: Delete the row from the source table
        cursor.execute('DELETE FROM agent WHERE id_agent = ?', (agent))
        
        # Commit the changes
        conexao.commit()
        print("Agent selected successfully.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conexao.rollback()  # Rollback in case of error
    
    finally:
        # Close the connection
        conexao.close()