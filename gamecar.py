import pygame
from random import randint

pygame.init()

posx = 540
posy = 200
posCarX = 330
posCarY = 800
posCarY2 = 1200
posCarY3 = 1600
velocidade = 20
velocidadeSecundaria = 20 
fundo = pygame.image.load("assets/asfaltoNovo.png")
carroPrincipal = pygame.image.load("assets/CarOne.png")
segundoCarro = pygame.image.load("assets/segundoCarro.png")
terceiroCarro = pygame.image.load("assets/terceiroCarro.png")
quartoCarro = pygame.image.load("assets/quartoCarro.png")
cronometro = 0
segundos = 0
fonte = pygame.font.SysFont('arial black', 30) 
texto = fonte.render("Tempo: ", True, (255,255,255), (0,0,0)) 
postexto = texto.get_rect()
postexto.center = (68,60) 
janela = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Desvio maluco") 
jogo = True 

while jogo :
    pygame.time.delay(50)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_RIGHT] and posx <= 650:
        posx += velocidade
    elif teclas[pygame.K_LEFT] and posx >= 327:
        posx -= velocidade

    elif (cronometro < 10):
        cronometro += 1
    else:
        segundos += 1
        texto = fonte.render("Cronômetro: "+str(segundos), True, (255,255,255), (0,0,0))
        cronometro = 0

    if (posCarY <= -200) and (posCarY2 <= -200) and (posCarY3 <= -200):
        posCarY = randint(800,1100) 
        posCarY2 = randint(1400,2000)
        posCarY3 = randint(2300,3000)

    posCarY -= velocidadeSecundaria + randint(1,10)
    posCarY2 -= velocidadeSecundaria + randint(1,10)
    posCarY3 -= velocidadeSecundaria + randint(1,10)

    janela.blit(fundo,(0,0)) 
    janela.blit(carroPrincipal, (posx,posy)) 
    janela.blit(segundoCarro, (posCarX, posCarY)) 
    janela.blit(terceiroCarro,(posCarX + 163, posCarY2)) 
    janela.blit(quartoCarro,(posCarX + 310, posCarY3)) 
    janela.blit(texto, postexto) 

    pygame.display.update()

pygame.quit()