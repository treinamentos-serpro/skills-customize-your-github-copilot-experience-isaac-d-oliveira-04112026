# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Construa o clássico jogo da Forca, onde os jogadores adivinham letras para revelar uma palavra oculta antes de esgotar as tentativas. Você vai praticar manipulação de strings, loops, condicionais e seleção aleatória — e ao final terá um jogo completo para compartilhar com seus colegas!

## 📝 Tarefas

### 🛠️ Seleção da Palavra e Estado do Jogo

#### Descrição
Prepare a base do jogo: selecione uma palavra secreta aleatoriamente e inicialize as variáveis que controlam o estado da partida.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida usando o módulo `random`.
- Inicializar uma estrutura para armazenar as letras já adivinhadas.
- Definir o número máximo de tentativas incorretas permitidas.

### 🛠️ Loop Principal do Jogo

#### Descrição
Implemente o loop que mantém o jogo em andamento: exiba o progresso, receba os palpites do jogador e atualize o estado a cada rodada.

#### Requisitos
O programa concluído deve:

- Exibir o progresso atual da palavra no formato `_ _ _`, revelando as letras já acertadas.
- Aceitar palpites de letras do jogador usando `input()`.
- Verificar se a letra está na palavra secreta e atualizar o estado do jogo.
- Rastrear e exibir o número de tentativas incorretas restantes.

### 🛠️ Fim de Jogo: Vitória ou Derrota

#### Descrição
Finalize o jogo detectando quando o jogador vence ou perde e exibindo uma mensagem apropriada.

#### Requisitos
O programa concluído deve:

- Encerrar o loop quando a palavra for completamente adivinhada ou as tentativas esgotarem.
- Exibir uma mensagem de vitória revelando a palavra quando o jogador acertar.
- Exibir uma mensagem de derrota mostrando a palavra secreta quando as tentativas acabarem.
