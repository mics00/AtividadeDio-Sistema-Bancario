# AtividadeDio-Sistema-Bancario
Sistema Bancário - Python

Este é um simples sistema bancário desenvolvido em Python. O programa permite ao usuário realizar operações bancárias, como depositar, sacar, visualizar o extrato de suas transações, e encerrar a sessão. Ele oferece um controle de limite de saques diários e impede a realização de operações inválidas.

Funcionalidades

Depósito: O usuário pode depositar um valor positivo na conta.
Saque: O usuário pode sacar até o limite diário, respeitando o limite de saques diários e o saldo disponível.
Extrato: O usuário pode visualizar o extrato das transações realizadas.
Encerrar sessão: O usuário pode encerrar sua conta.
Requisitos

Python 3.x instalado no seu sistema.
O código não possui dependências externas.
Como usar

Clone o repositório ou baixe o código.
Abra o terminal e navegue até o diretório onde o arquivo está localizado.
Execute o arquivo com o comando:
python sistemaBancario.py
O programa apresentará um menu com as opções:
[1] Depositar: Permite que o usuário deposite um valor na conta.
[2] Sacar: Permite que o usuário saque um valor, respeitando os limites de saque diário e saldo.
[3] Extrato: Exibe o histórico de transações realizadas.
[4] Sair: Encerra a sessão bancária.
O programa pedirá para o usuário inserir o valor desejado para cada operação.
Regras do Sistema

O usuário pode realizar até 3 saques diários.
O saque só será permitido se houver saldo suficiente.
O limite de saque é de R$ 500,00 por transação.
Valores de saque inválidos (zero ou negativos) não serão aceitos.
Os depósitos negativos ou iguais a zero não são permitidos.
O extrato exibe todas as transações realizadas, incluindo depósitos e saques.
Exemplo de Execução

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair 

=> 1
--- Depósito ---
Qual valor você deseja depositar? 1000
Depósito de R$ 1000.00 realizado com sucesso!

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair 

=> 2
--- Saque ---
Digite o valor a ser sacado: R$ 200
Saque de R$ 200.00 realizado com sucesso!

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair 

=> 3
---- Extrato ----
Depósito: R$ 1000.00
Saque de R$ 200.00

Saldo atual: R$ 800.00
Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Se você encontrar um erro, por favor, abra um issue ou envie um pull request.