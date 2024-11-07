## FUNDO

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


loop = True 

while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False 

    imagem_fundo

    pygame.display.update()
