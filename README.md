# Projeto de Transmissão de Mensagens 📨

## Descrição:
Este projeto simula uma transmissão de mensagens entre um transmissor e um receptor através de diferentes camadas de comunicação.

## Estrutura do Projeto:

### 1. main.py
Este é o ponto de entrada do programa. Aqui, definimos as constantes que serão utilizadas em todo o programa e chamamos a função `aplicacaoTransmissora` para iniciar a transmissão.

### 2. transmissor.py
Este módulo define as funções e camadas responsáveis pela transmissão da mensagem. A mensagem é capturada, convertida em bits, passa por um controle de erros e, por fim, é enviada através de um meio de comunicação.

### 3. meiodecomunicacao.py
Este módulo simula o meio de comunicação. É aqui que os bits podem ser corrompidos de acordo com uma probabilidade definida. Após isso, os bits são passados para a camada física do receptor.

### 4. receptor.py
O receptor é responsável por receber a mensagem, verificar possíveis erros através do controle de erros definido e, em seguida, traduzir os bits recebidos de volta para a mensagem original.

### 5. utils.py
Aqui estão definidas várias funções auxiliares e constantes usadas em todo o programa. Este módulo também contém funções para calcular e verificar o erro na transmissão.

## Instalando as Dependências

O projeto possui um arquivo chamado `requirements.txt` que lista todas as bibliotecas necessárias para rodar o projeto. Para instalar essas bibliotecas, siga os passos abaixo:

1. Certifique-se de ter o Python instalado em sua máquina. Se ainda não tiver, você pode baixá-lo [aqui](https://www.python.org/downloads/).

2. É recomendável criar um ambiente virtual para o projeto. Isso evitará conflitos entre versões de bibliotecas usadas em diferentes projetos. Para criar e ativar um ambiente virtual:

   - No Windows:
     ```bash
     python -m venv nome_do_ambiente
     nome_do_ambiente\Scripts\activate
     ```

   - No MacOS/Linux:
     ```bash
     python3 -m venv nome_do_ambiente
     source nome_do_ambiente/bin/activate
     ```

3. Com o ambiente virtual ativado (ou não, caso opte por não criar um), navegue até a pasta do projeto e instale as bibliotecas listadas no `requirements.txt` utilizando o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

Pronto! Agora você já tem todas as dependências instaladas e pode executar o projeto corretamente.

## Como usar:

1. Defina as constantes no arquivo `utils.py` conforme necessário.
2. Execute o arquivo `main.py`.
3. Digite a mensagem que deseja transmitir.
4. Acompanhe o processo de transmissão e recepção da mensagem através das saídas no console.

## Autores:

- Beatriz Cardoso de Oliveira
- Heitor Tanoue de Mello - 12547260