import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re

#Criando função que cria o link de pesquisa dado uma entrada

def create_search_link(search_query):
    base_url = 'https://lista.mercadolivre.com.br/'
    encoded_query = search_query.replace(' ', '%20')
    search_link = f'{base_url}{encoded_query}#D[A:{encoded_query}]'
    return search_link

#Criando função que retira os links da página de pesquisa

def GetLinks(url):
    # Faz a requisição HTTP
    response = requests.get(url)

    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra todos os elementos <a> que contêm os links dos produtos
    links = soup.find_all('a', class_='ui-search-link')

    # Cria uma lista para armazenar os links dos produtos
    lista_links = []

    # Extrai os links e adiciona à lista
    for link in links:
        href = link.get('href')
        if href.startswith('https://produto.mercadolivre.com.br/'):
            lista_links.append(href)

    # Cria um DataFrame do Pandas com os links dos produtos
    df = pd.DataFrame({'Links': lista_links})

    # Remove as duplicatas do DataFrame
    df = df.drop_duplicates()

    # Organiza o índice em ordem crescente
    df = df.reset_index(drop=True)

    return df

#Criando função para extração de links dos comentários
def extrair_comentarios_mercadolivre(link):
    # Inicializar o driver do Selenium
    driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado e no PATH
    driver.get(link)
    
    # Aguardar o carregamento inicial da página
    time.sleep(5)
    
    # Rolar até o final da página
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Extrair o conteúdo HTML da página atual
    html = driver.page_source
    
    # Extrair os comentários com o Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    comentarios_html = soup.find_all('p', {'role': 'presentation', 'class': 'ui-review-capability-comments__comment__content'})
    
    # Extrair o texto dos comentários
    comentarios_texto = [comentario.text for comentario in comentarios_html]
    
    # Fechar o driver do Selenium
    driver.quit()
    
    return comentarios_texto

#Função final que junta todas as funções

def extract_comments_to_dataframe(search_query):
    # Cria o link de pesquisa
    search_link = create_search_link(search_query)
    
    # Obtém os links dos produtos
    df_links = GetLinks(search_link)
    
    # Inicializa o DataFrame final
    df_final = pd.DataFrame(columns=['Titulo', 'Link', 'Comentario'])
    
    # Itera sobre os links dos produtos
    for index, row in df_links.iterrows():
        link_produto = row['Links']
        
        # Obtém o link da página de comentários
        rev_link = GetRevLinks(link_produto)
        
        if rev_link is not None:
            # Faz a requisição HTTP para obter o título do anúncio
            response = requests.get(link_produto)
            soup = BeautifulSoup(response.text, 'html.parser')
            titulo = soup.find('h1', class_='ui-pdp-title').text.strip()
            
            # Extrai os comentários
            comentarios = extrair_comentarios_mercadolivre(rev_link)
            
            # Cria um DataFrame temporário com os títulos, links e comentários
            df_temp = pd.DataFrame({'Titulo': [titulo] * len(comentarios),
                                    'Link': [link_produto] * len(comentarios),
                                    'Comentario': comentarios})
            
            # Concatena o DataFrame temporário com o DataFrame final
            df_final = pd.concat([df_final, df_temp], ignore_index=True)
    
    return df_final

#Função que carrega arquivos e roda o webscraper

def process_product_list(file_path, output_file):
    # Carrega a lista de produtos do arquivo de texto
    with open(file_path, 'r') as file:
        lista_produtos_processada = file.read().splitlines()
    
    # Inicializa o DataFrame final
    df_final = pd.DataFrame(columns=['Titulo', 'Link', 'Comentario'])
    
    # Itera sobre os itens da lista de produtos
    for search_query in lista_produtos_processada:
        # Extrai os comentários para a consulta de pesquisa atual
        df_result = extract_comments_to_dataframe(search_query)
        
        # Concatena o DataFrame resultante com o DataFrame final
        df_final = pd.concat([df_final, df_result], ignore_index=True)
        
        # Exibe o número de linhas do DataFrame após cada iteração
        print(f"Número de linhas do DataFrame: {len(df_final)}")
        
        # Salva o DataFrame em um arquivo CSV após cada iteração
        df_final.to_csv(output_file, index=False)
    
    return df_final

%%time
file_path = 'lista_produtos_processada.txt'
output_file = 'resultados.csv'
df_result_final = process_product_list(file_path, output_file)

