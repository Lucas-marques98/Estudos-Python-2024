# PASSOS MANUAIS 

# # Entrar na planilha
import openpyxl
#copiar os dados da planilha
import pyperclip
#automatizar as tarefas
import pyautogui

#importando a biblioteca time, para dar uma pausa de uma página para a outra
from time import sleep

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx') #Variavel que chama a planilha
sheet_produtos = workbook['Produtos'] #Variavel que instancia a página de produtos da planilha


# # Copiar informação de um campo
for linha in sheet_produtos.iter_rows(min_row=2):
    #Nome do produto
    nome_produto = linha[0].value #copiando o valor da linha pelo indice
    pyperclip.copy(nome_produto)
    pyautogui.click(138,309,duration=1) #clicando com o mouse na linha do sistema e a duração que leva até fazer
    pyautogui.hotkey('ctrl', 'v') #usando o atalho de colar 
    
    #Descrição
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(170,394,duration=1)
    pyautogui.hotkey('ctrl', 'v')

   #Categoria
    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(164,525,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Código do produto
    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(113,616,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Peso do produto
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(98,703,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Dimensões
    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(100,795,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Botão concluir página 1
    pyautogui.click(98,847,duration=1)
    sleep(2) #tempo para a troca de página
    #FIM DA PÁGINA 1


    #Preço
    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(129,332,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Quantidade em estoque
    quantidade_estoque = linha[7].value
    pyperclip.copy(quantidade_estoque)
    pyautogui.click(108,423,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Data de validade
    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.click(100,506,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Cor
    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(115,593,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Tamanho
    tamanho = linha[10].value
    pyautogui.click(103,675,duration=1)
    #ler a informação da planilha
    if tamanho == 'Pequeno':
        pyautogui.click(127,718,duration=1)#se for pequeno 'clicar em uma informação'
    elif tamanho == 'Médio':
       pyautogui.click(104,741,duration=1)#se for médio 'clicar em outra informação'
    else:
        pyautogui.click(117,781,duration=1)#se for grande 'clicar na informação de grande'
   
    #Material
    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(104,763,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    #Botão concluir página 2
    pyautogui.click(111,823,duration=1)
    sleep(2) #tempo para a troca de página

    #FIM DA PÁGINA 2

    
    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(108,352,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    
    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(103,441,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    
    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(141,539,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    
    codigo_de_barras= linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(109,661,duration=1)
    pyautogui.hotkey('ctrl', 'v')

    
    localizacoes_armazem = linha[16].value
    pyperclip.copy(localizacoes_armazem)
    pyautogui.click(123,751,duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    #Botão concluir página 3
    pyautogui.click(111,804,duration=1)
    sleep(2) #tempo para a troca de página

    #FIM DA PÁGINA 3

    #Clicar em ok depois de concluir
    pyautogui.click(532,234,duration=1)
    sleep(2)

    #Clicar em adicionar mais um
    pyautogui.click(322,579,duration=1)
    sleep(2)



    

    





# e colar no seu campo correspondente
# # Repetir esses passos para outros campos
# até preencher campos daquela página
# # Clicar em próximo
# # Repetir os mesmos passos e ir para a
# próxima página (pagina 2)
# # Repetir os mesmos passos e finalizar
# o cadastro daquele produto e clicar em
# concluir
# # Clicar em ok, para finalizar o processo
# # Clicar no ok mais uma vez na mensagem
# de confirmação de salvamento no banco de 
# dados
# # Clicar em 'adicionar mais um e repetir
# o processo até finalizar a planilha'

