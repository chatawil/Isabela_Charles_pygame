## ADICIONANDO MOVIMENTO AO CARRO 

import pygame 
import random 

pygame.init()

clock = pygame.time.Clock()
FDS = 60 

WIDTH = 870
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🏃🏽‍♂️🏃🏽‍♀️RUN GAME🏃🏽‍♀️🏃🏽‍♂️')


imagem_fundo = pygame.image.load('assets/img/RUA.png').convert_alpha()
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))
imagem_fundo_rect = imagem_fundo.get_rect()
speed_fundo = 10


## CARRO VERMELHO 
imagem_carro_vermelho = pygame.image.load('assets/img/CARRO.png').convert_alpha()
imagem_carro_vermelho_width = 170
imagem_carro_vermelho_height  = 160
imagem_carro_vermelho = pygame.transform.scale(imagem_carro_vermelho, (imagem_carro_vermelho_width, imagem_carro_vermelho_height))
imagem_carro_vermelho_rect = imagem_carro_vermelho.get_rect()
# posiciona carro em 405 
# imagem_carro_vermelho_rect.centerx = WIDTH / 2 #+ 60 # Centraliza o carro horizontalmente
# imagem_carro_vermelho_rect.centery = HEIGHT - 70 # Centraliza o carro verticalmente BOTTOM 



# Defina as faixas de estrada e posicione o carro inicialmente na faixa central (405)
faixas_estrada_carro = [300, 435, 570]
faixa_atual = 1  # Começa na faixa do meio (405)
imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]  # Centraliza o carro horizontalmente
imagem_carro_vermelho_rect.centery = HEIGHT - imagem_carro_vermelho_height / 2  # Centraliza o carro verticalmente no fundo


## BARRICADAS 
imagem_barricada = pygame.image.load('assets/img/barricada.png').convert_alpha()
imagem_barricada = pygame.transform.scale(imagem_barricada, (50, 50))
imagem_barricada_rect = imagem_barricada.get_rect()
imagem_barricada_rect.y = -imagem_barricada.get_height()

# Defina as faixas de estrada
faixas_estrada_barricada = [270, 405, 540]
barricada_speed = 10




# Função para reposicionar a barricada
def reposiciona_barricada():
    imagem_barricada_rect.x = random.choice(faixas_estrada_barricada)
    imagem_barricada_rect.y = -imagem_barricada.get_height()

reposiciona_barricada()





############################# LOOP PRINCIPAL ###################################

# Índice atual da faixa onde o carro está posicionado
faixa_atual = 1  # Começa no meio (faixa 405)

loop = True 

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    

 #### movimento teclas 
    # Captura as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Movimento para a esquerda
    if keys[pygame.K_LEFT]:
        if faixa_atual > 0:  # Verifica se não está na faixa mais à esquerda
            faixa_atual -= 1  # Move para a faixa à esquerda
            imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]
            pygame.time.wait(200)  # Pequena pausa para evitar movimento rápido demais

    # Movimento para a direita
    if keys[pygame.K_RIGHT]:
        if faixa_atual < len(faixas_estrada_carro) - 1:  # Verifica se não está na faixa mais à direita
            faixa_atual += 1  # Move para a faixa à direita
            imagem_carro_vermelho_rect.centerx = faixas_estrada_carro[faixa_atual]
            pygame.time.wait(150)  # Pequena pausa para evitar movimento rápido demais



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




## para aparecer elementos:

    # Desenha a barricada
    window.blit(imagem_barricada, imagem_barricada_rect)

    # Desenha o carro vermelho
    window.blit(imagem_carro_vermelho, imagem_carro_vermelho_rect)



    pygame.display.update()
    clock.tick(FDS)

pygame.quit()

