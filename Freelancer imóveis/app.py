# Passos Manuais

# 1 - Entrar no site: 
# https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4


# 2 - Inseri o preço, link da casa, data dentro de uma planilha que eu criei

# 3 = Anotar os preços, links das casas e datas de cada um dos anúncios daquela página

# 4 - se houver mais páginas, fazer o mesmo nas outras páginas


from selenium import webdriver as webdv
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

# 1 - Entrar no site: 
# https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4
#Iniciando o navegador google chrome
driver = webdv.Chrome()

driver.get('https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=L&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4')
input('')

# 2 - Inseri o preço, link da casa, data dentro de uma planilha que eu criei
precos = driver.find_elements(By.XPATH,"//div[@class='card-valores']/div") #Extrai a informação através da tag e atributo
links = driver.find_elements(By.XPATH,"//a[@class='carousel-cell']")

#inserindo dentro da planilha
workbook = openpyxl.load_workbook('Pnl_Imóveis.xlsx')
pagina_planilha = workbook['Página1']


for preco,link in zip(precos,links):
    preco_formatado = preco.text.split(' ')[1] #separando o preço pelo indice, pegando somente os números
    link_pronto = link.get_attribute('href') #pegando o link pelo atributo
    data_atual = datetime.now().strftime('%d/%m/%Y')
    pagina_planilha.append([preco_formatado,link_pronto,data_atual])


workbook.save('Pnl_Imóveis.xlsx')