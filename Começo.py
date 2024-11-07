## FUNDO + CARRO
import pygame 

pygame.init()

clock = pygame.time.Clock()
FDS = 60 

WIDTH = 870
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️')


imagem_fundo = pygame.image.load('assets/img/RUA.png').convert()
window.blit(imagem_fundo,(0, 0))

imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))
imagem_fundo_rect = imagem_fundo.get_rect()
speed_fundo = 10


## CARRO VERMELHO 
imagem_carro_vermelho = pygame.image.load('assets/img/CARRO_VERMELHO.png').convert_alpha()
imagem_carro_vermelho_width = 300
imagem_carro_vermelho_height  = 300
imagem_carro_vermelho = pygame.transform.scale(imagem_carro_vermelho, (imagem_carro_vermelho_width, imagem_carro_vermelho_height))
imagem_carro_vermelho_rect = imagem_carro_vermelho.get_rect()
imagem_carro_vermelho_rect.centerx = WIDTH / 2 + 60 # Centraliza o carro horizontalmente
imagem_carro_vermelho_rect.centery = HEIGHT  # Centraliza o carro verticalmente BOTTOM 


loop = True 

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False 

    # Desenha a imagem de fundo
    window.blit(imagem_fundo, (0, 0))
    
    # Desenha o carro vermelho
    window.blit(imagem_carro_vermelho, (imagem_carro_vermelho_rect.x, imagem_carro_vermelho_rect.y))

    pygame.display.update()
    clock.tick(FDS)

pygame.quit()