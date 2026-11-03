# APS2 — Criptografia com Cifra de Vigenère

**Universidade Paulista (UNIP)**

**Curso:** Ciência da Computação  
**Atividade:** Atividades Práticas Supervisionadas — APS2  
**Aluno:** Álvaro Francisco Vitiello  
**Ano:** 2026

## Sobre o projeto

Este projeto foi desenvolvido como parte das Atividades Práticas Supervisionadas (APS2) do curso de Ciência da Computação da Universidade Paulista (UNIP).

O trabalho tem como objetivo estudar os fundamentos da criptografia e desenvolver uma aplicação em Python que demonstre o funcionamento da **Cifra de Vigenère**, uma técnica clássica de criptografia por substituição polialfabética.

A proposta está relacionada a um cenário de comunicação controlada envolvendo uma embarcação que transporta materiais tóxicos. Nesse contexto, o programa demonstra como mensagens e instruções podem ser cifradas antes de sua transmissão e recuperadas por um destinatário que conheça a mesma chave.

A aplicação possui finalidade educacional e não representa um sistema completo de segurança da informação.

## Funcionalidades

O programa apresenta as seguintes funcionalidades:

- Criptografia de mensagens utilizando a Cifra de Vigenère.
- Descriptografia de mensagens com a mesma chave utilizada na cifragem.
- Avaliação educativa da força da chave, classificada como **Fraca, Média ou Forte**.
- Análise do tamanho, diversidade de letras e previsibilidade da chave.
- Preservação de espaços, números, pontuação e caracteres não pertencentes ao alfabeto A–Z.
- Limitação das mensagens a **128 caracteres**.
- Validação de entradas e tratamento de erros.
- Interface interativa executada diretamente no terminal.

## Tecnologias utilizadas

- **Python 3:** linguagem utilizada para o desenvolvimento.
- **Biblioteca collections:** utilização da classe `Counter` para análise da frequência de caracteres.
- **GitHub:** armazenamento e versionamento do código-fonte.
- **GitHub Codespaces:** ambiente utilizado para execução e testes do programa.

O projeto utiliza apenas recursos da biblioteca padrão do Python, sem necessidade de instalar bibliotecas externas.

## Estrutura do projeto

O repositório contém:

- **criptografia.py:** código-fonte completo, incluindo as funções de cifragem, decifragem, análise da chave e interação com o usuário.
- **README.md:** documentação e apresentação do projeto.

## Como executar

1. Abra o projeto no GitHub Codespaces ou em um ambiente com Python 3 instalado.
2. Acesse o terminal na pasta do programa.
3. Execute o comando `python3 criptografia.py`.
4. Escolha uma das opções apresentadas pelo programa.

O menu principal oferece três opções:

- `1` — Cifrar mensagem
- `2` — Decifrar mensagem
- `3` — Sair

Após selecionar a operação, o usuário informa a chave e a mensagem desejada.

## Exemplo de funcionamento

**Mensagem original:** OLA MUNDO

**Chave utilizada:** SEGREDO

**Resultado criptografado:** GPG DYQRG

**Resultado descriptografado:** OLA MUNDO

O exemplo demonstra a transformação da mensagem original em texto cifrado e sua posterior recuperação por meio da mesma chave.

## Avaliação da força da chave

Além das operações de criptografia, o programa apresenta um avaliador educativo que considera características da chave informada pelo usuário.

São analisados critérios como comprimento, diversidade de letras, combinação de maiúsculas e minúsculas, repetições excessivas e presença de palavras previsíveis.

A classificação obtida tem finalidade exclusivamente didática e não constitui uma medida de segurança criptográfica real.

## Limitações

A Cifra de Vigenère possui importância histórica no desenvolvimento da criptografia, mas apresenta vulnerabilidades relacionadas à repetição das chaves e à análise estatística dos textos cifrados.

Por esse motivo, o programa foi desenvolvido exclusivamente para fins acadêmicos e não deve ser utilizado para proteger dados sensíveis ou comunicações reais que exijam segurança moderna.

## Considerações finais

O desenvolvimento do projeto permitiu aplicar conhecimentos de programação, matemática e segurança da informação em uma implementação prática.

A atividade possibilitou compreender o funcionamento de uma cifra clássica, a importância da escolha das chaves e as limitações de técnicas históricas diante das necessidades atuais de proteção da informação.

## Código-fonte

O programa completo está disponível no arquivo [criptografia.py](https://github.com/Playsasuke/APS2/blob/main/criptografia.py).
