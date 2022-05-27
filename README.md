# Projeto Scraping E-sports
Esse projeto tem como objetivo desenvolver um processo de web crawling para estruturar dados de portais concorrentes de notícias, agregar métricas sobre esses dados e disponibilizar informações.


## Tecnologias
Aqui estão as tecnologias usadas neste projeto.

- Python 3.10.4
- MongoDB 5.0.8


## Desenvolvimento
1. Definição da área no qual serão extraído os dados.
    - Games:
        - League Of Legends
        - Counter-Strike: Global Offensive
<br/><br/>

2. Procurar sites com estruturas parecidas, ou seja, contiam os mesmos elementos como Autor, Data, Tags entre outos. Foram escolhidos:
    - Sites:
        - <a href='https://maisesports.com.br/'>MaisEsports</a>
        - <a herf='https://www.techtudo.com.br/e-sports/'>Techtudo Esports</a>
<br/><br/>

3. Escolha de Framework e Pacotes auxiliares.
    - Framework:
        - Scrapy - Muito usado no mercado, Rápido, Facilmente extensível e  Diversas alternativas para deploy.
    - Pacotes Auxiliares
        - Pymongo - Criado pela MongoDB, possui diversas funções que auxiliam durante o uso do MongoDB via python.
<br/><br/>

4. Desenvolvimento e organização do código.
    
    O programa foi desenvolvido de forma modular, afim de facilitar na detecção de erros, manutenção de código e reutilização de funções.

    ```bash
    │   mongo_script.txt #Comandos para criação de Database e Collection para o MongoDB
    │   README.md #Documentação
    │   requirements.txt #Pacotes e versões necessários para rodar o programa 
    │   run.py #Script que inicia todo o programa
    │   scrapy.cfg #Configurações do Scrapy
    │
    ├───esports
    │   │   items.py #Classe para padronização e manipulação dos dados
    │   │   pipelines.py #Classe para transformação e inserção de cada item em nossa Collection
    │   │   settings.py #Setados nossas configurações de projeto
    │   │   __init__.py
    │   │
    │   └───spiders
    │           maisesports.py #Classe criada para a extração de dados e retorno de item para o pipeline
    │           techtudo.py #Classe criada para a extração de dados e retorno de item para o pipeline
    │           __init__.py
    │
    └───logs #Pasta onde fica localizado os logs do sistema, são gerados automaticamente, sendo registrados pelo dia da execução
            2022-05-27.log
    ```
<br/><br/>

5. Extração, Transformação e Carregamento
    - Dados extraídos:
        - Site
        - Url
        - Título
        - Autor
        - Data de Publicação
        - Data de Extração
        - Tags

    - Transformações aplicadas:
        - Padronização da Data de Publicação
        - Remoção de espaços desnecessários nas tags
        - Caso o retorno das tags sejam listas vazias, definimos como tipo None
        - Verificação da quantidade de Autores

    - Carregamento dos dados:
        - Dados carregados ao final de sua passagem pelo pipeline
        - Somente são carregados dados novos, que não possuem registro em nosso Banco de Dados
<br/><br/>
6. Desempenho do programa


    Nossos logs salvam tudo que o programa execulta, lá podemos encontrar a métrica de tempo de execução, onde ficaram da seguinte maneira:

    - Techtudo Esports
        - Quantidade de Noticias - 19
        - Tempo de Execução - 25.71 segundos

    - MaisEsports
        - Quantidade de Noticias - 24
        - Tempo de Execução - 33.26 segundos

    O tempo de execução pode variar de acordo com os hardwares da máquina e velocidade da internet.
<br/><br/>
7. Deploy e Escalabilidade


    Para o deploy da aplicação, temos 3 alternativas:

    - Implantando em um servidor Scrapyd(indicado pelo framework)
        - Facilidade no deploy
        - Monitoramento
        - Agendamento via requisição HTTP/GET
        - Baixa Escalabilidade  
    - Implantando no Zyte Scrapy Cloud(indicado pelo framework)
        - Servidor em Nuvem
        - Interface gráfica
        - Gerenciar spiders, revisar itens, logs e estatísticas dos scrapings.
        - Alta Escalabilidade
    - Agendando nosso run.py em um servidor
        - Maior economia
        - Facilidade no deploy
        - Baixa Escalabilidade
<br/><br/>


## Começando

- Clone o repositório
```
$ git clone https://github.com/andreventura02/ProjetoScrapingEsports.git
```

- Abra o terminal e navegue até a pasta clonada
```
$ pip install -r requirements.txt
```

- Caso esteja utilizando linux, será necessário executar o comando abaixo
```
$ sudo apt install python3-scrapy
```

- Em seguida, execute os comandos localizados no arquivo <a href='https://github.com/andreventura02/Projeto_Scraping/blob/main/mongo_script.txt'>mongo_script.txt</a> para criar a Database e a Collection.

- Configure a conexão e modo de extração no arquivo <a href='https://github.com/andreventura02/Projeto_Scraping/blob/main/esports/settings.py'>esports/settings.py</a>
    - MONGO_URI - String de Conexão
    - MONGO_DATABASE - Nome da Database
    - ITEM_DAY - True raspa apenas os dados do dia, caso seja False ele raspa todos os dados disponíveis

- Necessário a criação de uma pasta chamada 'logs/'

- Após a configuração, vá até a raiz da pasta e execute
```
$ python run.py
```

## Análises Possíveis

Em nossos dados, podemos buscar por padrões, como:

- Processamento de Linguagem Natural nos títulos
- Analisar quais as tags mais utilizadas em ambos os sites
- Quais horários as noticias são postadas
- Quais os dias da semana em que mais são postados as noticias
