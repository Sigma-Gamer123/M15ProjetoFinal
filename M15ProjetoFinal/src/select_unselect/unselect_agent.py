import sqlite3

def unselect_agent(agent_id, agent1_id):
    # Connect to the database
    conexao = sqlite3.connect('valorant.db')
    cursor = conexao.cursor()

    try:
        # Step 1: Select the row from the team table
        cursor.execute('SELECT * FROM team WHERE id_agent = ?', (agent_id,))
        row = cursor.fetchone()
        
        if row is None:
            print("No agent found with the given ID in the team.")
            return
        
        # Step 2: Check if the agent already exists in the agent table
        cursor.execute('SELECT * FROM agent WHERE id_agent = ?', (row[0],))
        existing_agent = cursor.fetchone()
        
        if existing_agent is None:
            # Step 3: Insert the row into the agent table
            cursor.execute('''
                INSERT INTO agent (id_agent, agent, role)
                VALUES (?, ?, ?)
            ''', (row[0], row[1], row[2]))  # Adjust indices based on your table structure
        else:
            print("Agent already exists in the agent table. Updating the existing record.")
            # Optionally, update the existing record instead of inserting
            cursor.execute('''
                UPDATE agent
                SET agent = ?, role = ?
                WHERE id_agent = ?
            ''', (row[1], row[2], row[0]))

        # Step 3: Delete the row from the source table
        cursor.execute('DELETE FROM team WHERE id_agent = ?', (agent_id))

        # Step 4: Select the row from the agent table
        cursor.execute('SELECT * FROM agent WHERE id_agent = ?', (agent1_id,))
        row = cursor.fetchone()
        
        if row is None:
            print("No agent found with the given ID in the team.")
            return

        # Step 5: Update the team table
        cursor.execute('''
                INSERT INTO team (id_agent, agent, role)
                VALUES (?, ?, ?)
            ''', (row[0], row[1], row[2]))

        # Commit the changes
        conexao.commit()
        print("Agent unselected successfully.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conexao.rollback()  # Rollback in case of error
    
    finally:
        # Close the connection
        conexao.close()