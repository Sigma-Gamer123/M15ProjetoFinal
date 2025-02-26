import sys
import os

# Caminho absoluto do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Voltar atras no caminho absoluto (src)
sys.path.append(os.path.join(current_dir, '..'))

# Importar o create/insert, read e delete
from create.create_tables import create_tables
from read.show_agents import show_agents
from insert.insert_agents import insert_agents
from select_unselect.select_agent import select_agent
from select_unselect.unselect_agent import unselect_agent

if __name__ == "__main__":
    create_tables()
    insert_agents()
    # Enquanto estiver a correr
    while True:
        print("\nMenu:\n1. Select an agent\n2. Unselect agent\n3. Rage quit")
        choice = input()
        # Ações feitas baseado no input
        if choice == '1':
            team = "agent"
            show_agents(team)
            agent = input("\nWhich agent do you wish to select (1-26): ")
            select_agent(agent)
        elif choice == '2':
            team = "team"
            show_agents(team)
            agent_id = input("\nWhich agent do you wish to switch out(use their id): ")
            team = "agent"
            show_agents(team)
            agent1_id = input("\nWhich agent do you wish to switch in(use their id): ")
            unselect_agent(agent_id, agent1_id)

        elif choice == '3':
            print("AFK Offense: Penalty Administered")
            break # yep
        else:
            print("Inválido")