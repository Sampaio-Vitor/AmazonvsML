# Projeto de Análise de Sentimento de Comentários de Produtos

Este projeto consiste em uma aplicação de machine learning com webscraping para comparar a análise de sentimentos de comentários de produtos na Amazon e no Mercado Livre. O objetivo é utilizar processamento de linguagem natural (NLP) para calcular os escores de sentimento dos comentários e comparar as médias desses escores entre as duas plataformas.

## Funcionalidades
- Webscraping de avaliações de produtos listados em um txt.
- Leitura de arquivos CSV contendo os comentários de produtos da Amazon e do Mercado Livre.
- Cálculo dos escores de sentimento usando a biblioteca NLTK (Natural Language Toolkit).
- Comparação das médias dos escores de sentimento entre a Amazon e o Mercado Livre para um item selecionado.
- Identificação dos comentários com os escores mais baixos e mais altos para a Amazon e o Mercado Livre.

## Configuração do Ambiente

Certifique-se de ter as seguintes bibliotecas instaladas em seu ambiente de desenvolvimento:

- pandas
- numpy
- nltk
- googletrans
- tqdm
- requests
- bs4
- selenium
- webdriver (ChromeDriver)

## Instruções de Uso

1. Clone este repositório em seu ambiente de desenvolvimento local.

2. Certifique-se de ter os arquivos CSV contendo os comentários da Amazon (`reviews_amazon_english_nowarning_final.csv`) e do Mercado Livre (`reviews_meli_english_nowarning_final.csv`).

3. Execute o comando no terminal `python app_flask.py` para iniciar a aplicação.

4. Na aplicação web, selecione um item da lista apresentada e observe os resultados na página que abrir.

Para execução no ambiente python, utilize o `app.py`
## Arquivos do Projeto

- `app_flask.py`: Contém o código principal da aplicação, incluindo a leitura dos arquivos CSV, cálculo dos escores de sentimento, filtragem de comentários e exibição dos resultados.

- `translator.py`: Responsável pela tradução dos comentários do português para o inglês usando a biblioteca Google Translate.

- `amazon_scraper.py`: Realiza o web scraping dos comentários dos produtos na Amazon usando a biblioteca BeautifulSoup e requests.

- `meli_scraper.py`: Realiza o web scraping dos comentários dos produtos no Mercado Livre usando a biblioteca BeautifulSoup, Selenium e o webdriver do Chrome.

## Observações

- Certifique-se de ter as dependências necessárias instaladas em seu ambiente de desenvolvimento antes de executar o projeto.

- Os arquivos CSV contendo os comentários da Amazon e do Mercado Livre devem ser fornecidos e estar no mesmo diretório do projeto.

- Certifique-se de ter o ChromeDriver instalado e configurado corretamente para executar o web scraping na Amazon e no Mercado Livre.

- O arquivo `missing_values.txt` contém a lista de produtos a serem pesquisados nos websites. Certifique-se de fornecer os produtos de interesse nesse arquivo.

- Os resultados serão exibidos no terminal após a execução do programa. Certifique-se de que a saída do terminal seja compatível com caracteres especiais para evitar problemas na exibição dos resultados.

## Limitações


O desempenho do web scraping pode variar de acordo com a conexão com a Internet e a velocidade de resposta dos websites.

- O projeto atual é focado na comparação de comentários de produtos específicos entre a Amazon e o Mercado Livre. Não leva em consideração outros fatores que podem afetar a análise de sentimentos, como a reputação do vendedor, o número de vendas, etc.

- A tradução dos comentários do português para o inglês é realizada automaticamente, mas pode haver imprecisões ou erros de tradução.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request. Será um prazer receber feedbacks e melhorias para a aplicação.

## Deploy em EC2

Para realizar o deploy do aplicativo em um servidor Linux, foram seguidos os seguintes passos:

1. Criou-se uma instância EC2 na AWS.

2. Conectou-se à instância EC2 utilizando o PuTTY.

3. Instalou-se os pacotes necessários no servidor utilizando o gerenciador de pacotes.

4. Transferiu-se os arquivos do projeto para o servidor utilizando o WinSCP.

5. Utilizou-se o pacote `screen` para manter o servidor rodando mesmo após a desconexão do SSH.

6. O site ficou disponível na web através do acesso ao endereço IP público da instância EC2.

Esses passos permitiram a disponibilização do aplicativo web em um ambiente remoto para acesso público.

## Conclusão
Este projeto apresentou uma análise de sentimentos de comentários de produtos na Amazon e no Mercado Livre, utilizando técnicas de machine learning, webscraping e processamento de linguagem natural. Apesar das limitações encontradas, como a tradução automática e a disponibilidade limitada dos dados, o projeto foi capaz de fornecer insights interessantes sobre a percepção de qualidade dos produtos em ambas as plataformas.

Com a aplicação do projeto em um ambiente de produção na AWS, foi possível disponibilizar o aplicativo web de forma acessível através da internet. Isso permitiu que os usuários pudessem comparar os resultados de forma fácil e conveniente.

Em suma, este projeto demonstrou o poder da análise de sentimentos e do webscraping na comparação de plataformas de comércio eletrônico. Com melhorias contínuas e expansão do escopo do projeto, é possível obter insights ainda mais valiosos sobre a percepção dos clientes em relação aos produtos oferecidos pela Amazon e pelo Mercado Livre.

## Links Adicionais
Para mais detalhes sobre o projeto, você pode ler o artigo completo no [Medium](https://medium.com/@VitorCSampaio/compara%C3%A7%C3%A3o-de-percep%C3%A7%C3%A3o-de-qualidade-entre-amazon-e-mercado-livre-via-nlp-um-processo-passo-a-d5ff8a2c707).

O projeto está hosteado [neste link](http://ec2-18-231-173-40.sa-east-1.compute.amazonaws.com:8080/)


