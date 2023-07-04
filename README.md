# Projeto de Análise de Sentimento de Comentários de Produtos

Este projeto consiste em uma aplicação de machine learning com webscraping para comparar a análise de sentimentos de comentários de produtos na Amazon e no Mercado Livre. O objetivo é utilizar processamento de linguagem natural (NLP) para calcular os escores de sentimento dos comentários e comparar as médias desses escores entre as duas plataformas.

## Funcionalidades

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

3. Execute o arquivo `app.py` para iniciar a aplicação.

4. No terminal, selecione um item da lista apresentada. Digite o número correspondente ao item desejado e pressione Enter.

5. Aguarde o processamento dos comentários e a exibição dos resultados. Os resultados incluem a média dos escores de sentimento para a Amazon e o Mercado Livre, bem como os comentários com os escores mais baixos e mais altos para cada plataforma.

## Arquivos do Projeto

- `app.py`: Contém o código principal da aplicação, incluindo a leitura dos arquivos CSV, cálculo dos escores de sentimento, filtragem de comentários e exibição dos resultados.

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



- O desempenho do web scraping pode variar de acordo com a conexão com a Internet e a velocidade de resposta dos websites.

- O projeto atual é focado na comparação de comentários de produtos específicos entre a Amazon e o Mercado Livre. Não leva em consideração outros fatores que podem afetar a análise de sentimentos, como a reputação do vendedor, o número de vendas, etc.

- A tradução dos comentários do português para o inglês é realizada automaticamente, mas pode haver imprecisões ou erros de tradução.

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir um pull request. Será um prazer receber feedbacks e melhorias para a aplicação.
