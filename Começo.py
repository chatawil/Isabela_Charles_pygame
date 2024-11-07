## ADICIONANDO BARRICADAS

import pygame 
import random 

pygame.init()

clock = pygame.time.Clock()
FDS = 60 

WIDTH = 870
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️')


imagem_fundo = pygame.image.load('assets/img/RUA.png').convert()
# window.blit(imagem_fundo,(0, 0))
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


## BARRICADAS 
imagem_barricada = pygame.image.load('assets/img/barricada.png').convert_alpha()
imagem_barricada = pygame.transform.scale(imagem_barricada, (50, 50))
imagem_barricada_rect = imagem_barricada.get_rect()
imagem_barricada_rect.y = -imagem_barricada.get_height()

# Defina as faixas de estrada
faixas_estrada = [270, 405, 540]

barricada_speed = 10




# Função para reposicionar a barricada
def reposiciona_barricada():
    imagem_barricada_rect.x = random.choice(faixas_estrada)
    imagem_barricada_rect.y = -imagem_barricada.get_height()

reposiciona_barricada()









############################# LOOP PRINCIPAL ###################################

loop = True 

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    # Atualiza estado do jogo
    window.fill((0, 0, 0))

    # Atualiza a posição da imagem de fundo.
    imagem_fundo_rect.y += speed_fundo

    # Se o fundo saiu da janela, faz ele voltar para dentro.
    if imagem_fundo_rect.top >= HEIGHT:
        imagem_fundo_rect.y -= imagem_fundo_rect.height

    # Desenha o fundo e uma cópia para baixo.
    window.blit(imagem_fundo, imagem_fundo_rect)
    imagem_fundo_rect_2 = imagem_fundo_rect.copy()
    imagem_fundo_rect_2.y -= imagem_fundo_rect_2.height
    window.blit(imagem_fundo, imagem_fundo_rect_2)



    # Atualiza a posição da barricada
    imagem_barricada_rect.y += barricada_speed

    # Se a barricada saiu da janela, reposiciona ela no topo
    if imagem_barricada_rect.top >= HEIGHT:
        reposiciona_barricada()




    # # Verifica colisão
    # if imagem_carro_vermelho_rect.colliderect(imagem_barricada_rect):
    #     game_over()






## para aparecer elementos:

    # Desenha a barricada
    window.blit(imagem_barricada, imagem_barricada_rect)

    # Desenha o carro vermelho
    window.blit(imagem_carro_vermelho, imagem_carro_vermelho_rect)



    pygame.display.update()
    clock.tick(FDS)

pygame.quit()




