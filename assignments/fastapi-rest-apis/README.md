# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Crie uma API REST para cadastrar e gerenciar tarefas usando o framework FastAPI. Nesta atividade, você vai praticar métodos HTTP, validação de dados, códigos de status e documentação interativa, desenvolvendo e testando a API passo a passo.

## 📝 Tarefas

### 🛠️ Criar e Executar a Aplicação

#### Descrição
Configure a aplicação FastAPI e prepare os modelos de dados que representarão as tarefas.

#### Requisitos
O programa concluído deve:

- Instalar as dependências listadas em `requirements.txt`.
- Criar uma aplicação FastAPI e um modelo de entrada com título e descrição.
- Iniciar a aplicação com `uvicorn main:app --reload`.
- Disponibilizar a documentação interativa em `/docs`.

### 🛠️ Consultar e Criar Tarefas

#### Descrição
Implemente os endpoints para listar as tarefas, consultar uma tarefa pelo identificador e criar novas tarefas.

#### Requisitos
O programa concluído deve:

- Retornar todas as tarefas em `GET /tasks`.
- Retornar uma tarefa em `GET /tasks/{task_id}` ou responder com status `404` quando ela não existir.
- Criar uma tarefa em `POST /tasks`, validar os dados recebidos e responder com status `201`.
- Guardar os dados em memória; eles podem ser reiniciados quando a aplicação for encerrada.

### 🛠️ Atualizar, Remover e Testar

#### Descrição
Complete as operações da API para atualizar e remover tarefas. Use a documentação interativa do FastAPI para testar cada endpoint.

#### Requisitos
O programa concluído deve:

- Atualizar título e descrição em `PUT /tasks/{task_id}` ou responder com status `404` se a tarefa não existir.
- Remover uma tarefa em `DELETE /tasks/{task_id}` e responder com status `204`, ou `404` se ela não existir.
- Permitir testar os endpoints pela interface em `/docs`.
