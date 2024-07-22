# Gerenciador de Senhas para Controle de Fila de Espera

Este é um gerenciador de senhas simples para um sistema de controle de fila de espera. O sistema permite a inclusão de pessoas a serem atendidas e a exclusão, seguindo as regras especificadas abaixo.

## Funcionalidades

1. **Inclusão de Pessoas na Fila:**
   - A pessoa informa seu nome e se possui prioridade.
   - O sistema gera uma senha aleatória.
   - Monta um nó com as informações (nome, senha e prioridade).
   - A inclusão ocorre de acordo com as seguintes regras:
     - Se a pessoa não tiver prioridade, ela é inserida no final da fila.
     - Se a pessoa tiver prioridade:
       - A inclusão ocorre no final do último bloco de prioridades (ou cria um novo bloco, se necessário).
       - Cada bloco de prioridades pode ter até 2 pessoas.
       - Entre cada bloco de prioridades, pode haver até 2 pessoas sem prioridade.
       - A fila segue o formato: 1 bloco de prioridades, seguido de 1 bloco sem prioridades, e assim por diante.

2. **Exclusão de Pessoas da Fila:**
   - A exclusão ocorre como em uma fila comum.
   - Sempre a primeira pessoa da fila é atendida e removida.

3. **Estrutura da Fila:**
   - A fila é construída de forma encadeada.

## Exemplo de Uso

Suponhamos que temos as seguintes pessoas na fila:

1. João (prioridade)
2. Maria (prioridade)
3. Carlos (sem prioridade)
4. Ana (prioridade)
5. Pedro (sem prioridade)

Se uma nova pessoa chamada Laura (com prioridade) for adicionada, ela será inserida após Ana, formando um novo bloco de prioridades:

1. João (prioridade)
2. Maria (prioridade)
3. Carlos (sem prioridade)
4. Ana (prioridade)
5. Laura (prioridade)
6. Pedro (sem prioridade)

E, ao atender a primeira pessoa da fila (João), a fila ficará assim:

1. Maria (prioridade)
2. Carlos (sem prioridade)
3. Ana (prioridade)
4. Laura (prioridade)
5. Pedro (sem prioridade)

## Implementação

A implementação do gerenciador de senhas foi feita em Python em um único file .py a pedido do enunciado.
