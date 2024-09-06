# Projeto Prático 1 - Automação com Selenium e pytest

Este projeto tem como objetivo automatizar um fluxo de compras em um site de demonstração utilizando Selenium com Python e pytest.

## Descrição do Projeto

O objetivo é automatizar o fluxo de interação com o site [Sauce Demo](https://www.saucedemo.com/), que inclui ações como login, adição e remoção de produtos do carrinho, e verificação de mensagens de confirmação.

## Funcionalidades Automatizadas

1. **Login no site**
2. **Fluxo de Compra**
   - Adicionar todos os 6 produtos disponíveis no carrinho.
   - Verificar se o carrinho exibe uma badge com 6 produtos.
   - Acessar o carrinho.
   - Remover um dos produtos.
   - Verificar se o carrinho exibe uma badge com 5 produtos.
   - Clicar no botão de Checkout.
   - Preencher os dados solicitados e clicar em Continue.
   - Clicar no botão Finish.
   - Verificar a mensagem de confirmação: "Thank you for your order!"

