# RogerioEoBot é o seu mais novo e eficiente consultor de rap 😎

## Chatbot com ChatterBot
## Este projeto implementa um chatbot utilizando a biblioteca ChatterBot em Python. 
A seguir, estão as instruções para configurar o ambiente de desenvolvimento, instalar as dependências necessárias e executar o projeto.

### Configuração do Ambiente

1. Criar o Ambiente Virtual no Anaconda

    Para criar um ambiente virtual utilizando o Anaconda, execute o seguinte comando:
    ```
    conda create --name chatbotpython python=3.6
    ```

2. Ativar o Ambiente Virtual

    Ative o ambiente virtual criado com o comando:
    ```
    conda activate chatbotpython
    ```

3. Instalar Jupyter

    Instale o Jupyter Notebook para facilitar o desenvolvimento e testes interativos:
    ```
    pip install jupyter
    ```

4. Instalar ChatterBot

    Instale a biblioteca ChatterBot, que será utilizada para criar o chatbot:
    ```
    pip install chatterbot
    ```

5. Instalar spaCy

    Instale a biblioteca spaCy, que ajuda no processamento de linguagem natural, corrigindo pequenos erros de digitação e pontuação:
    ```
    pip install spacy
    ```

6. Baixar o Modelo de Linguagem do spaCy

    Baixe o modelo de linguagem necessário para o spaCy:
    ```
    python -m spacy download en_core_web_sm
    ```

### Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
chatbot_project/
│
├── train_chatbot.py       # Script para treinar o chatbot
├── get_response.py        # Script para obter respostas do chatbot treinado
├── README.md              # Documentação do projeto
└── requirements.txt       # Lista de dependências do projeto
```

### Executando o Projeto

#### Treinando o Chatbot

Execute o script `train_chatbot.py` para treinar o chatbot:
```
python train_chatbot.py
```

#### Obtendo Respostas do Chatbot

Após treinar o chatbot, você pode obter respostas executando o script `get_response.py`:
```
python get_response.py
```

