# Seletor de Agentes do Valorant

Uma aplicação de linha de comandos (CLI) em Python para selecionar e gerir agentes do Valorant utilizando uma base de dados SQLite. A aplicação permite criar tabelas, inserir agentes, visualizar agentes, selecionar um agente para a equipa e desselecioná-lo.

---

## Estrutura do Projeto
```
src/
├── app/
│   ├── main.py              # Menu principal da aplicação
│   ├── create/
│   │   └── create_tables.py # Cria as tabelas agent e team
│   ├── insert/
│   │   └── insert_agents.py # Insere agentes predefinidos na base de dados
│   ├── read/
│   │   └── show_agents.py   # Mostra agentes da base de dados
│   └── select_unselect/
│       ├── select_agent.py  # Seleciona um agente para a equipa
│       └── unselect_agent.py# Desseleciona um agente da equipa
├── valorant.db              # Base de dados SQLite
└── README.md                # Documentação do projeto
```

---

## Começar

### Pré-requisitos
- Python 3.x instalado.
- SQLite3 (já incluído com Python).

### Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <pasta-do-repositorio>
   ```
2. Navegue até ao diretório `src/app`:
   ```bash
   cd src/app
   ```
3. Execute a aplicação:
   ```bash
   python main.py
   ```

---

## Utilização
Ao iniciar a aplicação, verá o seguinte menu:
```
Menu:
1. Selecionar um agente
2. Desselecionar agente
3. Sair
```

### Opções:
1. **Selecionar um agente:**
   - Mostra os agentes disponíveis.
   - Permite escolher um agente pelo ID.
   - Move o agente selecionado para a equipa.

2. **Desselecionar agente:**
   - Mostra os membros atuais da equipa.
   - Permite escolher um agente para retirar e outro para adicionar.

3. **Sair:**
   - Sai da aplicação com uma mensagem divertida.

---

## Descrição dos Ficheiros

### `main.py`
Controla o menu principal e as entradas do utilizador, chamando funções para criar tabelas, inserir agentes, visualizar agentes e gerir seleções.

### `create_tables.py`
- Cria as tabelas `agent` e `team`.
- Elimina tabelas existentes para um reinício limpo.

### `insert_agents.py`
- Insere 26 agentes predefinidos com os seus papéis na tabela `agent`.

### `show_agents.py`
- Exibe agentes das tabelas `agent` ou `team` com os respetivos IDs, nomes e papéis.

### `select_agent.py`
- Move um agente da tabela `agent` para a `team` com base no ID indicado.

### `unselect_agent.py`
- Move um agente da `team` de volta para a `agent` e permite substituir por outro agente.

---

## Estrutura da Base de Dados
### Tabela `agent`:
| Coluna     | Tipo     | Descrição                  |
|------------|----------|----------------------------|
| id_agent   | INTEGER  | Chave primária, autoincremento |
| agent      | TEXT     | Nome do agente             |
| role       | TEXT     | Função do agente (ex.: Duelist, Controller) |

### Tabela `team`:
| Coluna     | Tipo     | Descrição                  |
|------------|----------|----------------------------|
| id_agent   | INTEGER  | Referência ao ID do agente |
| agent      | TEXT     | Nome do agente             |
| role       | TEXT     | Função do agente           |

---

## Exemplo de Execução
```bash
Menu:
1. Select an agent
2. Unselect agent
3. Rage quit

> 1
ID	Agent	Role
1	Brimstone	Controller
2	Viper	Controller
...
Which agent do you wish to select (1-26):2
Agent selected successfully.
```

---

## Licença
Este projeto foi desenvolvido para fins educativos.
