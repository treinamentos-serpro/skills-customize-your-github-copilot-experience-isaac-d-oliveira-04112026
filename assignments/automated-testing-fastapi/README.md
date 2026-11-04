# 📘 Assignment: Automated Testing for FastAPI

## 🎯 Objective

Aprenda a testar uma API FastAPI com `pytest` e `TestClient`. Use a API de tarefas da atividade anterior para verificar respostas corretas, casos de erro e o isolamento entre testes.

## 📝 Tasks

### 🛠️ Configure o ambiente e escreva o primeiro teste

#### Descrição
Depois de concluir a implementação da API na atividade **Building REST APIs com FastAPI**, prepare o projeto para testes automatizados e teste a rota inicial.

#### Requisitos
O programa concluído deve:

- Instalar `pytest` e `httpx` no mesmo ambiente da aplicação.
- Criar um arquivo `test_main.py` ao lado de `main.py` e importar a aplicação FastAPI.
- Criar um cliente de teste com `fastapi.testclient.TestClient`.
- Testar `GET /` e confirmar o status `200` e a mensagem de resposta esperada.
- Executar os testes com `pytest -q`.

### 🛠️ Teste criação, consulta e validação de tarefas

#### Descrição
Escreva testes para as rotas que listam e criam tarefas e para a consulta de uma tarefa específica, incluindo respostas de sucesso e erro.

#### Requisitos
O programa concluído deve:

- Confirmar que `GET /tasks` retorna uma lista vazia quando não há tarefas.
- Confirmar que `POST /tasks` retorna status `201` e os dados da tarefa criada, incluindo seu identificador.
- Confirmar que `GET /tasks/{task_id}` retorna a tarefa criada.
- Confirmar que a consulta de um identificador inexistente retorna status `404`.
- Confirmar que dados inválidos enviados para criar uma tarefa são rejeitados com status `422`.

### 🛠️ Teste atualização, remoção e isolamento

#### Descrição
Complete a cobertura das operações da API e garanta que os testes não dependam da ordem em que são executados.

#### Requisitos
O programa concluído deve:

- Confirmar que `PUT /tasks/{task_id}` atualiza os dados da tarefa e retorna status `200`.
- Confirmar que `DELETE /tasks/{task_id}` remove a tarefa e retorna status `204`.
- Confirmar que uma tarefa removida não pode mais ser consultada e que a resposta é `404`.
- Preparar os dados em memória antes de cada teste, limpando a coleção de tarefas e reiniciando o próximo identificador.
- Executar toda a suíte com `pytest -q` e confirmar que os testes passam independentemente da ordem de execução.