
---

# Sistema de Gestão de Agentes do Valorant

## Visão Geral

Este projeto foi desenvolvido para permitir a gestão e interação com os agentes do jogo *Valorant* através de uma base de dados SQLite local. O sistema oferece funcionalidades para selecionar e desmarcar agentes de uma equipa, visualizar os agentes disponíveis na base de dados e registar as ações em um ficheiro de log para acompanhamento.

## Funcionalidades

### 1. **Criação de Tabelas**  
A aplicação começa criando as tabelas necessárias para armazenar informações sobre os agentes e a equipa. Caso as tabelas já existam, elas são descartadas e recriadas.

### 2. **Inserção de Agentes**  
Os agentes são inseridos na base de dados inicialmente com seus respectivos papéis, como 'Duelist', 'Controller', 'Sentinel' e 'Initiator'.

### 3. **Seleção de Agentes**  
Os agentes podem ser selecionados para a equipa, movendo-os da tabela de agentes disponíveis para a tabela de equipa. Isso é feito com base no ID do agente.

### 4. **Desmarcação de Agentes**  
Agentes podem ser desmarcados da equipa e movidos de volta para a tabela de agentes disponíveis.

### 5. **Visualização de Agentes**  
É possível visualizar os agentes disponíveis na base de dados, listando os agentes e seus respectivos papéis.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte maneira:

```
/valorant-agent-management
│
├── create
│   └── create_tables.py        # Criação das tabelas na base de dados
│
├── insert
│   └── insert_agents.py        # Inserção de agentes na base de dados
│
├── select_unselect
│   ├── select_agent.py         # Seleção de agentes
│   └── unselect_agent.py       # Desmarcação de agentes
│
├── read
│   └── show_agents.py          # Mostrar agentes existentes na base de dados
│
└── main.py                     # Arquivo principal que executa a aplicação
```

## Como Usar

1. **Criação e Inserção dos Agentes**  
   O sistema começa por criar as tabelas necessárias na base de dados e inserir um conjunto inicial de agentes com seus papéis.

2. **Interação com o Sistema**  
   Ao executar o arquivo `main.py`, o usuário verá um menu com as opções:
   - **1. Selecionar um agente**: Exibe os agentes disponíveis e permite que o usuário selecione um agente para a equipa.
   - **2. Desmarcar um agente**: Exibe os agentes na equipa e permite desmarcar um agente.
   - **3. Sair**: Finaliza a aplicação.

3. **Ações Registradas**  
   A cada interação, as ações do usuário são registradas e as tabelas da base de dados são atualizadas adequadamente.

## Requisitos

- Python 3.x
- SQLite3 (já incluído no Python)

## Conclusão

Este sistema permite uma gestão eficaz dos agentes no *Valorant* usando uma base de dados local. Através de um menu simples, os usuários podem interagir com a base de dados para selecionar, desmarcar e visualizar agentes.

---