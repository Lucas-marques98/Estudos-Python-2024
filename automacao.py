import pyautogui as robo #o pyautogui vai ser chamado de robo
import time 


#Funçõs de pegar posição do mouse e da tela
print(robo.position())
print(robo.size())

#Funções do mouse
time.sleep(5) #Antes dele clicar eu quero que ele espera o tempo que eu determinar
robo.click(x=898, y=171,button ='left') #Para ele clicar temos que passar as posições X = e Y =

#Podemos usar o parametro button para escolher qual botão clicar do mouse  'left para clicar com o botão esquerdo', 'middle para clicar com o botão do meio do mouse', ou 'right para clicar com o segundo botão do mouse'.